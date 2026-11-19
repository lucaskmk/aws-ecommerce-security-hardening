**English** | [Português](README.pt-BR.md)

# Final delivery

Material for Group 3's final assessment: presentation, risk matrix, screenshots that prove each control and the scripts that generate the slides and figures.

The presentation exists in English and Portuguese. The risk matrix (PDF and XLSX) is in Portuguese only; its content is summarized in English in [`docs/risk-traceability.md`](../docs/risk-traceability.md). File and folder names (`evidencias_*`, `figuras`, `gerar_*`) are in Portuguese.

| File or folder | Content |
| --- | --- |
| [Final_Presentation_G3_EN.pdf](Final_Presentation_G3_EN.pdf) and `.pptx` | Final presentation in English, 12 slides |
| [Apresentacao_Final_G3.pdf](Apresentacao_Final_G3.pdf) and `.pptx` | Same presentation, in Portuguese |
| [Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.pdf](Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.pdf) and `.xlsx` | Matrix v2.2 with 25 risks, CIS v8 controls, residual risk and evidence (in Portuguese) |
| [evidencias_aws/](evidencias_aws/) | Screenshots of the AWS console, Cloudflare, WordPress and the jump server (2026-11-18) |
| [evidencias_novas/](evidencias_novas/) | Screenshots from the final week, used in the slides |
| [evidencias_slides/](evidencias_slides/) | Crops of original screenshots to fit the slides; the origin of each one is in [ORIGEM.md](evidencias_slides/ORIGEM.md) (in Portuguese) |
| [figuras/](figuras/) | Architecture diagram (PNG and SVG), heat map, before and after chart and icons; the English versions are in [figuras/en/](figuras/en/) |
| [gerar_figuras.py](gerar_figuras.py) | Reads the spreadsheet and recreates the heat map and the risk chart |
| [gerar_apresentacao.py](gerar_apresentacao.py) | Builds the 12-slide PPTX from the figures and screenshots |
| [textos_en.py](textos_en.py) | English translation of each slide text |
| [requirements.txt](requirements.txt) | Script dependencies |

The architecture rationale and the traceability of each risk are in [`docs/`](../docs/). The external scan is in [`external-scan/`](../external-scan/).

The screenshots show the interfaces as they were used, many of them in Portuguese.

## Evidence → control it proves

### evidencias_aws/

| File | Control |
| --- | --- |
| [00_waf_rate_limit_wp_admin.png](evidencias_aws/00_waf_rate_limit_wp_admin.png) | Cloudflare WAF rate limit on `/wp-admin` (error 1015) |
| [01_sg_webserver.png](evidencias_aws/01_sg_webserver.png) | Webserver accepts 80/443 only from the Cloudflare prefix list and SSH only from Guacamole |
| [02_sg_dbserver.png](evidencias_aws/02_sg_dbserver.png) | Database accepts 3306 only from the webserver Security Group, with no `0.0.0.0/0` rule |
| [03_sg_guacamole.png](evidencias_aws/03_sg_guacamole.png) | Jump server with 443 only from Cloudflare and 10050 only from the monitoring server |
| [04_sg_wazuh_zabbix.png](evidencias_aws/04_sg_wazuh_zabbix.png) | Monitoring with 443 restricted to the team's `/32` addresses, 1514/1515 only from the internal Security Groups and 10051 only from the VPC |
| [05b_iam_politica_senha.png](evidencias_aws/05b_iam_politica_senha.png) | IAM password policy (14+ characters, 90 days, no reuse) |
| [06_cloudtrail_ativo.png](evidencias_aws/06_cloudtrail_ativo.png) | Multi-region CloudTrail, with integrity validation and a private S3 bucket |
| [07_dlm_backups_e_snapshots.png](evidencias_aws/07_dlm_backups_e_snapshots.png) | DLM policy with daily snapshots and 7-day retention |
| [08_wordpress_mfa_totp_ativo.png](evidencias_aws/08_wordpress_mfa_totp_ativo.png) | TOTP MFA on the WordPress dashboard |
| [09_ufw_jump01_10050_restrito.png](evidencias_aws/09_ufw_jump01_10050_restrito.png) | Jump server UFW accepting port 10050 only from the Zabbix server (`10.0.4.20`) |

### evidencias_novas/

| File | Control |
| --- | --- |
| [fail2ban_ban.png](evidencias_novas/fail2ban_ban.png) | Fail2ban bans the IP after 5 failed logins and creates the block rule on Cloudflare |
| [guacamole_totp.png](evidencias_novas/guacamole_totp.png) | Guacamole login asking for the TOTP code |
| [vpn_tunel.png](evidencias_novas/vpn_tunel.png) | Active OpenVPN tunnel, with only UDP 1194 open |
| [wazuh_agentes.png](evidencias_novas/wazuh_agentes.png) | Three active Wazuh agents (web-01, db-01 and jump-01) |
| [zabbix_hosts.png](evidencias_novas/zabbix_hosts.png) | Four hosts available in Zabbix |
| [scan_final.png](evidencias_novas/scan_final.png) | Summary of the OWASP ZAP scan of 2026-11-19: no high alerts |

### evidencias_slides/

| File | Control |
| --- | --- |
| [iam_usuarios_2026-11-18.png](evidencias_slides/iam_usuarios_2026-11-18.png) | Individual IAM users, one per member |
| [cloudtrail_2026-11-18.png](evidencias_slides/cloudtrail_2026-11-18.png) | Active CloudTrail (crop of screenshot 06) |
| [dlm_backups_2026-11-18.png](evidencias_slides/dlm_backups_2026-11-18.png) | Daily DLM backups (crop of screenshot 07) |
| [wazuh_cves_roteiro1.png](evidencias_slides/wazuh_cves_roteiro1.png) | Wazuh vulnerability detection: starting point, with the CVEs found in Lab 1 |
| [wazuh_eventos_db01_2026-11-06.png](evidencias_slides/wazuh_eventos_db01_2026-11-06.png) | Centralized logging: Wazuh events in the database incident |
| [zabbix_hosts_2026-11-10.png](evidencias_slides/zabbix_hosts_2026-11-10.png) | Availability monitoring of the four hosts in Zabbix |
| [zabbix_email_2026-11-10.png](evidencias_slides/zabbix_email_2026-11-10.png) | Zabbix alert delivered by e-mail, with problem and recovery |

## How to regenerate

In the `final-delivery/` folder:

```bash
pip install -r requirements.txt               # python-pptx, matplotlib, openpyxl
python gerar_figuras.py                       # reads the spreadsheet and writes figuras/01_* and figuras/02_*
python gerar_figuras.py --lang en             # writes figuras/en/01_* and figuras/en/02_*
python gerar_apresentacao.py                  # writes Apresentacao_Final_G3.pptx
python gerar_apresentacao.py --lang en        # writes Final_Presentation_G3_EN.pptx
```

Run `gerar_figuras.py` again whenever a score in the matrix changes, and then `gerar_apresentacao.py`. If an expected screenshot in `evidencias_novas/` does not exist, the slide uses the previous screenshot or shows a "PRINT PENDENTE" ("screenshot pending") box.

The Portuguese texts live in `gerar_apresentacao.py`; the translations, in `textos_en.py`, keyed by the Portuguese text. If a text changes and its translation is not updated, `--lang en` stops and lists what is missing.

The architecture diagram is not generated by a script: the vector is in `figuras/03_diagrama_arquitetura_aws.svg` (English: `figuras/en/03_architecture_diagram_aws.svg`), and the 3840×2160 PNG was exported from it with a headless browser, for example:

```bash
msedge --headless --hide-scrollbars --force-device-scale-factor=2 --window-size=1920,1080 --screenshot=figuras/en/03_architecture_diagram_aws.png figuras/en/03_architecture_diagram_aws.svg
```

The PDFs were exported from the PPTX files with PowerPoint (Save as PDF).
