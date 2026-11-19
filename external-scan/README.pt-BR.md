[English](README.md) | **Português**

# Scan externo

Varredura da superfície pública da loja (`https://maisplace.net.br/`) com o OWASP ZAP, feita duas vezes: em 18/11/2026, como linha de base, e em 19/11/2026, depois das correções no servidor web e no banco.

## Método

- **Ferramenta:** OWASP ZAP 2.17.0, imagem `ghcr.io/zaproxy/zaproxy:stable`, script `zap-baseline.py`.
- **Modo:** *Baseline*, ou seja, crawl curto (`-m 2`) e apenas regras passivas. Nenhum ataque é enviado.
- **Escopo:** só a superfície pública, sem login, passando pela Cloudflare.
- **Saídas:** relatório em HTML, JSON e Markdown em uma pasta com data e hora.

## Como rodar

Requer Docker. Na raiz do repositório:

```bash
bash external-scan/rodar_scan_passivo.sh
```

O script só aceita `https://maisplace.net.br/` como alvo e grava em `external-scan/scan_<data>_<hora>/`. O ZAP termina com código 2 quando há avisos (`WARN`); isso não indica falha da execução.

## Resultado

| | 18/11 | 19/11 |
| --- | --- | --- |
| Alertas altos | 0 | 0 |
| Alertas médios | 8 | 7 |
| Alertas baixos | 10 | 10 |
| Alertas informativos | 10 | 10 |
| Tipos de alerta | 28 | 27 |
| Instâncias | 109 | 108 |
| Endpoints no relatório | 158 | 158 |
| URLs no crawl | 235 | não registrado |

Entre os dois scans, o WordPress foi para a versão 7.1.5, os pacotes de segurança foram aplicados no web-01 e no db-01 e o Apache passou a enviar HSTS, `X-Frame-Options`, `X-Content-Type-Options` e `Referrer-Policy`. O alerta de clickjacking (5 instâncias) sumiu. Continuam abertos: falta de CSP, avisos automáticos de token anti-CSRF e a biblioteca `moment.js` que vem com o WordPress.

## Limites

- Scan passivo e sem login: não cobre rotas autenticadas, checkout nem integrações.
- O tráfego passa pela Cloudflare, então o servidor de origem não é testado diretamente. Parte dos alertas restantes vem de respostas geradas pela própria Cloudflare ou de arquivos em cache.
- "Nenhum alerta alto" vale para o que o ZAP observou. Não demonstra ausência de vulnerabilidade alta.
- A tentativa complementar com WPScan em 18/11 foi interrompida por limites de requisição (respostas 429 e 403) antes de enumerar plugins; o arquivo `wpscan_limites.json` registra a cobertura incompleta, não um resultado.

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| [report-2026-11-18.pt-BR.md](report-2026-11-18.pt-BR.md) | Scan de linha de base, achados e lacunas (Eduardo); só em português |
| [report-2026-11-19.pt-BR.md](report-2026-11-19.pt-BR.md) | Correções aplicadas, scan final e comparação com 18/11 (Lucas); versão em inglês em [report-2026-11-19.md](report-2026-11-19.md) |
| [rodar_scan_passivo.sh](rodar_scan_passivo.sh) | Script de execução |
| [scan_2026-11-18/](scan_2026-11-18/) | Saídas brutas de 18/11, resumo em imagem e diagnóstico do WPScan |
| [scan_2026-11-19_013332/](scan_2026-11-19_013332/) | Saídas brutas de 19/11 |
