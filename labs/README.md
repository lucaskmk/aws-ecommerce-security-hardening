**English** | [Português](README.pt-BR.md)

# Labs

The four lab assignments built the MaisPlace environment in stages, and the class activity analyzed access and monitoring on top of what already existed. Each stage started from the state left by the previous one.

The reports (PDF and DOCX) are in Portuguese. The sections below are the English summary of each one.

## Lab 1 — Webserver and security platform (2026-09-15)

**Goal:** bring the store up on AWS with a separate database, put Cloudflare in front of it and install a SIEM.

- EC2 webserver (t3.micro, Ubuntu) with Apache, PHP, WordPress and a certificate via certbot; Security Group with 80/443 only for the Cloudflare prefix list.
- MySQL database on its own instance, in a private subnet, with no public IP, `bind-address` on the private IP and 3306 accepted only from the webserver Security Group.
- Cloudflare as DNS and WAF, with 5 rules: geo-blocking (Brazil only), plugin exploitation, SQL injection, rate limit on `/wp-admin` and blocking of `/wp-json/wp/v2/users`.
- Wazuh with vulnerability detection, agents on the web and database servers, a custom rule for access to `wp-config.php`, real-time FIM on `/var/www/html` and log ingestion through CloudWatch.

**Result:** environment working behind Cloudflare and with security visibility. Wazuh e-mail delivery was recorded as a limitation: `wazuh-maild` does not authenticate to Gmail.

Report (in Portuguese): [Relatorio_Roteiro1.pdf](lab-1-infra-waf-siem/Relatorio_Roteiro1.pdf)

## Lab 2 — Administrative access control and automated rules (2026-10-07)

**Goal:** get rid of exposed SSH, automate the response to brute force and prevent anyone from bypassing Cloudflare.

- Apache Guacamole in Docker Compose as the jump server, behind Nginx, with mandatory TOTP, an IP allowlist, port 8080 only on loopback and UFW.
- Webserver SSH allowed only from the Guacamole Security Group.
- Fail2ban reading the real client IP (`mod_remoteip` with `CF-Connecting-IP`): 5 failures on `/wp-login.php` within 10 minutes trigger a 1-hour block created through the Cloudflare API, with a minimal-scope token.
- Managed prefix list with the Cloudflare IPs in the webserver Security Group.

**Result:** the simulated attack from a 4G network was blocked on the sixth attempt (HTTP 403 and then Cloudflare error 1107), and direct access via the server IP started to time out.

Report (in Portuguese): [Relatorio_Roteiro2.pdf](lab-2-jump-server-fail2ban/Relatorio_Roteiro2.pdf)

## Lab 3 — Monitoring with Amazon CloudWatch

**Goal:** create alarms on the webserver and deliver the notifications to the group.

- SNS topic `Alertas-CloudWatch`, with one e-mail subscription per member.
- `High-CPU-Alarm`: CPU above 70% over 5 minutes; tested with `stress` and triggered with an average of 99.99%.
- `High-Network-Traffic-Alarm`: NetworkIn above 50 MB per minute, with detailed monitoring; tested with a batch download of about 1 GB.
- `High-Disk-Write-Alarm`: volume writes above 100 MB per minute; tested with a 150 MB `dd`.
- `System-Status-Check-Alarm`: failed status check; the test section for this alarm was marked as pending in the report.

**Result:** for the three tested alarms, the full flow worked: metric, change to ALARM, publication to SNS and e-mail in about one minute.

Report (in Portuguese): [Relatorio_Roteiro3.pdf](lab-3-cloudwatch/Relatorio_Roteiro3.pdf)

## Class activity — Cloud resource management (2026-11-03)

**Goal:** analyze who accesses each resource, with which privilege, and what should be monitored.

- Table of resources (webserver, database, Guacamole, Wazuh/Zabbix, Cloudflare token) with access, privileges, excesses and impact of compromise.
- Analysis of the compromise of Guacamole and of the Cloudflare token.
- Use of IAM roles and users and application of least privilege.
- Signals monitored per layer (CloudWatch, Zabbix, Wazuh) and a data leak scenario: what would have been prevented, detected or not.

**Result:** conclusion that the network was well locked down, but the identities inside the resources (WordPress without MFA, MySQL user with `ALL`, shared account on Guacamole) still had too much privilege. Several of these points went into the risk matrix of the final delivery.

Report (in Portuguese): [Relatorio.pdf](class-activity-resource-management/Relatorio.pdf)

## Lab 4 — Operations and management with Zabbix (2026-11-10)

**Goal:** install Zabbix, monitor the servers, configure alerts and compare Zabbix and Wazuh.

- Zabbix 7.0 installed on the same instance as Wazuh, with 2 GB of swap, a limited MySQL and nginx publishing Zabbix and Wazuh per subdomain on the same port 443, with a Let's Encrypt certificate.
- Four monitored hosts (Zabbix server, db-01, jump-01, web-01), with Linux, MySQL and Docker templates and checks for Apache and Guacamole.
- Seven custom triggers with hysteresis, CPU and stopped-agent tests and e-mail alerting with problem and recovery.
- Zabbix × Wazuh comparison on the real database incident on 2026-11-06 (summarized in [`docs/incident-db01.md`](../docs/incident-db01.md)).

**Result:** operational monitoring working, with the main lesson of the project: the alerts existed, but nobody was notified and the site was down for hours.

Report (in Portuguese): [Roteiro4_Relatorio_Final.docx](lab-4-zabbix/report/Roteiro4_Relatorio_Final.docx). The DOCX is generated by Python scripts; see the [report README](lab-4-zabbix/report/README.md). The [`task1-zabbix-https/`](lab-4-zabbix/task1-zabbix-https/) folder holds the text, screenshots, configurations and resource measurements of the installation (in Portuguese).
