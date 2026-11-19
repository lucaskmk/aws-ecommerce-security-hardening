#!/usr/bin/env python3
"""Recria as duas figuras da matriz de risco a partir da planilha v2.

Uso:  python gerar_figuras.py [--lang pt|en]     (requer matplotlib e openpyxl)

Lê, na aba de ameaças e riscos, a probabilidade e o impacto originais (colunas
G e H), os residuais (P e Q) e o status (O) de cada risco, e grava:

  --lang pt (padrão):
    figuras/01_mapa_calor_original_vs_residual.png   (slide 4)
    figuras/02_grafico_riscos_antes_x_depois.png     (slide 11)
  --lang en:
    figuras/en/01_risk_heatmap_original_vs_residual.png
    figuras/en/02_risk_chart_before_after.png

Rode de novo sempre que uma nota da matriz mudar e, em seguida, rode
gerar_apresentacao.py para levar as figuras novas aos slides.
"""

import argparse
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
MATRIZ = ROOT / "Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.xlsx"
PRIMEIRA_LINHA = 10  # primeira linha de risco na aba (ID 1)

CLASSES = ["Extremo", "Alto", "Moderado", "Baixo"]
FAIXAS = {"Extremo": "> 9", "Alto": "7–9", "Moderado": "3–6", "Baixo": "1–2"}
CORES = {"Extremo": "#dc2626", "Alto": "#f97316", "Moderado": "#facc15", "Baixo": "#22c55e"}
ESCURO = "#0f172a"
FORA_DO_LABORATORIO = ("Plano proposto", "Fora de escopo")

# Textos das figuras por idioma. As chaves internas (classes, status) seguem a planilha, em português.
TEXTOS = {
    "pt": {
        "pasta": "figuras",
        "arquivo_01": "01_mapa_calor_original_vs_residual.png",
        "arquivo_02": "02_grafico_riscos_antes_x_depois.png",
        "classes": {"Extremo": "Extremo", "Alto": "Alto", "Moderado": "Moderado", "Baixo": "Baixo"},
        "probabilidades": ["Improvável", "Possível", "Provável", "Quase Certa"],
        "impactos": ["Baixo", "Moderado", "Alto", "Catastrófico"],
        "eixo_x": "IMPACTO",
        "eixo_y": "PROBABILIDADE",
        "ids": "IDs: ",
        "titulo_mapa": "MaisPlace (Grupo G3) — Mapa de Calor de Riscos: Original vs. Residual ({n} Riscos)",
        "painel_original": "Risco Original (Ambiente Legado)",
        "painel_residual": "Risco Residual (Ambiente AWS Implementado)",
        "eixo_quantidade": "Quantidade de Riscos (Total = {n})",
        "titulo_grafico": "MaisPlace (Grupo G3) — Redução de Riscos Cibernéticos: Antes x Depois",
        "legenda_original": "Risco Original (Legado)",
        "legenda_residual": "Residual: {c}",
        "quadro": ("Impacto da Migração + Controles:\n"
                   "• Extremos: {e0} → {e1} ({ve})\n"
                   "• Extremo + Alto: {a0} → {a1} ({va})\n"
                   "• Moderados: {m0} → {m1} (redução de criticidade)\n"
                   "• {fora} dos {a1} restantes são organizacionais\nou fora de escopo do laboratório"),
        "decimal": ",",
    },
    "en": {
        "pasta": "figuras/en",
        "arquivo_01": "01_risk_heatmap_original_vs_residual.png",
        "arquivo_02": "02_risk_chart_before_after.png",
        "classes": {"Extremo": "Extreme", "Alto": "High", "Moderado": "Moderate", "Baixo": "Low"},
        "probabilidades": ["Unlikely", "Possible", "Likely", "Almost Certain"],
        "impactos": ["Low", "Moderate", "High", "Catastrophic"],
        "eixo_x": "IMPACT",
        "eixo_y": "LIKELIHOOD",
        "ids": "IDs: ",
        "titulo_mapa": "MaisPlace (Group G3) — Risk Heat Map: Original vs. Residual ({n} Risks)",
        "painel_original": "Original Risk (Legacy Environment)",
        "painel_residual": "Residual Risk (Implemented AWS Environment)",
        "eixo_quantidade": "Number of Risks (Total = {n})",
        "titulo_grafico": "MaisPlace (Group G3) — Cyber Risk Reduction: Before vs. After",
        "legenda_original": "Original Risk (Legacy)",
        "legenda_residual": "Residual: {c}",
        "quadro": ("Impact of Migration + Controls:\n"
                   "• Extreme: {e0} → {e1} ({ve})\n"
                   "• Extreme + High: {a0} → {a1} ({va})\n"
                   "• Moderate: {m0} → {m1} (lower criticality)\n"
                   "• {fora} of the remaining {a1} are organizational\nor outside the lab scope"),
        "decimal": ".",
    },
}
T = TEXTOS["pt"]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def nome(c):
    return T["classes"][c]


def classe(nota):
    """Mesma regra das colunas J e S da planilha."""
    if nota > 9:
        return "Extremo"
    if nota >= 7:
        return "Alto"
    if nota >= 3:
        return "Moderado"
    return "Baixo"


def ler_riscos():
    aba = load_workbook(MATRIZ, data_only=False).worksheets[2]
    riscos = []
    linha = PRIMEIRA_LINHA
    while aba.cell(linha, 3).value and aba.cell(linha, 4).value:
        valores = [aba.cell(linha, coluna).value for coluna in (7, 8, 16, 17)]
        if not all(isinstance(v, (int, float)) for v in valores):
            raise SystemExit(f"Linha {linha} da matriz sem probabilidade ou impacto numérico.")
        riscos.append({
            "id": linha - PRIMEIRA_LINHA + 1,
            "original": (int(valores[0]), int(valores[1])),
            "residual": (int(valores[2]), int(valores[3])),
            "status": str(aba.cell(linha, 15).value or "").strip(),
        })
        linha += 1
    return riscos


def contar(riscos, momento):
    total = {c: 0 for c in CLASSES}
    for r in riscos:
        p, i = r[momento]
        total[classe(p * i)] += 1
    return total


def pct(antes, depois):
    """Variação percentual com o separador decimal do idioma e sinal de menos tipográfico."""
    if not antes:
        return f"0{T['decimal']}0%"
    valor = (depois - antes) / antes * 100
    return f"{'−' if valor < 0 else '+'}{abs(valor):.1f}%".replace(".", T["decimal"])


def lista_ids(ids):
    if len(ids) <= 5:
        return T["ids"] + ", ".join(map(str, ids))
    meio = len(ids) // 2
    return T["ids"] + ", ".join(map(str, ids[:meio])) + "\n" + ", ".join(map(str, ids[meio:]))


def painel(ax, riscos, momento, titulo):
    total = contar(riscos, momento)
    for p in range(1, 5):
        for i in range(1, 5):
            nome_classe = classe(p * i)
            ids = [r["id"] for r in riscos if r[momento] == (p, i)]
            claro = nome_classe in ("Extremo", "Alto")
            ax.add_patch(Rectangle((i - 1 + 0.012, p - 1 + 0.02), 0.976, 0.96, color=CORES[nome_classe], lw=0))
            ax.text(i - 0.07, p - 0.1, f"({p * i})", ha="right", va="top", fontsize=7, fontweight="bold",
                    color="white" if claro else "#334155", alpha=0.9)
            if ids:
                ax.text(i - 0.5, p - 0.4, str(len(ids)), ha="center", va="center", fontsize=20,
                        fontweight="bold", color="white" if claro else ESCURO)
                ax.text(i - 0.5, p - 0.78, lista_ids(ids), ha="center", va="center", fontsize=7,
                        color="white" if claro else ESCURO, linespacing=1.15)
            else:
                ax.text(i - 0.5, p - 0.5, "0", ha="center", va="center", fontsize=12,
                        color="white" if nome_classe != "Moderado" else "#713f12", alpha=0.45)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_xticks([x + 0.5 for x in range(4)])
    ax.set_xticklabels([f"{rotulo}\n({n})" for n, rotulo in enumerate(T["impactos"], 1)], fontsize=9,
                       fontweight="bold")
    ax.set_yticks([y + 0.5 for y in range(4)])
    ax.set_yticklabels([f"{rotulo}\n({n})" for n, rotulo in enumerate(T["probabilidades"], 1)], fontsize=9,
                       fontweight="bold")
    ax.tick_params(length=0, colors="#1e293b")
    ax.set_xlabel(T["eixo_x"], fontsize=10, fontweight="bold", color=ESCURO, labelpad=8)
    ax.set_ylabel(T["eixo_y"], fontsize=10, fontweight="bold", color=ESCURO, labelpad=8)
    for borda in ax.spines.values():
        borda.set_visible(False)
    resumo = "  |  ".join(f"{nome(c)}: {total[c]}" for c in CLASSES)
    ax.set_title(f"{titulo}\n{resumo}", fontsize=11, fontweight="bold", color=ESCURO, pad=10)


def mapa_de_calor(riscos, pasta):
    fig, eixos = plt.subplots(1, 2, figsize=(13.5, 5.8), dpi=300)
    fig.suptitle(T["titulo_mapa"].format(n=len(riscos)), fontsize=13, fontweight="bold", color=ESCURO, y=0.975)
    painel(eixos[0], riscos, "original", T["painel_original"])
    painel(eixos[1], riscos, "residual", T["painel_residual"])
    fig.legend(handles=[Patch(color=CORES[c], label=f"{nome(c)} ({FAIXAS[c]})") for c in CLASSES],
               loc="lower center", ncol=4, frameon=False, fontsize=9, bbox_to_anchor=(0.5, 0.005))
    fig.subplots_adjust(left=0.1, right=0.985, top=0.77, bottom=0.2, wspace=0.26)
    destino = pasta / T["arquivo_01"]
    fig.savefig(destino, dpi=300, facecolor="white")
    plt.close(fig)
    return destino


def grafico_antes_depois(riscos, pasta):
    original, residual = contar(riscos, "original"), contar(riscos, "residual")
    altos_antes = original["Extremo"] + original["Alto"]
    altos_depois = residual["Extremo"] + residual["Alto"]
    fora = sum(1 for r in riscos
               if classe(r["residual"][0] * r["residual"][1]) in ("Extremo", "Alto")
               and r["status"] in FORA_DO_LABORATORIO)

    fig, ax = plt.subplots(figsize=(9.8, 5.4), dpi=300)
    largura = 0.34
    cores_residual = {**CORES, "Moderado": "#eab308"}
    for n, c in enumerate(CLASSES):
        ax.bar(n - largura / 2, original[c], largura, color="#94a3b8", edgecolor="#475569", linewidth=1)
        ax.bar(n + largura / 2, residual[c], largura, color=cores_residual[c], edgecolor="#1e293b", linewidth=1)
        ax.text(n - largura / 2, original[c] + 0.35, str(original[c]), ha="center", va="bottom", fontsize=11,
                fontweight="bold", color="#475569")
        ax.text(n + largura / 2, residual[c] + 0.35, str(residual[c]), ha="center", va="bottom", fontsize=12,
                fontweight="bold", color=ESCURO)

    ax.set_xticks(range(4))
    ax.set_xticklabels([f"{nome(c)}\n({FAIXAS[c]})" for c in CLASSES], fontsize=11, fontweight="bold",
                       color="#1e293b")
    ax.set_ylabel(T["eixo_quantidade"].format(n=len(riscos)), fontsize=11, fontweight="bold", color=ESCURO)
    ax.set_ylim(0, max(max(original.values()), max(residual.values())) + 3.5)
    ax.yaxis.grid(True, linestyle="--", color="#cbd5e1", alpha=0.8)
    ax.set_axisbelow(True)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.set_title(T["titulo_grafico"], fontsize=13, fontweight="bold", color=ESCURO, pad=34)
    ax.legend(handles=[Patch(facecolor="#94a3b8", edgecolor="#475569", label=T["legenda_original"])]
              + [Patch(facecolor=cores_residual[c], edgecolor="#1e293b",
                       label=T["legenda_residual"].format(c=nome(c)))
                 for c in CLASSES[:3]],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=4, frameon=False, fontsize=9.5)

    variacao = pct(original["Extremo"], residual["Extremo"])
    ax.annotate(f"{variacao}\n({original['Extremo']} → {residual['Extremo']})",
                xy=(largura / 2, residual["Extremo"] + 1.25), xytext=(largura / 2, 10.6),
                ha="center", va="center", fontsize=10, fontweight="bold", color="#991b1b",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#fef2f2", edgecolor="#dc2626", linewidth=1.5),
                arrowprops=dict(arrowstyle="->", color="#dc2626", linewidth=1.8))
    ax.text(0.772, 0.805,
            T["quadro"].format(e0=original["Extremo"], e1=residual["Extremo"], ve=variacao,
                               a0=altos_antes, a1=altos_depois, va=pct(altos_antes, altos_depois),
                               m0=original["Moderado"], m1=residual["Moderado"], fora=fora),
            transform=ax.transAxes, ha="center", va="center", fontsize=9, color="#1e293b", linespacing=1.45,
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#eff6ff", edgecolor="#2563eb", linewidth=1.5))
    fig.subplots_adjust(left=0.075, right=0.985, top=0.87, bottom=0.11)
    destino = pasta / T["arquivo_02"]
    fig.savefig(destino, dpi=300, facecolor="white")
    plt.close(fig)
    return destino


def main():
    global T
    parser = argparse.ArgumentParser(description="Gera o mapa de calor e o gráfico de riscos a partir da matriz.")
    parser.add_argument("--lang", choices=sorted(TEXTOS), default="pt", help="idioma das figuras (padrão: pt)")
    T = TEXTOS[parser.parse_args().lang]
    pasta = ROOT / T["pasta"]
    pasta.mkdir(parents=True, exist_ok=True)

    riscos = ler_riscos()
    original, residual = contar(riscos, "original"), contar(riscos, "residual")
    print(f"{MATRIZ.name}: {len(riscos)} riscos")
    print("  original:", ", ".join(f"{c} {original[c]}" for c in CLASSES))
    print("  residual:", ", ".join(f"{c} {residual[c]}" for c in CLASSES))
    for destino in (mapa_de_calor(riscos, pasta), grafico_antes_depois(riscos, pasta)):
        print("  gravado:", destino.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
