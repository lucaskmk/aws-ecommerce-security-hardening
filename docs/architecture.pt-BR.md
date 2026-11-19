[English](architecture.md) | **Português**

# Arquitetura AWS: justificativas, hardening e evidências (SG, IAM)

**Projeto:** MaisPlace — Migração Segura para AWS (Grupo G3)  
**Diagrama oficial (PNG 16:9, 3840×2160 + SVG editável):**
* `final-delivery/figuras/03_diagrama_arquitetura_aws.png` *(pronto para colar no Slide 6)*
* `final-delivery/figuras/03_diagrama_arquitetura_aws.svg` *(vetor editável)*

---

## 1. Justificativa Arquitetural por Componente (Exigência da Seção 12 do Estudo de Caso)

> *"O grupo deverá ser capaz de justificar por que cada componente está localizado naquele ponto da arquitetura e quais comunicações são realmente necessárias."*

| Componente | Localização na Arquitetura | Por que está neste ponto? | Comunicações estritamente necessárias |
| :--- | :--- | :--- | :--- |
| **Cloudflare (DNS + Proxy + WAF)** | Camada de Borda (externa à AWS) | Absorve ataques volumétricos (DoS/DDoS), aplica 5 regras de WAF antes do tráfego tocar a AWS e oculta o IP de origem do servidor web. | Entrada: HTTPS (443) da Internet.<br>Saída: HTTPS (443) apenas para `web-01` e `jump-01` (TLS Full Strict). |
| **`web-01` (Apache / WordPress / WooCommerce)** | Sub-rede Pública (`us-east-1a`, `10.0.11.45`) | Precisa receber o tráfego HTTPS encaminhado pela Cloudflare (origem atrás de Managed Prefix List). Apesar de estar na sub-rede pública, **o acesso direto pelo IP público resulta em timeout** (SG bloqueia tudo exceto Prefix List Cloudflare). | Entrada: `80/443` só Cloudflare; `22` só SG `jump-01`; `10050` só SG Zabbix.<br>Saída: `3306` para `db-01`; `1514/1515` para Wazuh; `443` para API Cloudflare (Fail2ban). |
| **`db-01` (MySQL 8)** | **Sub-rede Privada** (`us-east-1a`, `10.0.136.239`, **sem IP público**) | Armazena dados cadastrais, pedidos e informações sujeitas à LGPD. Fica completamente isolado da Internet, sem rota direta de entrada externa e com `bind-address` restrito ao IP privado. | Entrada: `3306` **somente** do SG `web-01`; `22` somente de SG Guacamole (ou manutenção); `10050` somente de SG Zabbix.<br>Saída: `1514/1515` para Wazuh; `10051` para Zabbix. |
| **`jump-01` (Apache Guacamole)** | Sub-rede Pública (`us-east-1a`, `10.0.4.101`) | Atua como **ponto único e padronizado de administração remota** (bastion host), eliminando SSH aberto para a Internet. Protegido por Cloudflare + Allowlist de IP no Nginx + MFA TOTP obrigatório + UFW. | Entrada: `443` só Cloudflare; `10050` só SG Zabbix.<br>Saída: `22` (SSH interno) para `web-01`, `db-01` e `g3-wazuh-server`; `1514/1515` para Wazuh. |
| **`g3-wazuh-server` (Wazuh 4.9.2 + Zabbix 7.0)** | Sub-rede Pública com Elastic IP (`10.0.4.20` / `<EIP-MONITORAMENTO>`) | Centraliza SIEM (segurança/logs) e monitoramento de disponibilidade/desempenho com subdomínios HTTPS (`monitoramento` e `zabbix`) via Let's Encrypt e acesso web restrito aos `/32` da equipe. | Entrada: `443` só `/32` dos integrantes; `80` (ACME Certbot); `1514/1515` só SGs internos; `10051` só VPC.<br>Saída: `10050` para agentes Zabbix; `587` SMTP Gmail (alertas). |
| **AWS IAM, CloudTrail, CloudWatch/SNS e DLM** | Camada de Serviços Gerenciados AWS (fora da VPC) | Separam governança, auditoria imutável (`CloudTrail` → S3 privado AES-256), alertas de infraestrutura (`CloudWatch` → `SNS`) e continuidade de negócio (`DLM` snapshots diários) das EC2 de aplicação. | Comunicação interna via plano de controle AWS / APIs gerenciadas. |

---

## 2. Hardening do `jump-01` (UFW porta 10050) — concluído em 18/11

O **UFW** interno do `jump-01` tinha uma regra ampla para a porta `10050`, embora o Security Group da AWS já restringisse ao SG do Wazuh/Zabbix. O ajuste foi aplicado em 18/11 (Sidney): a porta agora só aceita `10.0.4.20`. Evidência: `final-delivery/evidencias_aws/09_ufw_jump01_10050_restrito.png`.

Comandos aplicados no `jump-01` (`ubuntu@ip-10-0-4-101`), como defesa em profundidade (*Defense in Depth*):

```bash
sudo ufw status numbered
sudo ufw delete allow 10050/tcp
sudo ufw allow from 10.0.4.20 to any port 10050 proto tcp comment 'Zabbix Server'
sudo ufw status verbose
```

---

## 3. Prints Datados da AWS (Slides 7 e 10) — capturados em 18/11

Os prints abaixo foram tirados no **Console AWS** em 18/11 (Sidney), com data e hora visíveis, e estão em `final-delivery/evidencias_aws/`. Os de Security Groups entram no Slide 7; os de IAM, CloudTrail e DLM, no Slide 10. Se algum precisar ser refeito, manter a **data/hora do relógio do Windows** visível:

1. **`01_sg_webserver.png`** — EC2 → Security Groups → `g3-webserver` (`sg-0db0cd00f2f9031da`), aba *Regras de entrada* (mostrando 80/443 só Cloudflare Prefix List e 22 só Guacamole).
2. **`02_sg_dbserver.png`** — `g3-dbserver` (`sg-03adf00c20d9725af`), aba *Regras de entrada* (mostrando 3306 só do SG `web-01`, sem nenhuma regra `0.0.0.0/0`).
3. **`03_sg_guacamole.png`** — `g3-guacamole` (`sg-073f913d4abf7b330`), aba *Regras de entrada* (mostrando 443 só Cloudflare e 10050 só SG Wazuh/Zabbix).
4. **`04_sg_wazuh_zabbix.png`** — `g3-sc-wazuh` (`sg-037a90ce974392b5e`), aba *Regras de entrada* (mostrando 443 restrito aos `/32`, 1514/1515 só dos SGs internos e 10051 só VPC).
5. **`final-delivery/evidencias_slides/iam_usuarios_2026-11-18.png`** (recorte) e **`05b_iam_politica_senha.png`** — IAM → *Usuários* (mostrando os 5 usuários individuais do grupo: `Edu`, `Kenji`, `Sid`, `Takahacker`, `RickRock`) e *Configurações da conta* mostrando a política de senha (14+ chars, 90 dias, sem reuso).
6. **`06_cloudtrail_ativo.png`** — CloudTrail → *Trilhas* (mostrando `g3-maisplace-trail` multi-região ativa, validação de integridade e bucket S3 privado).
7. **`07_dlm_backups_e_snapshots.png`** — EC2 → *Lifecycle Manager* (mostrando a política `policy-0cc22d1984291ecdd` ativa com retenção de 7 dias).

*(Atenção antes de colocar nos slides: se o ID numérico da conta AWS aparecer no canto superior direito do Console AWS, borrar/cortar antes de colar na apresentação).*
