#!/usr/bin/env python3
"""Gera a apresentação editável da avaliação final G3 (12 slides).

Uso:  python gerar_apresentacao.py [--lang pt|en]   (requer python-pptx e Pillow)

  --lang pt (padrão): grava Apresentacao_Final_G3.pptx
  --lang en:          grava Final_Presentation_G3_EN.pptx, com os textos de
                      textos_en.py e as figuras de figuras/en/

Prints novos: salve o arquivo em `evidencias_novas/` com o nome indicado em
SLOTS e rode o script de novo. Enquanto o arquivo não existir, o slide usa o
print anterior (quando há um) ou mostra um quadro tracejado "PRINT PENDENTE".

Os recortes em `evidencias_slides/` vêm dos prints originais (ver ORIGEM.md
nessa pasta); neles o ID da conta AWS e as chaves de acesso foram removidos.
"""

import argparse
import re
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description="Gera a apresentação final (12 slides).")
parser.add_argument("--lang", choices=("pt", "en"), default="pt", help="idioma dos slides (padrão: pt)")
LANG = parser.parse_args().lang
OUT = ROOT / ("Final_Presentation_G3_EN.pptx" if LANG == "en" else "Apresentacao_Final_G3.pptx")
# figuras com texto: versão em português em figuras/, versão em inglês em figuras/en/
FIG = {
    "pt": {"mapa": "figuras/01_mapa_calor_original_vs_residual.png",
           "grafico": "figuras/02_grafico_riscos_antes_x_depois.png",
           "diagrama": "figuras/03_diagrama_arquitetura_aws.png"},
    "en": {"mapa": "figuras/en/01_risk_heatmap_original_vs_residual.png",
           "grafico": "figuras/en/02_risk_chart_before_after.png",
           "diagrama": "figuras/en/03_architecture_diagram_aws.png"},
}[LANG]
NOVAS = "evidencias_novas"

# --- Estado da entrega: ajustar aqui quando mudar ---------------------------
VPN_IMPLANTADA = True

# slot: (arquivo esperado em evidencias_novas/, print anterior ou None, o que capturar)
SLOTS = {
    "wazuh_agentes": ("wazuh_agentes.png", None,
                      "Wazuh: 3 agentes ativos e alertas recentes"),
    "zabbix_hosts": ("zabbix_hosts.png", "evidencias_slides/zabbix_hosts_2026-11-10.png",
                     "Zabbix: 4 hosts disponíveis"),
    "waf_eventos": ("waf_eventos.png", "evidencias_aws/00_waf_rate_limit_wp_admin.png",
                    "Cloudflare: eventos do WAF com requisições bloqueadas"),
    "fail2ban_ban": ("fail2ban_ban.png", None,
                     "Fail2ban: IP banido (log + regra na Cloudflare)"),
    "guacamole_totp": ("guacamole_totp.png", None,
                       "Guacamole: login pedindo o código TOTP"),
    "vpn_tunel": ("vpn_tunel.png", None,
                  "VPN: túnel OpenVPN ativo e SG só com UDP 1194"),
    "scan_final": ("scan_final.png", "../external-scan/scan_2026-11-18/zap_resumo.png",
                   "Resumo do scan final, depois das correções"),
}

FONT = "Calibri"
NAVY = RGBColor(13, 28, 50)
BLUE = RGBColor(31, 92, 153)
CYAN = RGBColor(43, 183, 196)
PALE = RGBColor(232, 243, 248)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(87, 101, 116)
LINE = RGBColor(196, 208, 219)
ORANGE = RGBColor(196, 106, 18)

LEFT, WIDTH = 0.56, 12.2  # margem esquerda e largura útil, em polegadas

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
pendentes = []
sem_traducao = []
if LANG == "en":
    from textos_en import EN
else:
    EN = {}


def tr(texto):
    """Devolve o texto no idioma escolhido. Em pt, o próprio texto; em en, a tradução de textos_en.py.
    Números passam sem tradução (só a vírgula decimal vira ponto) e caminhos de arquivo ficam iguais."""
    if LANG == "pt" or re.fullmatch(r"[\w./-]+\.png", texto):
        return texto
    if not re.search(r"[A-Za-zÀ-ú]", texto):
        return re.sub(r"(\d),(\d)", r"\1.\2", texto)  # 87,5% -> 87.5%
    if texto not in EN:
        sem_traducao.append(texto)
        return texto
    return EN[texto]


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def box(slide, x, y, w, h, fill=WHITE, line=None, dash=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.shadow.inherit = False
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(1)
        if dash:
            shape.line.dash_style = MSO_LINE.DASH
    return shape


def txt(slide, text, x, y, w, h, size=16, color=NAVY, bold=False, align=None,
        anchor=MSO_ANCHOR.TOP, spacing=0):
    """`text`: string, ou lista de parágrafos; cada parágrafo pode ser uma lista
    de trechos (texto, negrito) ou (texto, negrito, cor)."""
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = anchor
    paragraphs = text if isinstance(text, list) else [text]
    for i, para in enumerate(paragraphs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        runs = para if isinstance(para, list) else [(para, bold)]
        for run in runs:
            r = p.add_run()
            r.text = tr(run[0])
            r.font.name = FONT
            r.font.size = Pt(size)
            r.font.bold = run[1]
            r.font.color.rgb = run[2] if len(run) > 2 else color
        if align:
            p.alignment = align
        if i and spacing:
            p.space_before = Pt(spacing)
    return shape


def base(title, source, notes):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    box(slide, 0, 0, 13.333, 0.16, CYAN)
    txt(slide, title, LEFT, 0.3, WIDTH, 0.7, 26, NAVY, True, anchor=MSO_ANCHOR.MIDDLE)
    box(slide, LEFT, 1.06, WIDTH, 0.025, PALE)
    txt(slide, source, LEFT, 7.04, 11.4, 0.26, 10, GRAY)
    txt(slide, f"{len(prs.slides):02d}", 12.3, 7.04, 0.46, 0.26, 10, GRAY, align=PP_ALIGN.RIGHT)
    slide.notes_slide.notes_text_frame.text = tr(notes)
    return slide


def card(slide, heading, body, x, y, w, h, accent=BLUE, heading_size=16, body_size=14, spacing=5):
    box(slide, x, y, w, h, PALE)
    box(slide, x, y, 0.07, h, accent)
    txt(slide, heading, x + 0.22, y + 0.12, w - 0.4, 0.4, heading_size, BLUE, True, anchor=MSO_ANCHOR.MIDDLE)
    txt(slide, body, x + 0.22, y + 0.58, w - 0.4, h - 0.68, body_size, NAVY, spacing=spacing)


def bullets(slide, lines, x, y, w, size=15, gap=0.62):
    for i, line in enumerate(lines):
        box(slide, x, y + i * gap + 0.11, 0.1, 0.1, CYAN)
        txt(slide, line, x + 0.26, y + i * gap, w - 0.26, gap - 0.04, size)


def img(slide, path, x, y, w, h, halign="center", valign="top", border=True):
    """Encaixa a imagem na área (x, y, w, h) sem distorcer. Devolve (x, y, w, h) reais."""
    path = ROOT / path
    if not path.exists():
        raise FileNotFoundError(path)
    with Image.open(path) as im:
        iw, ih = im.size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    px = x + {"left": 0, "center": (w - pw) / 2, "right": w - pw}[halign]
    py = y + {"top": 0, "middle": (h - ph) / 2}[valign]
    pic = slide.shapes.add_picture(str(path), Inches(px), Inches(py), width=Inches(pw), height=Inches(ph))
    if border:
        pic.line.color.rgb = LINE
        pic.line.width = Pt(0.75)
    return px, py, pw, ph


def caption(slide, lead, rest, x, y, w, h=0.5, size=11):
    txt(slide, [[(lead, True, NAVY), (rest, False, GRAY)]], x, y, w, h, size, GRAY)


def evid(slide, source, lead, rest, x, y, w, h, halign="left", cap_h=0.5):
    """Coloca um print com legenda. `source` é um caminho ou o nome de um slot."""
    path = source
    if source in SLOTS:
        novo, anterior, descricao = SLOTS[source]
        path = f"{NOVAS}/{novo}" if (ROOT / NOVAS / novo).exists() else anterior
        if path != f"{NOVAS}/{novo}":
            pendentes.append(f"{NOVAS}/{novo}  ->  {descricao}"
                             + ("" if anterior is None else f"  (hoje usa {anterior})"))
        if path is None:
            box(slide, x, y, w, h, WHITE, ORANGE, dash=True)
            txt(slide, [[("PRINT PENDENTE", True, ORANGE)], descricao, [(f"{NOVAS}/{novo}", False, GRAY)]],
                x + 0.1, y, w - 0.2, h, 11, NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=2)
            caption(slide, lead, rest, x, y + h + 0.04, w, cap_h)
            return y + h
    px, py, pw, ph = img(slide, path, x, y, w, h, halign)
    caption(slide, lead, rest, x, py + ph + 0.04, w, cap_h)
    return py + ph


# 1 — introdução
s = base("MaisPlace: migração segura do e-commerce para a AWS",
         "Fonte: Estudo de caso MaisPlace 2026-2, seções 1 a 5",
         "A MaisPlace depende da loja online para vender e processar pedidos. O estudo de caso traz três "
         "incidentes que explicam a migração: a loja fora do ar por cerca de duas horas em uma campanha, sem "
         "causa identificada; o uso de uma conta administrativa de madrugada, sem autor e com poucos logs; e "
         "uma atualização que afetou pedidos e foi corrigida direto em produção. A diretoria discutiu se, na "
         "AWS, a segurança deixaria de ser responsabilidade da empresa. Não deixa: a AWS responde pelo "
         "datacenter, pelo hardware e pela virtualização; conta administrativa roubada, aplicação explorada e "
         "dados de clientes continuam com a MaisPlace. Por isso a análise de riscos veio antes da migração. "
         "Nosso objetivo foi reconstruir a loja na AWS com um controle para cada risco alto, mostrar a "
         "evidência de que funciona e dizer o que ainda falta.")
txt(s, "Avaliação final · Cibersegurança em Nuvem · Prof. Dr. Rodolfo Avelino", LEFT, 1.25, WIDTH, 0.36, 16, BLUE, True)
txt(s, "Grupo 3 · Eduardo · Gustavo · Henrique · Lucas · Sidney", LEFT, 1.62, WIDTH, 0.36, 16, GRAY)
txt(s, "Três incidentes motivaram a migração", LEFT, 2.2, WIDTH, 0.4, 18, NAVY, True)
card(s, "Indisponibilidade", "Loja fora do ar por cerca de duas horas durante campanha promocional. A causa não foi determinada.",
     0.56, 2.68, 3.92, 1.62, body_size=14)
card(s, "Conta administrativa", "Conta privilegiada usada de madrugada, sem autor identificado e com poucos logs para investigar.",
     4.70, 2.68, 3.92, 1.62, body_size=14)
card(s, "Mudança em produção", "Atualização prejudicou pedidos e foi corrigida direto em produção, em horário comercial.",
     8.84, 2.68, 3.92, 1.62, body_size=14)
# pergunta da diretoria (seção 5 do estudo de caso; risco 21 da matriz)
box(s, LEFT, 4.5, WIDTH, 1.0, PALE)
box(s, LEFT, 4.5, 0.07, 1.0, ORANGE)
txt(s, [[("Responsabilidade compartilhada  ", True, ORANGE),
         ("A AWS protege datacenter, hardware e virtualização. Contas, sistema operacional, aplicação, dados e "
          "regras de rede continuam com a MaisPlace: migrar não transfere esses riscos.", False, NAVY)]],
    LEFT + 0.3, 4.5, WIDTH - 0.6, 1.0, 15, NAVY, anchor=MSO_ANCHOR.MIDDLE)
box(s, LEFT, 5.7, WIDTH, 1.1, NAVY)
txt(s, [[("Objetivo  ", True, CYAN),
         ("Reconstruir a loja na AWS com um controle para cada risco alto da matriz, evidência de que cada "
          "controle funciona e registro claro dos riscos que permanecem.", False, WHITE)]],
    LEFT + 0.3, 5.7, WIDTH - 0.6, 1.1, 17, WHITE, anchor=MSO_ANCHOR.MIDDLE)

# 2 — ameaças
s = base("Seis ameaças e o que cada uma custa ao negócio",
         "Fontes: Estudo de caso MaisPlace 2026-2, seções 4, 7 e 8; matriz v2.2 (riscos 18, 20, 21 e 23)",
         "Partimos das seis classes de ameaça do estudo de caso: insider, malware, negação de serviço, ataques "
         "à aplicação web, comprometimento de credenciais e comprometimento de informações. Para cada uma "
         "mostramos como ela aparece na MaisPlace e o que custa ao negócio: venda perdida, perda de "
         "rastreabilidade, exposição de dados de clientes. Revisamos o levantamento, como o caso pede: as seis "
         "continuam relevantes e acrescentamos ameaças que ganham peso na nuvem, como erro de configuração, "
         "leitura errada da responsabilidade compartilhada, cadeia de suprimentos de plugins e phishing. No "
         "total, a matriz tem 25 riscos.")
ameacas = [
    ("insider", "Insider", "Conta administrativa compartilhada, usada de madrugada sem autor identificado.",
     "ações sem responsável"),
    ("malware", "Malware e ransomware", "Sem gestão de vulnerabilidades e com backup nunca restaurado em teste.",
     "parada prolongada da loja"),
    ("dos", "Negação de serviço", "Loja fora do ar por cerca de duas horas em plena campanha promocional.",
     "vendas perdidas"),
    ("web", "Ataques à aplicação web", "Plugins do WooCommerce sem rotina de atualização; injeção de SQL.",
     "pedidos e cadastro expostos"),
    ("credenciais", "Comprometimento de credenciais", "Acesso administrativo sem MFA e credenciais guardadas em arquivos.",
     "controle da loja por terceiros"),
    ("informacoes", "Comprometimento de informações", "Dados pessoais de clientes em banco pouco isolado da aplicação.",
     "LGPD e reputação"),
]
for i, (icone, nome, como, impacto) in enumerate(ameacas):
    x, y = LEFT + (i % 3) * 4.14, 1.25 + (i // 3) * 2.45
    box(s, x, y, 3.92, 2.28, PALE)
    img(s, f"figuras/icones/{icone}.png", x + 0.25, y + 0.2, 0.62, 0.62, border=False)
    txt(s, nome, x + 1.02, y + 0.16, 2.75, 0.7, 17, BLUE, True, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, como, x + 0.25, y + 0.96, 3.45, 0.8, 14)
    txt(s, [[("Impacto: ", True, ORANGE), (impacto, True, NAVY)]], x + 0.25, y + 1.78, 3.45, 0.4, 14)
# seção 7 do estudo de caso: ameaças não consideradas e as que pesam mais na nuvem
txt(s, [[("Além das seis: ", True, BLUE),
         ("a matriz inclui ameaças que ganham peso na nuvem, como erro de configuração, leitura errada da "
          "responsabilidade compartilhada, cadeia de suprimentos (plugins) e phishing. São 25 riscos, cada um "
          "com probabilidade, impacto e controle.", False, NAVY)]],
    LEFT, 6.3, WIDTH, 0.66, 14, NAVY, anchor=MSO_ANCHOR.MIDDLE)

# 3 — vulnerabilidades
s = base("Vulnerabilidades do legado e CVEs encontradas pelo Wazuh",
         "Fontes: Estudo de caso, seção 8; Relatório do Roteiro 1 (print 17, Wazuh Vulnerability Detection)",
         "O ambiente anterior tinha contas compartilhadas sem MFA, administração remota sem padrão, rede pouco "
         "segmentada, nenhuma gestão de vulnerabilidades, logs dispersos e backup sem teste. No Roteiro 1 "
         "ligamos a detecção de vulnerabilidades do Wazuh nos dois servidores e ela mostrou 403 CVEs críticas e "
         "1.562 altas, concentradas no pacote linux-aws, o kernel do Ubuntu. Esse é o retrato inicial: sem "
         "rotina de atualização, a exposição se acumula.")
txt(s, "Fragilidades do ambiente anterior", LEFT, 1.3, 4.9, 0.4, 17, BLUE, True)
bullets(s, [
    "Contas compartilhadas e privilegiadas, sem MFA",
    "Administração remota sem padrão; credenciais em arquivos",
    "Rede pouco segmentada entre aplicação e banco",
    "Sem gestão de vulnerabilidades (plugins e sistema)",
    "Logs dispersos; monitoramento só de disponibilidade",
    "Backup sem teste de restauração",
], LEFT, 1.9, 4.9, 16, 0.78)
fundo = evid(s, "evidencias_slides/wazuh_cves_roteiro1.png", "Wazuh Vulnerability Detection (Roteiro 1). ",
             "CVEs por severidade em web-server e db-server.", 5.76, 1.3, 7.0, 2.3)
card(s, "O que o print mostra",
     "403 CVEs críticas e 1.562 altas nos dois servidores, concentradas no pacote linux-aws (kernel do Ubuntu). "
     "É o retrato inicial: sem rotina de atualização, a exposição se acumula.",
     5.76, fundo + 0.6, 7.0, 2.2, accent=ORANGE, body_size=16)

# 4 — matriz
s = base("Matriz de risco: 25 cenários, de 8 extremos para 1",
         "Fonte: Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.xlsx (v2.2, revisão de 19/11/2026)",
         "A matriz avalia 25 riscos por probabilidade e impacto, em escala de 1 a 4. Na classificação original, "
         "do ambiente legado, 8 são extremos e 14 altos. Depois dos controles implementados, resta 1 extremo e "
         "ficam 14 altos. O último a cair foi o de ataques web a plugins, depois do WordPress atualizado e do "
         "scan final sem alertas altos. Cada linha traz o controle CIS v8, o que foi implementado e a "
         "evidência. As notas residuais são avaliação do grupo.")
img(s, FIG["mapa"], LEFT, 1.25, 8.6, 5.5, valign="middle", border=False)
card(s, "Original (legado)", "8 extremos · 14 altos · 3 moderados", 9.4, 1.5, 3.36, 1.3, body_size=15)
card(s, "Residual (AWS)", "1 extremo · 14 altos · 10 moderados", 9.4, 3.0, 3.36, 1.3, accent=CYAN, body_size=15)
card(s, "Como ler", "Probabilidade × impacto, de 1 a 4. Cada risco tem controle CIS v8, implementação e evidência.",
     9.4, 4.5, 3.36, 1.9, accent=GRAY, body_size=14)

# 5 — antes x depois
s = base("Riscos altos e mitigação: antes × depois",
         "Fonte: docs/risk-traceability.pt-BR.md, seções 2 e 3; notas da matriz v2.2",
         "Este quadro resume o que mudou em cinco frentes. O perímetro ganhou Cloudflare com WAF e Fail2ban. O "
         "banco foi para sub-rede privada. O acesso administrativo passou a exigir o Guacamole com TOTP, e o "
         "WordPress tem MFA. Os logs chegam ao Wazuh, ao Zabbix, ao CloudWatch e ao CloudTrail. Os backups são "
         "diários e a restauração do banco foi testada. A coluna de risco mostra a nota de um risco "
         "representativo antes e depois.")
colunas = [("Frente", 1.85), ("Antes (legado)", 2.85), ("Depois (AWS, Grupo 3)", 3.75), ("Risco", 1.2),
           ("Impacto no negócio", 2.55)]
linhas = [
    ("Perímetro e aplicação", "Servidor exposto direto à internet, sem WAF.",
     "Cloudflare como proxy e WAF (5 regras), Fail2ban e origem oculta.", "ID 4\n16 → 8",
     "Loja protegida contra ataques web e DoS em campanha."),
    ("Dados (LGPD)", "Aplicação e banco na mesma rede, com poucas restrições.",
     "MySQL em sub-rede privada, sem IP público; porta 3306 só do webserver.", "ID 6\n12 → 8",
     "Menor chance de vazamento da base de clientes."),
    ("Acesso administrativo", "Contas compartilhadas, sem MFA e sem padrão de acesso remoto.",
     "SSH público fechado; Guacamole com TOTP e allowlist; IAM nominal; MFA no WordPress.", "ID 1\n16 → 8",
     "Cada ação tem autor; força bruta não alcança os servidores."),
    ("Visibilidade", "Logs dispersos; monitoramento só de “ligado ou não”.",
     "Wazuh (3 agentes), Zabbix (4 hosts), CloudWatch/SNS e CloudTrail.", "ID 16\n12 → 6",
     "Incidente investigável: efeito e causa do caso db-01."),
    ("Continuidade", "Backup sem teste de restauração.",
     "Snapshots diários (DLM, 7 dias) e dump do MySQL com restauração testada.", "ID 15\n8 → 4",
     "Recuperação da loja comprovada, não presumida."),
]
x = LEFT
for nome, largura in colunas:
    box(s, x, 1.3, largura, 0.42, NAVY)
    txt(s, nome, x + 0.08, 1.3, largura - 0.16, 0.42, 13, WHITE, True, anchor=MSO_ANCHOR.MIDDLE)
    x += largura
for i, linha in enumerate(linhas):
    y = 1.72 + i * 0.92
    box(s, LEFT, y, WIDTH, 0.92, PALE if i % 2 == 0 else WHITE, LINE)
    x = LEFT
    for j, (valor, (_, largura)) in enumerate(zip(linha, colunas)):
        txt(s, valor, x + 0.08, y, largura - 0.16, 0.92, 13, BLUE if j == 0 else NAVY, j in (0, 3),
            anchor=MSO_ANCHOR.MIDDLE)
        x += largura
txt(s, "Nota de risco = probabilidade × impacto (1 a 16). A rastreabilidade completa dos riscos altos está no "
       "documento de rastreabilidade.", LEFT, 6.42, WIDTH, 0.4, 12, GRAY)

# 6 — arquitetura
s = base("Arquitetura na AWS: só os fluxos necessários",
         "Fonte: docs/architecture.pt-BR.md e diagrama do grupo (figuras/03_diagrama_arquitetura_aws)",
         "A Cloudflare recebe o tráfego da loja e só ela alcança o webserver nas portas 80 e 443. O webserver "
         "fala com o banco, que fica em sub-rede privada e sem IP público, apenas na 3306. A administração entra "
         "pelo jump server com Guacamole. Wazuh e Zabbix ficam na instância de monitoramento. Os Security Groups "
         "se referenciam por função, então cada servidor só aceita o que precisa.")
img(s, FIG["diagrama"], LEFT, 1.2, WIDTH, 5.7, border=False)

# 7 — evidências: rede, WAF e acesso
s = base("Evidências: rede, WAF e acesso administrativo",
         "Fontes: evidencias_aws (capturas de 18/11/2026) e evidencias_novas",
         "Os Security Groups mostram o menor privilégio de rede: o webserver só recebe 80 e 443 da lista de "
         "prefixos da Cloudflare e SSH só do Guacamole; o banco só recebe 3306 do webserver. O WAF bloqueou "
         "nosso teste de excesso de requisições em /wp-admin com o erro 1015. O acesso administrativo passa "
         "pelo Guacamole com TOTP e allowlist de IP."
         + ("" if VPN_IMPLANTADA else " A VPN OpenVPN pedida na avaliação ainda não foi implantada."))
fundo = evid(s, "evidencias_aws/01_sg_webserver.png", "SG do webserver. ",
             "80/443 só da lista de prefixos da Cloudflare; 22 só do SG do Guacamole; 10050 só do Zabbix (18/11/2026).",
             LEFT, 1.25, 5.95, 1.75)
evid(s, "evidencias_aws/02_sg_dbserver.png", "SG do banco. ",
     "3306 só do SG do webserver; nenhuma regra aberta para a internet (18/11/2026).",
     LEFT, fundo + 0.55, 5.95, 1.85)
evid(s, "waf_eventos", "WAF. ", "Rate limit em /wp-admin: erro 1015 da Cloudflare (18/11/2026).",
     6.8, 1.25, 2.87, 1.62)
evid(s, "fail2ban_ban", "Fail2ban. ", "5 falhas de login geram bloqueio de 1 hora na Cloudflare.",
     9.88, 1.25, 2.87, 1.62)
evid(s, "guacamole_totp", "Guacamole. ", "Jump server com TOTP obrigatório e allowlist de IP.",
     6.8, 3.6, 2.87, 1.62)
evid(s, "vpn_tunel", "VPN. ", "OpenVPN com apenas UDP 1194 aberta." if VPN_IMPLANTADA
     else "Ainda não implantada; requisito em aberto.", 9.88, 3.6, 2.87, 1.62)
box(s, LEFT, 6.2, WIDTH, 0.62, PALE)
txt(s, "SSH fechado para a internet; administração só pelo Guacamole (TOTP e allowlist)"
       + (", por dentro da VPN." if VPN_IMPLANTADA else ". VPN OpenVPN ainda não implantada."),
    LEFT + 0.2, 6.2, WIDTH - 0.4, 0.62, 14, NAVY, True, anchor=MSO_ANCHOR.MIDDLE)

# 8 — evidências: monitoramento e incidente
s = base("Evidências: monitoramento mostrou efeito e causa no db-01",
         "Fontes: Relatório do Roteiro 4 (capturas de 06 e 10/11/2026), Roteiro 3 e evidencias_novas",
         "O caso do db-01 mostrou a diferença entre a instância estar ligada e a loja funcionar. O status check "
         "da AWS continuou normal enquanto o MySQL travou e a loja deu erro de banco. O Zabbix registrou o "
         "efeito, com indisponibilidade e métricas congeladas, e o Wazuh guardou os eventos do servidor que "
         "ajudaram a chegar à causa. O alerta por e-mail do Zabbix foi testado. Por isso monitoramos serviço e "
         "aplicação, além da instância.")
fundo = evid(s, "zabbix_hosts", "Zabbix. ", "4 hosts monitorados e disponíveis: db-01, jump-01, web-01 e o próprio servidor.",
             LEFT, 1.25, 5.95, 0.9, cap_h=0.3)
fundo = evid(s, "evidencias_slides/zabbix_email_2026-11-10.png", "Alerta por e-mail. ",
             "Problema de CPU e resolução notificados pelo Zabbix (10/11/2026).", LEFT, fundo + 0.48, 5.95, 0.65, cap_h=0.3)
evid(s, "wazuh_agentes", "Wazuh. ", "Agentes do web-01, db-01 e jump-01 ativos; FIM, SCA e detecção de vulnerabilidades.",
     LEFT, fundo + 0.48, 5.95, 1.7, cap_h=0.3)
fundo = evid(s, "evidencias_slides/wazuh_eventos_db01_2026-11-06.png", "Wazuh, incidente do db-01. ",
             "Eventos do db-server na madrugada de 06/11/2026, até o agente desconectar.", 6.8, 1.25, 5.95, 2.33, cap_h=0.3)
card(s, "O que o incidente ensinou",
     "O status check da EC2 seguiu “ok” com o MySQL travado e a loja fora do ar. O Zabbix mostrou o efeito; "
     "o Wazuh, os eventos que levaram à causa.", 6.8, fundo + 0.48, 5.95, 1.55, accent=ORANGE, body_size=14)
box(s, LEFT, 6.2, WIDTH, 0.62, PALE)
txt(s, "Também ativos: CloudWatch com 4 alarmes e SNS para os 5 integrantes; Fail2ban integrado à Cloudflare; "
       "WAF com 5 regras.", LEFT + 0.2, 6.2, WIDTH - 0.4, 0.62, 14, NAVY, True, anchor=MSO_ANCHOR.MIDDLE)

# 9 — scan externo
s = base("Scan externo: nenhum alerta alto na superfície pública",
         "Fonte: external-scan/report-2026-11-19.pt-BR.md (scan final) e report-2026-11-18.pt-BR.md; "
         "OWASP ZAP Baseline 2.17.0",
         "Antes do scan final atualizamos o WordPress para a 7.1.5, aplicamos os pacotes de segurança nos dois "
         "servidores e reiniciamos o servidor web para ativar o kernel corrigido. Depois rodamos de novo o "
         "OWASP ZAP em modo baseline contra a loja, de fora. O relatório registrou zero alertas altos, sete "
         "médios, dez baixos e dez informativos; o alerta de clickjacking sumiu com os novos cabeçalhos. O "
         "scan é passivo, sem login e passa pela Cloudflare, então não cobre rotas autenticadas nem o servidor "
         "de origem; por dentro, conferimos versões e integridade dos arquivos. Os médios que restam são a "
         "falta de CSP, avisos automáticos de token anti-CSRF e a biblioteca moment.js do próprio WordPress.")
evid(s, "scan_final", "OWASP ZAP Baseline. ",
     "Resumo do relatório gerado em 19/11/2026 04:35 UTC para https://maisplace.net.br, depois das correções.",
     LEFT, 1.3, 7.6, 5.0, cap_h=0.3)
card(s, "Resultado", "0 altos · 7 médios · 10 baixos · 10 informativos. Em 18/11 eram 8 médios.",
     8.4, 1.3, 4.36, 1.5, accent=CYAN, body_size=15)
card(s, "Limite", "Scan passivo, sem login e através da Cloudflare. Não cobre rotas autenticadas nem o servidor de origem.",
     8.4, 3.0, 4.36, 1.6, accent=ORANGE, body_size=15)
card(s, "Correções antes do scan", "WordPress 7.1.5, pacotes de segurança, kernel novo em uso e cabeçalhos "
                                   "no Apache. Restam CSP e os cabeçalhos na borda da Cloudflare.",
     8.4, 4.8, 4.36, 1.75, body_size=14)

# 10 — políticas e boas práticas
s = base("Políticas e boas práticas: identidade, auditoria e backup",
         "Fontes: evidencias_aws (capturas de 18/11/2026, recortadas); docs/architecture.pt-BR.md, seção 3",
         "Em identidade, cada integrante tem usuário IAM próprio, com acesso por SSO e política de senha de 14 "
         "caracteres, 90 dias e sem reuso. O CloudTrail registra todas as chamadas de API, em todas as regiões, "
         "com validação de integridade. Os backups são snapshots diários por DLM e dump do MySQL, e a "
         "restauração foi testada em 17 de novembro. Na aplicação, o WordPress tem MFA. Ficam como riscos "
         "aceitos a console AWS sem MFA e os volumes sem criptografia.")
praticas = [
    ("Identidade nominal", "5 usuários IAM individuais, acesso por SSO e política de senha: 14+ caracteres, 90 dias, sem reuso.",
     "evidencias_slides/iam_usuarios_2026-11-18.png"),
    ("Auditoria", "CloudTrail em todas as regiões, com validação de integridade e logs em bucket S3 privado.",
     "evidencias_slides/cloudtrail_2026-11-18.png"),
    ("Backup testado", "Snapshots diários por DLM (retenção de 7) e dump do MySQL; restauração conferida em 17/11.",
     "evidencias_slides/dlm_backups_2026-11-18.png"),
    ("Hardening da aplicação", "MFA TOTP no WordPress; token da Cloudflare com escopo mínimo; UFW no jump server.",
     "evidencias_aws/08_wordpress_mfa_totp_ativo.png"),
]
for i, (nome, texto, figura) in enumerate(praticas):
    x, y = LEFT + (i % 2) * 6.25, 1.22 + (i // 2) * 2.58
    txt(s, nome, x, y, 5.95, 0.34, 16, BLUE, True)
    txt(s, texto, x, y + 0.34, 5.95, 0.5, 12.5)
    img(s, figura, x, y + 0.88, 5.95, 1.58, halign="left")
box(s, LEFT, 6.4, WIDTH, 0.5, PALE)
txt(s, [[("Riscos aceitos e registrados na matriz: ", True, ORANGE),
         ("console AWS sem MFA (laboratório) e volumes EBS sem criptografia.", False, NAVY)]],
    LEFT + 0.2, 6.4, WIDTH - 0.4, 0.5, 13, anchor=MSO_ANCHOR.MIDDLE)

# 11 — impacto
s = base("Impacto: menos risco extremo, mais continuidade da loja",
         "Fonte: Matriz v2.2 e docs/risk-traceability.pt-BR.md (revisão de 19/11/2026)",
         "Na matriz, os riscos extremos caíram de 8 para 1, redução de 87,5%. Somando extremos e altos, fomos de "
         "22 para 15. Para o negócio isso significa loja disponível em campanha, dados de clientes isolados, "
         "ações administrativas com autor e recuperação testada. Esses números são uma avaliação estruturada do "
         "grupo, não uma medição de ataques evitados.")
img(s, FIG["grafico"], LEFT, 1.25, 7.4, 5.4, valign="middle", border=False)
for y, rotulo, valor, cor in ((1.3, "Riscos extremos", "8 → 1  (−87,5%)", CYAN),
                              (2.68, "Extremos + altos", "22 → 15  (−32%)", BLUE)):
    box(s, 8.2, y, 4.56, 1.2, PALE)
    box(s, 8.2, y, 0.07, 1.2, cor)
    txt(s, rotulo, 8.42, y + 0.1, 4.2, 0.34, 14, BLUE, True)
    txt(s, valor, 8.42, y + 0.44, 4.2, 0.66, 28, NAVY, True, anchor=MSO_ANCHOR.MIDDLE)
card(s, "Para o negócio",
     ["• Loja disponível em campanha", "• Dados de clientes isolados (LGPD)",
      "• Cada ação administrativa com autor", "• Recuperação testada, não presumida"],
     8.2, 4.06, 4.56, 2.1, accent=ORANGE, body_size=14, spacing=3)
txt(s, "Notas são avaliação do grupo, não medição de ataques evitados.", 8.2, 6.24, 4.56, 0.36, 11, GRAY)

# 12 — conclusão
residuais = ["• 1 extremo: segredos de aplicação e integrações",
             "• Console AWS sem MFA (aceito em laboratório)",
             "• Volumes EBS sem criptografia",
             "• Sem Auto Scaling nem Multi-AZ para campanhas"]
if not VPN_IMPLANTADA:
    residuais.append("• VPN (OpenVPN) ainda não implantada")
s = base("Conclusão, riscos residuais e próximos passos",
         "Fonte: Matriz v2.2 e docs/risk-traceability.pt-BR.md (seção 4)",
         "Entregamos a loja na AWS com banco isolado, WAF, administração por jump server com MFA, "
         "monitoramento e SIEM, e backup com restauração testada. Permanece um risco extremo, o de segredos de "
         "aplicação e integrações, além de lacunas de laboratório como a console AWS sem MFA e a "
         "falta de escala automática. Os próximos passos são treinamento, revisão periódica da matriz e dos "
         "acessos, e automação com infraestrutura como código e rotação de segredos.")
card(s, "O que foi entregue",
     ["• Loja na AWS com banco em sub-rede privada", "• Cloudflare com WAF (5 regras) e Fail2ban",
      "• Administração por jump server com TOTP", "• Wazuh, Zabbix, CloudWatch e CloudTrail",
      "• Backup diário com restauração testada"],
     0.56, 1.3, 3.92, 4.5, accent=CYAN, body_size=15, spacing=10)
card(s, "Riscos que permanecem", residuais, 4.70, 1.3, 3.92, 4.5, accent=ORANGE, body_size=15, spacing=10)
card(s, "Próximos passos",
     [[("Treinamento: ", True), ("conscientização contra phishing e exercício de resposta a incidentes.", False)],
      [("Revisão periódica: ", True), ("matriz, Security Groups e acessos a cada trimestre; scan recorrente.", False)],
      [("Automação: ", True), ("infraestrutura como código, rotação de segredos e atualização de pacotes.", False)],
      [("Capacidade: ", True), ("RDS Multi-AZ e Auto Scaling para campanhas.", False)]],
     8.84, 1.3, 3.92, 4.5, body_size=15, spacing=10)
box(s, LEFT, 6.0, WIDTH, 0.8, NAVY)
txt(s, "A matriz liga cada risco a controle, evidência e risco residual; o que não foi implementado está "
       "registrado como plano.", LEFT + 0.3, 6.0, WIDTH - 0.6, 0.8, 16, WHITE, True, anchor=MSO_ANCHOR.MIDDLE)

if sem_traducao:
    raise SystemExit("Textos sem tradução em textos_en.py:\n" + "\n".join(f"  - {t!r}" for t in sem_traducao))
prs.save(OUT)
print(f"{OUT.name}: {len(prs.slides)} slides")
if pendentes:
    print("Prints que ainda faltam (salvar e rodar de novo):")
    for item in pendentes:
        print("  -", item)
