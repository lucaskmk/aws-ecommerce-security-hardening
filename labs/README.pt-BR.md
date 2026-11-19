[English](README.md) | **Português**

# Roteiros

Os quatro roteiros de laboratório construíram o ambiente da MaisPlace em etapas, e a atividade de aula analisou acessos e monitoramento sobre o que já existia. Cada etapa partiu do estado deixado pela anterior.

## Roteiro 1 — Webserver e plataforma de segurança (15/09/2026)

**Objetivo:** subir a loja na AWS com banco separado, colocar a Cloudflare na frente e instalar um SIEM.

- Webserver EC2 (t3.micro, Ubuntu) com Apache, PHP, WordPress e certificado via certbot; Security Group com 80/443 só para a lista de prefixos da Cloudflare.
- Banco MySQL em instância própria, em sub-rede privada, sem IP público, com `bind-address` no IP privado e 3306 aceita só do Security Group do webserver.
- Cloudflare como DNS e WAF, com 5 regras: bloqueio geográfico (só Brasil), exploração de plugins, SQL injection, rate limit em `/wp-admin` e bloqueio de `/wp-json/wp/v2/users`.
- Wazuh com detecção de vulnerabilidades, agentes no web e no banco, regra própria para acesso ao `wp-config.php`, FIM em tempo real em `/var/www/html` e ingestão de logs pelo CloudWatch.

**Resultado:** ambiente funcionando atrás da Cloudflare e com visibilidade de segurança. O envio de e-mail do Wazuh ficou registrado como limitação: o `wazuh-maild` não autentica no Gmail.

Relatório: [Relatorio_Roteiro1.pdf](lab-1-infra-waf-siem/Relatorio_Roteiro1.pdf)

## Roteiro 2 — Controle de acesso administrativo e regras automatizadas (07/10/2026)

**Objetivo:** acabar com o SSH exposto, automatizar a resposta a força bruta e impedir que alguém contorne a Cloudflare.

- Apache Guacamole em Docker Compose como jump server, atrás de Nginx, com TOTP obrigatório, allowlist de IP, porta 8080 só no loopback e UFW.
- SSH do webserver liberado apenas a partir do Security Group do Guacamole.
- Fail2ban lendo o IP real do cliente (`mod_remoteip` com `CF-Connecting-IP`): 5 falhas em `/wp-login.php` em 10 minutos geram um bloqueio de 1 hora criado pela API da Cloudflare, com token de escopo mínimo.
- Lista de prefixos gerenciada com os IPs da Cloudflare no Security Group do webserver.

**Resultado:** o ataque simulado a partir de uma rede 4G foi bloqueado na sexta tentativa (HTTP 403 e depois erro 1107 da Cloudflare), e o acesso direto pelo IP do servidor passou a dar tempo esgotado.

Relatório: [Relatorio_Roteiro2.pdf](lab-2-jump-server-fail2ban/Relatorio_Roteiro2.pdf)

## Roteiro 3 — Monitoramento com Amazon CloudWatch

**Objetivo:** criar alarmes sobre o webserver e entregar as notificações ao grupo.

- Tópico SNS `Alertas-CloudWatch`, com uma assinatura de e-mail por integrante.
- `High-CPU-Alarm`: CPU acima de 70% em 5 minutos; testado com `stress` e disparado com média de 99,99%.
- `High-Network-Traffic-Alarm`: NetworkIn acima de 50 MB por minuto, com monitoramento detalhado; testado com download em lote de cerca de 1 GB.
- `High-Disk-Write-Alarm`: escrita no volume acima de 100 MB por minuto; testado com `dd` de 150 MB.
- `System-Status-Check-Alarm`: status check com falha; a seção de teste deste alarme ficou marcada como pendente no relatório.

**Resultado:** nos três alarmes testados, o fluxo completo funcionou: métrica, mudança para ALARM, publicação no SNS e e-mail em cerca de um minuto.

Relatório: [Relatorio_Roteiro3.pdf](lab-3-cloudwatch/Relatorio_Roteiro3.pdf)

## Atividade — Gerenciamento de recursos em nuvem (03/11/2026)

**Objetivo:** analisar quem acessa cada recurso, com que privilégio, e o que deve ser monitorado.

- Tabela de recursos (webserver, banco, Guacamole, Wazuh/Zabbix, token da Cloudflare) com acessos, privilégios, excessos e impacto de comprometimento.
- Análise do comprometimento do Guacamole e do token da Cloudflare.
- Uso de roles e usuários IAM e aplicação do menor privilégio.
- Sinais monitorados por camada (CloudWatch, Zabbix, Wazuh) e um cenário de vazamento de dados: o que teria sido evitado, detectado ou não.

**Resultado:** conclusão de que a rede estava bem fechada, mas as identidades dentro dos recursos (WordPress sem MFA, usuário MySQL com `ALL`, conta compartilhada no Guacamole) ainda tinham privilégio demais. Vários desses pontos entraram na matriz de riscos da entrega final.

Relatório: [Relatorio.pdf](class-activity-resource-management/Relatorio.pdf)

## Roteiro 4 — Operação e gerenciamento com Zabbix (10/11/2026)

**Objetivo:** instalar o Zabbix, monitorar os servidores, configurar alertas e comparar Zabbix e Wazuh.

- Zabbix 7.0 instalado na mesma instância do Wazuh, com swap de 2 GB, MySQL limitado e nginx publicando Zabbix e Wazuh por subdomínio na mesma porta 443, com certificado Let's Encrypt.
- Quatro hosts monitorados (Zabbix server, db-01, jump-01, web-01), com templates de Linux, MySQL e Docker e checagem do Apache e do Guacamole.
- Sete triggers próprias com histerese, testes de CPU e de agente parado e alerta por e-mail com problema e recuperação.
- Comparação Zabbix × Wazuh no incidente real do banco em 06/11/2026 (resumido em [`docs/incident-db01.pt-BR.md`](../docs/incident-db01.pt-BR.md)).

**Resultado:** monitoramento operacional funcionando, com a principal lição do projeto: os alertas existiam, mas ninguém foi avisado e o site ficou fora do ar por horas.

Relatório: [Roteiro4_Relatorio_Final.docx](lab-4-zabbix/report/Roteiro4_Relatorio_Final.docx). O DOCX é gerado por scripts em Python; veja o [README do relatório](lab-4-zabbix/report/README.pt-BR.md). A pasta [`task1-zabbix-https/`](lab-4-zabbix/task1-zabbix-https/) guarda o texto, os prints, as configurações e as medições de recursos da instalação.
