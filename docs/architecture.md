**English** | [Português](architecture.pt-BR.md)

# AWS architecture: rationale, hardening and evidence (SG, IAM)

**Project:** MaisPlace — Secure Migration to AWS (Group G3)  
**Official diagram (16:9 PNG, 3840×2160 + editable SVG):**
* `final-delivery/figuras/03_diagrama_arquitetura_aws.png` *(ready to paste into Slide 6; Portuguese)*
* `final-delivery/figuras/03_diagrama_arquitetura_aws.svg` *(editable vector; Portuguese)*
* English version: `final-delivery/figuras/en/03_architecture_diagram_aws.png` and `final-delivery/figuras/en/03_architecture_diagram_aws.svg`

---

## 1. Architectural rationale per component (requirement of Section 12 of the case study)

> *"The group must be able to justify why each component is located at that point of the architecture and which communications are really necessary."*

| Component | Location in the architecture | Why is it at this point? | Strictly necessary communications |
| :--- | :--- | :--- | :--- |
| **Cloudflare (DNS + Proxy + WAF)** | Edge layer (outside AWS) | Absorbs volumetric attacks (DoS/DDoS), applies 5 WAF rules before traffic touches AWS and hides the web server's origin IP. | Inbound: HTTPS (443) from the Internet.<br>Outbound: HTTPS (443) only to `web-01` and `jump-01` (TLS Full Strict). |
| **`web-01` (Apache / WordPress / WooCommerce)** | Public subnet (`us-east-1a`, `10.0.11.45`) | Needs to receive the HTTPS traffic forwarded by Cloudflare (origin behind a Managed Prefix List). Although it is in the public subnet, **direct access via the public IP results in a timeout** (the SG blocks everything except the Cloudflare Prefix List). | Inbound: `80/443` only Cloudflare; `22` only SG `jump-01`; `10050` only SG Zabbix.<br>Outbound: `3306` to `db-01`; `1514/1515` to Wazuh; `443` to the Cloudflare API (Fail2ban). |
| **`db-01` (MySQL 8)** | **Private subnet** (`us-east-1a`, `10.0.136.239`, **no public IP**) | Stores customer records, orders and information subject to the LGPD. Fully isolated from the Internet, with no direct inbound route from outside and with `bind-address` restricted to the private IP. | Inbound: `3306` **only** from SG `web-01`; `22` only from SG Guacamole (or maintenance); `10050` only from SG Zabbix.<br>Outbound: `1514/1515` to Wazuh; `10051` to Zabbix. |
| **`jump-01` (Apache Guacamole)** | Public subnet (`us-east-1a`, `10.0.4.101`) | Acts as the **single, standardized point for remote administration** (bastion host), eliminating SSH open to the Internet. Protected by Cloudflare + IP allowlist in Nginx + mandatory TOTP MFA + UFW. | Inbound: `443` only Cloudflare; `10050` only SG Zabbix.<br>Outbound: `22` (internal SSH) to `web-01`, `db-01` and `g3-wazuh-server`; `1514/1515` to Wazuh. |
| **`g3-wazuh-server` (Wazuh 4.9.2 + Zabbix 7.0)** | Public subnet with Elastic IP (`10.0.4.20` / `<MONITORING-EIP>`) | Centralizes SIEM (security/logs) and availability/performance monitoring, with HTTPS subdomains (`monitoramento` and `zabbix`) via Let's Encrypt and web access restricted to the team's `/32` addresses. | Inbound: `443` only the members' `/32`; `80` (ACME Certbot); `1514/1515` only internal SGs; `10051` only VPC.<br>Outbound: `10050` to Zabbix agents; `587` Gmail SMTP (alerts). |
| **AWS IAM, CloudTrail, CloudWatch/SNS and DLM** | AWS managed services layer (outside the VPC) | Separate governance, immutable audit (`CloudTrail` → private S3 with AES-256), infrastructure alerts (`CloudWatch` → `SNS`) and business continuity (`DLM` daily snapshots) from the application EC2 instances. | Internal communication through the AWS control plane / managed APIs. |

---

## 2. Hardening of `jump-01` (UFW port 10050) — completed on Nov 18

The internal **UFW** on `jump-01` had a broad rule for port `10050`, although the AWS Security Group already restricted it to the Wazuh/Zabbix SG. The fix was applied on Nov 18 (Sidney): the port now only accepts `10.0.4.20`. Evidence: `final-delivery/evidencias_aws/09_ufw_jump01_10050_restrito.png`.

Commands applied on `jump-01` (`ubuntu@ip-10-0-4-101`), as *Defense in Depth*:

```bash
sudo ufw status numbered
sudo ufw delete allow 10050/tcp
sudo ufw allow from 10.0.4.20 to any port 10050 proto tcp comment 'Zabbix Server'
sudo ufw status verbose
```

---

## 3. Dated AWS screenshots (Slides 7 and 10) — captured on Nov 18

The screenshots below were taken in the **AWS Console** on Nov 18 (Sidney), with date and time visible, and are in `final-delivery/evidencias_aws/`. The Security Group ones go into Slide 7; the IAM, CloudTrail and DLM ones, into Slide 10. If any needs to be redone, keep the **Windows clock date/time** visible:

1. **`01_sg_webserver.png`** — EC2 → Security Groups → `g3-webserver` (`sg-0db0cd00f2f9031da`), *Inbound rules* tab (showing 80/443 only from the Cloudflare Prefix List and 22 only from Guacamole).
2. **`02_sg_dbserver.png`** — `g3-dbserver` (`sg-03adf00c20d9725af`), *Inbound rules* tab (showing 3306 only from the `web-01` SG, with no `0.0.0.0/0` rule).
3. **`03_sg_guacamole.png`** — `g3-guacamole` (`sg-073f913d4abf7b330`), *Inbound rules* tab (showing 443 only from Cloudflare and 10050 only from the Wazuh/Zabbix SG).
4. **`04_sg_wazuh_zabbix.png`** — `g3-sc-wazuh` (`sg-037a90ce974392b5e`), *Inbound rules* tab (showing 443 restricted to the `/32` addresses, 1514/1515 only from internal SGs and 10051 only from the VPC).
5. **`final-delivery/evidencias_slides/iam_usuarios_2026-11-18.png`** (crop) and **`05b_iam_politica_senha.png`** — IAM → *Users* (showing the group's 5 individual users: `Edu`, `Kenji`, `Sid`, `Takahacker`, `RickRock`) and *Account settings* showing the password policy (14+ chars, 90 days, no reuse).
6. **`06_cloudtrail_ativo.png`** — CloudTrail → *Trails* (showing the active multi-region `g3-maisplace-trail`, integrity validation and private S3 bucket).
7. **`07_dlm_backups_e_snapshots.png`** — EC2 → *Lifecycle Manager* (showing policy `policy-0cc22d1984291ecdd` active with 7-day retention).

*(Note before adding them to the slides: if the numeric AWS account ID appears in the top right corner of the AWS Console, blur/crop it before pasting it into the presentation.)*
