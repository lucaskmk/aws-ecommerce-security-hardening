[English](README.md) | **Português**

# Entrega final

Material da avaliação final do Grupo 3: apresentação, matriz de riscos, prints que comprovam cada controle e os scripts que geram slides e figuras.

| Arquivo ou pasta | Conteúdo |
| --- | --- |
| [Apresentacao_Final_G3.pdf](Apresentacao_Final_G3.pdf) e `.pptx` | Apresentação final, 12 slides |
| [Final_Presentation_G3_EN.pdf](Final_Presentation_G3_EN.pdf) e `.pptx` | Mesma apresentação, em inglês |
| [Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.pdf](Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.pdf) e `.xlsx` | Matriz v2.2 com 25 riscos, controles CIS v8, risco residual e evidências |
| [evidencias_aws/](evidencias_aws/) | Prints do console AWS, da Cloudflare, do WordPress e do jump server (18/11/2026) |
| [evidencias_novas/](evidencias_novas/) | Prints da semana final, usados nos slides |
| [evidencias_slides/](evidencias_slides/) | Recortes de prints originais para caber nos slides; a origem de cada um está em [ORIGEM.md](evidencias_slides/ORIGEM.md) |
| [figuras/](figuras/) | Diagrama da arquitetura (PNG e SVG), mapa de calor, gráfico antes e depois e ícones; as versões em inglês ficam em [figuras/en/](figuras/en/) |
| [gerar_figuras.py](gerar_figuras.py) | Lê a planilha e recria o mapa de calor e o gráfico de riscos |
| [gerar_apresentacao.py](gerar_apresentacao.py) | Monta o PPTX de 12 slides a partir das figuras e dos prints |
| [textos_en.py](textos_en.py) | Tradução para o inglês de cada texto dos slides |
| [requirements.txt](requirements.txt) | Dependências dos scripts |

A justificativa da arquitetura e a rastreabilidade de cada risco estão em [`docs/`](../docs/). O scan externo está em [`external-scan/`](../external-scan/).

## Evidência → controle que ela comprova

### evidencias_aws/

| Arquivo | Controle |
| --- | --- |
| [00_waf_rate_limit_wp_admin.png](evidencias_aws/00_waf_rate_limit_wp_admin.png) | Rate limit do WAF da Cloudflare em `/wp-admin` (erro 1015) |
| [01_sg_webserver.png](evidencias_aws/01_sg_webserver.png) | Webserver aceita 80/443 só da lista de prefixos da Cloudflare e SSH só do Guacamole |
| [02_sg_dbserver.png](evidencias_aws/02_sg_dbserver.png) | Banco aceita 3306 só do Security Group do webserver, sem regra `0.0.0.0/0` |
| [03_sg_guacamole.png](evidencias_aws/03_sg_guacamole.png) | Jump server com 443 só da Cloudflare e 10050 só do servidor de monitoramento |
| [04_sg_wazuh_zabbix.png](evidencias_aws/04_sg_wazuh_zabbix.png) | Monitoramento com 443 restrita a `/32` da equipe, 1514/1515 só dos Security Groups internos e 10051 só da VPC |
| [05b_iam_politica_senha.png](evidencias_aws/05b_iam_politica_senha.png) | Política de senha do IAM (14+ caracteres, 90 dias, sem reuso) |
| [06_cloudtrail_ativo.png](evidencias_aws/06_cloudtrail_ativo.png) | CloudTrail multi-região, com validação de integridade e bucket S3 privado |
| [07_dlm_backups_e_snapshots.png](evidencias_aws/07_dlm_backups_e_snapshots.png) | Política DLM de snapshots diários com retenção de 7 dias |
| [08_wordpress_mfa_totp_ativo.png](evidencias_aws/08_wordpress_mfa_totp_ativo.png) | MFA por TOTP no painel do WordPress |
| [09_ufw_jump01_10050_restrito.png](evidencias_aws/09_ufw_jump01_10050_restrito.png) | UFW do jump server aceitando a porta 10050 só do servidor Zabbix (`10.0.4.20`) |

### evidencias_novas/

| Arquivo | Controle |
| --- | --- |
| [fail2ban_ban.png](evidencias_novas/fail2ban_ban.png) | Fail2ban bane o IP após 5 falhas de login e cria a regra de bloqueio na Cloudflare |
| [guacamole_totp.png](evidencias_novas/guacamole_totp.png) | Login do Guacamole pedindo o código TOTP |
| [vpn_tunel.png](evidencias_novas/vpn_tunel.png) | Túnel OpenVPN ativo, com apenas UDP 1194 aberta |
| [wazuh_agentes.png](evidencias_novas/wazuh_agentes.png) | Três agentes do Wazuh ativos (web-01, db-01 e jump-01) |
| [zabbix_hosts.png](evidencias_novas/zabbix_hosts.png) | Quatro hosts disponíveis no Zabbix |
| [scan_final.png](evidencias_novas/scan_final.png) | Resumo do scan OWASP ZAP de 19/11/2026: nenhum alerta alto |

### evidencias_slides/

| Arquivo | Controle |
| --- | --- |
| [iam_usuarios_2026-11-18.png](evidencias_slides/iam_usuarios_2026-11-18.png) | Usuários IAM individuais, um por integrante |
| [cloudtrail_2026-11-18.png](evidencias_slides/cloudtrail_2026-11-18.png) | CloudTrail ativo (recorte do print 06) |
| [dlm_backups_2026-11-18.png](evidencias_slides/dlm_backups_2026-11-18.png) | Backups diários por DLM (recorte do print 07) |
| [wazuh_cves_roteiro1.png](evidencias_slides/wazuh_cves_roteiro1.png) | Detecção de vulnerabilidades do Wazuh: situação de partida, com as CVEs encontradas no Roteiro 1 |
| [wazuh_eventos_db01_2026-11-06.png](evidencias_slides/wazuh_eventos_db01_2026-11-06.png) | Logging centralizado: eventos do Wazuh no incidente do banco |
| [zabbix_hosts_2026-11-10.png](evidencias_slides/zabbix_hosts_2026-11-10.png) | Monitoramento de disponibilidade dos quatro hosts no Zabbix |
| [zabbix_email_2026-11-10.png](evidencias_slides/zabbix_email_2026-11-10.png) | Alerta do Zabbix entregue por e-mail, com problema e recuperação |

## Como regerar

Na pasta `final-delivery/`:

```bash
pip install -r requirements.txt               # python-pptx, matplotlib, openpyxl
python gerar_figuras.py                       # lê a planilha e grava figuras/01_* e figuras/02_*
python gerar_figuras.py --lang en             # grava figuras/en/01_* e figuras/en/02_*
python gerar_apresentacao.py                  # grava Apresentacao_Final_G3.pptx
python gerar_apresentacao.py --lang en        # grava Final_Presentation_G3_EN.pptx
```

Rode `gerar_figuras.py` de novo sempre que uma nota da matriz mudar, e depois `gerar_apresentacao.py`. Se um print esperado em `evidencias_novas/` não existir, o slide usa o print anterior ou mostra um quadro "PRINT PENDENTE".

Os textos em português ficam em `gerar_apresentacao.py`; as traduções, em `textos_en.py`, indexadas pelo texto em português. Se um texto mudar e a tradução não acompanhar, `--lang en` para e lista o que ficou sem tradução.

O diagrama da arquitetura não é gerado por script: o vetor está em `figuras/03_diagrama_arquitetura_aws.svg` (inglês: `figuras/en/03_architecture_diagram_aws.svg`), e o PNG de 3840×2160 foi exportado dele com um navegador em modo headless, por exemplo:

```bash
msedge --headless --hide-scrollbars --force-device-scale-factor=2 --window-size=1920,1080   --screenshot=figuras/en/03_architecture_diagram_aws.png figuras/en/03_architecture_diagram_aws.svg
```

Os PDFs foram exportados dos PPTX pelo PowerPoint (Salvar como PDF).
