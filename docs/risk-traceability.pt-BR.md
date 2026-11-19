[English](risk-traceability.md) | **Português**

# Rastreabilidade de riscos altos, quadro "antes x depois" e respostas executivas

**Projeto:** MaisPlace — Migração Segura para AWS (Grupo G3)  
**Base:** `final-delivery/Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.xlsx` (v2.2 — revisada em 19/11/2026: ID 4 revisto após o scan final; base v2.1 de 18/11)  

---

## 1. Resumo da Auditoria da Matriz v2.1 (CIS Controls v8 e Consistência)

* **52 salvaguardas CIS v8 auditadas:**
  * **Correção aplicada (ID 7 — Movimentação lateral):** removida a referência a `4.5` (*Firewall on End-User Devices*, aplicável apenas a estações de trabalho), mantendo `4.4` (Firewall on Servers), `12.2` (Secure Network Architecture) e `13.4` (Traffic Filtering Between Network Segments).
  * **Complementos de precisão:** adicionados `7.4` (Automated Application Patch Management) e `7.5` (Internal Vulnerability Scans) no **ID 4**, e `11.4` (Isolated Instance of Recovery Data) nos **IDs 8 e 15**.
* **Padronização de fórmulas:** alinhada a coluna `J` (Classificação Original) com a coluna `S` (Classificação Residual) e com a legenda oficial da aba `Descrição e Matriz` (`3–6 Moderado`, `7–9 Alto`, `>9 Extremo`).
* **Resultados consolidados (25 riscos totais):**
  * **Original (Legado):** 8 Extremos | 14 Altos | 3 Moderados | 0 Baixos (**22 riscos Extremo/Alto**).
  * **Residual (AWS + Controles):** **1 Extremo** | **14 Altos** | **10 Moderados** | 0 Baixos (**15 riscos Extremo/Alto**, dos quais 4 estão como plano proposto, por serem organizacionais ou de processo (IDs 12, 17, 18 e 22), e 1 está fora do escopo do laboratório (ID 14)).
  * **Redução efetiva:** **−87,5% em riscos Extremos (8 → 1)** e **−31,8% no total Extremo + Alto (22 → 15)**. Até 18/11 eram 2 Extremos residuais; o ID 4 caiu para Alto em 19/11.
  * As figuras são geradas por `final-delivery/gerar_figuras.py`, que lê as notas direto da planilha.

### Figuras prontas para os slides (em `final-delivery/figuras/`):
* **Slide 4 (Matriz de Risco):** `final-delivery/figuras/01_mapa_calor_original_vs_residual.png`
* **Slide 11 (Impactos e Benefícios):** `final-delivery/figuras/02_grafico_riscos_antes_x_depois.png`

---

## 2. Tabela de Rastreabilidade dos Riscos Críticos/Altos (Seção 11 do Estudo de Caso)

Atende diretamente à exigência: **`Risco → Requisito de segurança → Controle (CIS v8) → Implementação AWS → Evidência`**.

| ID | Risco / Ameaça | Orig → Res | Requisito de Segurança | Controles CIS v8 | Controle Implementado no Ambiente AWS | Evidência / Fonte | Status |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| **1** | Comprometimento de credenciais administrativas | **16 (Ext)** → **8 (Alt)** | Acesso administrativo forte com autenticação multifator, bloqueio de força bruta e auditoria de sessões | `5.2, 5.4, 6.3, 6.4, 6.5, 8.2` | Guacamole com **TOTP obrigatório** e allowlist no Nginx; **WordPress com MFA TOTP + Recovery Codes (`Two-Factor`, 18/11)**; Fail2ban + API Cloudflare (bloqueio após 5 falhas); rate limit no WAF em `/wp-admin`; 5 usuários IAM nominais + política de senha 14+ chars + SSO + CloudTrail. *Risco aceito em lab:* sem MFA na AWS. | Roteiros 1, 2 e 4; Prints IAM, CloudTrail, Guacamole e `08_wordpress_mfa_totp_ativo.png` | Parcial |
| **2** | Insider / abuso de privilégio por conta compartilhada | **9 (Alt)** → **6 (Mod)** | Identidade nominal e rastreabilidade individual de ações administrativas | `5.1, 5.4, 6.1, 6.8, 8.2` | 5 usuários IAM individuais + SSO nominal; CloudTrail multi-região registrando autoria de ações na AWS; acesso SSH restrito via chaves. *Lacuna:* grupo `admin` amplo e contas compartilhadas no Guacamole/Zabbix. | Prints IAM + CloudTrail (17/11) | Parcial |
| **3** | Segredos de aplicação e integrações expostos | **16 (Ext)** → **12 (Ext)** | Proteção de tokens/chaves em trânsito e em repouso com menor privilégio e rotação | `3.11, 5.2, 6.8` | Token Cloudflare com escopo mínimo (firewall da zona), restrito por IP, `chmod 600` via variável de ambiente; usuário `wazuh-cloudwatch-reader` somente leitura. *Lacuna:* sem Secrets Manager, sem expiração do token, chave fixa do CloudWatch. | Roteiro 2 e Atividade de Gerenciamento | Parcial |
| **4** | Ataque contra aplicação Web (WooCommerce / plugins) | **16 (Ext)** → **8 (Alt)*** | Filtragem de camada de aplicação, detecção de alterações em arquivos e gestão de vulnerabilidades | `7.1, 7.4, 7.5, 7.6, 13.10, 16.4, 18.2` | WAF Cloudflare com 5 regras (geo-block, plugins, SQLi, rate limit, bloqueio `/wp-json/wp/v2/users`); Wazuh Vulnerability Detection + FIM em `/var/www/html`; em 19/11, WordPress 7.1.5 com plugins e tema na última versão (inventário por `wp-cli`), pacotes de segurança aplicados e scan externo final sem alertas altos. *Lacuna:* scan passivo, sem teste autenticado; sem CSP. | Roteiros 1 e 2; `external-scan/report-2026-11-19.pt-BR.md` e `final-delivery/evidencias_novas/scan_final.png` | Parcial |
| **5** | Injeção SQL e falhas em integrações sob medida | **12 (Ext)** → **8 (Alt)** | Filtragem de payload SQLi e isolamento total do banco de dados | `5.4, 13.10, 16.1, 16.12` | Regra de SQLi ativa no WAF Cloudflare; MySQL em **sub-rede privada** sem IP público, `bind-address` no IP privado, SG aceitando porta `3306` exclusivamente do SG do `web-01`. *Lacuna:* usuário MySQL do WP com `ALL`. | Roteiro 1; Prints WAF e SG `g3-dbserver` | Parcial |
| **6** | Vazamento de dados pessoais de clientes (LGPD) | **12 (Ext)** → **8 (Alt)** | Segmentação por camada, ocultação da origem e criptografia em trânsito | `3.3, 3.10, 3.11, 12.2, 13.4` | Banco isolado em sub-rede privada; SGs referenciando SGs (sem CIDR amplo); `web-01` só aceita 80/443 da Prefix List da Cloudflare (acesso direto pelo IP dá timeout); TLS Full Strict; bloqueio de enumeração de usuários na REST API. *Lacuna:* EBS sem criptografia. | Roteiros 1 e 2; Prints SGs e teste de timeout | Parcial |
| **7** | Movimentação lateral por falta de segmentação | **9 (Alt)** → **6 (Mod)** | Microssegmentação por função com negação por padrão | `4.4, 12.2, 13.4` | SGs segregados por função (Web, DB, Guacamole, Monitoramento); SSH do web só via Guacamole; portas `55000` e `10050` indevidamente abertas foram fechadas em 17/11; UFW ativo no Guacamole. | Prints atualizados dos 4 SGs (17/11) | **Implementado** |
| **8** | Malware e ransomware | **12 (Ext)** → **8 (Alt)** | Detecção de integridade/rootkits e backups recuperáveis | `7.4, 10.1, 11.2, 11.3, 11.4, 11.5` | Wazuh com FIM, SCA e rootcheck nos 3 servidores (`web-01`, `db-01`, `jump-01`); política DLM de snapshots diários (7 dias) + dump diário do MySQL + **teste de restauração validado** em 17/11. *Lacuna:* backup na mesma conta/região (sem Vault Lock). | Roteiro 1; Logs DLM + teste de restore (17/11) | Parcial |
| **9** | Negação de serviço (DoS/DDoS) | **8 (Alt)** → **6 (Mod)** | Proteção de perímetro, absorção de tráfego e ocultação da origem | `12.2, 13.4, 13.10` | Proxy Cloudflare ocultando IP de origem + geo-block fora do Brasil + rate limit; SG do `web-01` restrito à Prefix List da Cloudflare; alarme de tráfego de rede no CloudWatch com SNS. *Lacuna:* sem Auto Scaling/Multi-AZ. | Roteiros 1, 2 e 3; Prints Cloudflare + CloudWatch | Parcial |
| **10** | Indisponibilidade por esgotamento de capacidade em campanha | **9 (Alt)** → **9 (Alt)** | Observabilidade de saturação e estabilidade de banco | `12.2, 13.1` | CloudWatch (CPU, Rede, Disco, Status Check + SNS) e Zabbix 7.0 (4 hosts + triggers + e-mail). Estabilização do `db-01` em 17/11 (CPU `unlimited`, swap 1 GB, tuning MySQL). *Lacuna:* sem ALB/Auto Scaling nem RDS Multi-AZ (instâncias enxutas de lab). | Roteiros 3 e 4; Incidente real `db-01` | Parcial |
| **11** | Força bruta e exposição da administração remota | **9 (Alt)** → **3 (Mod)** | Eliminação de SSH público e padronização de acesso administrativo com MFA | `4.4, 6.4, 6.5, 13.5` | Porta 22 fechada para a Internet; acesso centralizado no **Guacamole com TOTP + allowlist**; Fail2ban + Cloudflare banindo atacantes por 1h; painéis Wazuh/Zabbix restritos a `/32`. | Roteiros 2 e 4; Prints Guacamole, Fail2ban e SGs | **Implementado** |
| **15** | Perda de dados por backup sem teste de recuperação | **8 (Alt)** → **4 (Mod)** | Rotina automatizada de backup com teste comprovado de restauração | `11.1, 11.2, 11.3, 11.4, 11.5` | DLM diário (`Backup=daily`, retenção 7 dias) + 4 snapshots iniciais + cron `mysql-backup.sh` + **teste real de restauração** em 17/11 validando 51 tabelas, 11 posts e 421 opções. | Evidência de DLM e teste de restore (17/11) | **Implementado** |
| **16** | Ausência de logging centralizado (incidente não investigável) | **12 (Ext)** → **6 (Mod)** | Centralização de logs de SO, aplicação e trilha de auditoria AWS | `8.2, 8.5, 8.9, 8.11, 13.1` | Wazuh 4.9.2 centralizando logs e alertas dos 3 servidores + ingestão CloudWatch; Zabbix 7.0 para métricas; **CloudTrail multi-região** com validação de integridade em bucket S3 privado criptografado. | Roteiros 1 e 4; Prints Wazuh (3 agentes), Zabbix e CloudTrail | **Implementado** |
| **20** | Erro de configuração na nuvem e falta de controle de mudanças | **12 (Ext)** → **8 (Alt)** | Revisão rigorosa de regras de exposição e trilha de auditoria de mudanças | `4.1, 4.2, 12.2` | Auditoria e fechamento de regras amplas em 17/11 (portas `10050` e `55000`); CloudTrail registrando todas as chamadas de API AWS. *Lacuna:* sem IaC (Terraform/CloudFormation) nem contas separadas Dev/Homolog/Prod. | Prints SGs revisados + CloudTrail (17/11) | Parcial |
| **24** | Interceptação de tráfego administrativo (MITM) | **6 (Mod)** → **3 (Mod)** | Criptografia forte ponta a ponta em todos os acessos web e administrativos | `3.10, 12.6` | HTTPS com certificados válidos (Let's Encrypt + Cloudflare Full Strict) na loja, Guacamole, Wazuh e Zabbix; administração SSH exclusivamente cifrada via Guacamole. | Roteiros 1, 2 e 4; Prints de certificados HTTPS | **Implementado** |

*\*Nota sobre o ID 4: a probabilidade residual foi de 3 para 2 em 19/11, depois da atualização do WordPress e do scan externo final sem alertas altos (`external-scan/report-2026-11-19.pt-BR.md`), o que leva a nota de **12 (Extremo)** para **8 (Alto)**. O scan é passivo e sem login; essa limitação fica registrada como lacuna. Resta **1 risco Extremo residual (ID 3)**.*

---

## 3. Quadro Executivo "Antes x Depois" (Pronto para o Slide 5)

| Dimensão de Segurança | ANTES (Ambiente Legado MaisPlace) | DEPOIS (Ambiente AWS — Grupo G3) | Impacto no Negócio |
| :--- | :--- | :--- | :--- |
| **Perímetro e Aplicação Web** | Servidor único exposto diretamente na Internet, sem WAF e sem proteção contra SQLi/força bruta. | **Cloudflare Proxy + WAF (5 regras)** + **Fail2ban automatizado** + origem oculta (acesso direto ao IP bloqueado). | Proteção contínua do faturamento contra ataques web e DDoS durante campanhas. |
| **Isolamento de Dados (LGPD)** | Aplicação e banco na mesma rede plana com poucas restrições de comunicação. | **MySQL em sub-rede privada** sem IP público, porta `3306` exclusiva do SG do `web-01` e TLS Full Strict. | Redução drástica da chance de exfiltração da base de clientes e multas da ANPD. |
| **Acesso Administrativo** | Contas compartilhadas sem padrão único de acesso remoto e sem MFA (causa do Incidente 2). | **SSH público eliminado**; acesso via **Jump Server (Guacamole) com TOTP obrigatório** + allowlist + 5 contas IAM nominais. | Eliminação de ataques de força bruta SSH e rastreabilidade individual de ações. |
| **Visibilidade e Logs** | Logs dispersos consultados só após falhas; monitoramento restrito a "está ligado ou não". | **Wazuh SIEM (3 agentes 4.9.2)** + **Zabbix 7.0 (4 hosts + e-mail)** + **CloudWatch/SNS** + **CloudTrail multi-região**. | Detecção rápida de causa raiz (provado no incidente real do `db-01`) e capacidade de auditoria forense. |
| **Continuidade e Backups** | Backups gerados sem nenhum teste recente de restauração. | **AWS DLM diário (7 dias)** + **dump diário do MySQL** com **teste real de restauração validado** (51 tabelas conferidas). | Garantia comprovada de recuperação do e-commerce em caso de falha grave ou ransomware. |

---

## 4. Respostas Prontas para as 7 Perguntas Obrigatórias da Apresentação (Seção 14)

Use este roteiro para fechar os slides e preparar a equipe para a arguição do professor:

1. **Qual arquitetura foi implementada?**  
   VPC dedicada na AWS (`us-east-1`) segmentada em sub-rede pública (`web-01`, `jump-01`, `g3-wazuh-server`) e sub-rede privada (`db-01` sem IP público), protegida na borda por **Cloudflare DNS/Proxy/WAF** e gerenciada por **Security Groups referenciados por função**, **CloudTrail**, **CloudWatch/SNS**, **Wazuh 4.9.2** e **Zabbix 7.0**.
2. **Quais riscos influenciaram as principais decisões arquiteturais?**  
   Os 3 incidentes reais da MaisPlace (queda em campanha, acesso administrativo não rastreado na madrugada e mudança direta em produção) e os 8 riscos Extremos da matriz — especialmente vazamento de dados (LGPD), invasão por plugins WooCommerce, força bruta administrativa e ausência de logs.
3. **Quais controles foram implementados?**  
   Isolamento de banco privado, WAF com 5 regras, Fail2ban integrado à API Cloudflare, Guacamole com TOTP + allowlist, IAM nominal + política de senha + CloudTrail, Wazuh SIEM (FIM, SCA, Vulnerability Detection, 3 agentes), Zabbix 7.0 (alertas por e-mail), CloudWatch/SNS e backups automatizados (DLM + dump MySQL testado).
4. **Como esses controles foram configurados?**  
   Princípio do menor privilégio em rede: `web-01` aceita `80/443` somente da Prefix List da Cloudflare e SSH apenas do SG do Guacamole; `db-01` aceita `3306` apenas do SG do `web-01`; `g3-wazuh-server` aceita agentes apenas dos SGs internos e painéis HTTPS apenas de `/32` autorizados.
5. **Quais evidências demonstram seu funcionamento?**  
   Prints datados de todos os SGs, IAM/CloudTrail, timeout no acesso direto ao IP do web, bloqueios do WAF e Fail2ban, 3 agentes ativos no Wazuh, 4 hosts verdes e alertas de e-mail no Zabbix, teste real de restauração do banco (17/11), análise do incidente real do `db-01` (Zabbix detectou efeito, Wazuh a causa) e scan externo final de 19/11 (OWASP ZAP Baseline, depois das correções: nenhum alerta alto, 7 médios). *Limite:* o scan é passivo e não cobre rotas autenticadas nem o servidor de origem.
6. **Quais riscos permanecem (riscos residuais)?**  
   * **Técnicos de laboratório:** ausência de MFA na AWS (risco aceito pelo grupo em ambiente acadêmico), volumes EBS sem criptografia, ausência de AWS Secrets Manager (chaves estáticas no `wazuh-cloudwatch-reader` e token Cloudflare sem expiração), ausência de Auto Scaling/Multi-AZ e memória apertada no servidor Wazuh+Zabbix.
   * **Organizacionais (Plano proposto):** programa de conscientização contra phishing, gestão formal de terceiros/offboarding, plano formal de resposta a incidentes com DPO (LGPD) e ambientes separados Dev/Homolog/Prod.
7. **O que seria implementado em uma próxima etapa em produção?**  
   Migração do banco para **Amazon RDS Multi-AZ criptografado com KMS**, **ALB + Auto Scaling** para campanhas, **AWS Secrets Manager** com rotação automática + IAM Roles eliminando chaves fixas, **MFA obrigatório na AWS** (o WordPress já tem MFA TOTP desde 18/11), cópia imutável de backups em S3/Vault Lock cross-region, contas separadas via AWS Organizations + IaC (Terraform) e implantação de Plano de Resposta a Incidentes com exercícios periódicos.

---

## 5. Ativos e Processos Relevantes (Seção 10.1 do Estudo de Caso)

A Seção 10.1 pede a identificação de ativos e processos antes das ameaças. A lista abaixo parte das Seções 1, 2 e 6 do Estudo de Caso e aponta onde cada item fica no ambiente do grupo e quais riscos da matriz v2.1 o cobrem. Ela também serve de ponto de partida para o inventário cobrado no risco **ID 19**.

### Processos de negócio

| Processo | Por que importa | Onde acontece no ambiente | Riscos da matriz |
| :--- | :--- | :--- | :--- |
| Venda online (catálogo, carrinho e fechamento do pedido) | Praticamente todo o faturamento vem do e-commerce | `web-01` (WordPress/WooCommerce) atrás da Cloudflare | 4, 5, 9, 10 |
| Pagamento (iniciar e confirmar transações) | A loja participa do fluxo, mesmo sem guardar número de cartão | Integração com meios de pagamento (não reproduzida no laboratório) | 14, 25 |
| Pós-pedido: separação, emissão fiscal, expedição e atendimento | Uma parada da loja interrompe a operação, não só a TI | Integrações com ERP, estoque, fiscal e transportadoras (não reproduzidas no laboratório) | 23, 25 |
| Administração e mudança da plataforma | Origem dos Incidentes 2 e 3 (conta administrativa e correção direto em produção) | `jump-01` (Guacamole), IAM/SSO, WordPress admin | 1, 2, 11, 12, 13, 20 |
| Backup e recuperação | Backup existia, mas sem teste de restauração | DLM (snapshots EBS) e dump diário do MySQL no `db-01` | 8, 15 |
| Detecção e resposta a incidentes | O Incidente 2 não pôde ser investigado por falta de logs | Wazuh, Zabbix, CloudWatch/SNS e CloudTrail | 16, 17, 22 |

### Ativos de informação e de tecnologia

| Ativo | O que contém | Onde fica | Riscos da matriz |
| :--- | :--- | :--- | :--- |
| Aplicação WooCommerce e plugins | Código da loja e integrações sob medida | `web-01` | 4, 5, 23 |
| Banco de dados | Cadastro, pedidos, produtos, preços e estoque | `db-01` (MySQL, sub-rede privada) | 5, 6, 8, 15 |
| Dados pessoais dos clientes | Nome, endereço, telefone, e-mail e histórico de pedidos (LGPD) | `db-01` | 6, 22 |
| Credenciais de aplicações e integrações | Senha do banco no `wp-config.php`, token da Cloudflare, access key do `wazuh-cloudwatch-reader` | `web-01` e instância de monitoramento | 3 |
| Contas administrativas | Usuários IAM/SSO, Guacamole, WordPress, Wazuh e Zabbix | AWS IAM, `jump-01`, `web-01`, `g3-wazuh-server` | 1, 2, 12, 13 |
| Logs e trilha de auditoria | Eventos de sistema, aplicação e chamadas de API da AWS | Wazuh (`g3-wazuh-server`) e bucket S3 do CloudTrail | 16 |
| Backups | Snapshots EBS e dumps do MySQL | DLM e `/var/backups/mysql` no `db-01` | 8, 15 |
| Domínio e borda | DNS, certificado TLS e regras de WAF de `maisplace.net.br` | Cloudflare | 9, 24 |

*Limite do laboratório: as integrações de pagamento, ERP, estoque, fiscal e transportadoras existem no contexto do caso, mas não foram implantadas. Os riscos 14 e 25 estão na matriz como fora de escopo; o 23 (cadeia de suprimentos) está como parcial, coberto apenas no que se refere aos plugins.*
