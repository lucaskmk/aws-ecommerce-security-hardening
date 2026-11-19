"""Textos em inglês da apresentação, usados por `gerar_apresentacao.py --lang en`.

Cada chave é o texto exato em português do script; o valor é a tradução. Se um texto em
português mudar no script, atualize a chave aqui: o script para e lista o que ficou sem tradução.
"""

EN = {
    'MaisPlace: migração segura do e-commerce para a AWS':
        'MaisPlace: secure migration of the e-commerce store to AWS',
    'Fonte: Estudo de caso MaisPlace 2026-2, seções 1 a 5':
        'Source: MaisPlace case study 2026-2, sections 1 to 5',
    'A MaisPlace depende da loja online para vender e processar pedidos. O estudo de caso traz três incidentes que explicam a migração: a loja fora do ar por cerca de duas horas em uma campanha, sem causa identificada; o uso de uma conta administrativa de madrugada, sem autor e com poucos logs; e uma atualização que afetou pedidos e foi corrigida direto em produção. A diretoria discutiu se, na AWS, a segurança deixaria de ser responsabilidade da empresa. Não deixa: a AWS responde pelo datacenter, pelo hardware e pela virtualização; conta administrativa roubada, aplicação explorada e dados de clientes continuam com a MaisPlace. Por isso a análise de riscos veio antes da migração. Nosso objetivo foi reconstruir a loja na AWS com um controle para cada risco alto, mostrar a evidência de que funciona e dizer o que ainda falta.':
        "MaisPlace depends on its online store to sell and process orders. The case study describes three incidents that explain the migration: the store was down for about two hours during a campaign, with no identified cause; an administrative account was used in the middle of the night, with no known author and few logs; and an update affected orders and was fixed directly in production. The board discussed whether, on AWS, security would stop being the company's responsibility. It does not: AWS is responsible for the datacenter, the hardware and the virtualization; a stolen administrative account, an exploited application and customer data remain with MaisPlace. That is why the risk analysis came before the migration. Our goal was to rebuild the store on AWS with a control for each high risk, show the evidence that it works and state what is still missing.",
    'Avaliação final · Cibersegurança em Nuvem · Prof. Dr. Rodolfo Avelino':
        'Final assessment · Cloud Cybersecurity · Prof. Dr. Rodolfo Avelino',
    'Grupo 3 · Eduardo · Gustavo · Henrique · Lucas · Sidney':
        'Group 3 · Eduardo · Gustavo · Henrique · Lucas · Sidney',
    'Três incidentes motivaram a migração':
        'Three incidents drove the migration',
    'Indisponibilidade':
        'Downtime',
    'Loja fora do ar por cerca de duas horas durante campanha promocional. A causa não foi determinada.':
        'Store down for about two hours during a promotional campaign. The cause was not determined.',
    'Conta administrativa':
        'Administrative account',
    'Conta privilegiada usada de madrugada, sem autor identificado e com poucos logs para investigar.':
        'Privileged account used in the middle of the night, with no identified author and few logs to investigate.',
    'Mudança em produção':
        'Change in production',
    'Atualização prejudicou pedidos e foi corrigida direto em produção, em horário comercial.':
        'An update harmed orders and was fixed directly in production, during business hours.',
    'Responsabilidade compartilhada  ':
        'Shared responsibility  ',
    'A AWS protege datacenter, hardware e virtualização. Contas, sistema operacional, aplicação, dados e regras de rede continuam com a MaisPlace: migrar não transfere esses riscos.':
        'AWS protects the datacenter, hardware and virtualization. Accounts, operating system, application, data and network rules remain with MaisPlace: migrating does not transfer these risks.',
    'Objetivo  ':
        'Goal  ',
    'Reconstruir a loja na AWS com um controle para cada risco alto da matriz, evidência de que cada controle funciona e registro claro dos riscos que permanecem.':
        'Rebuild the store on AWS with a control for each high risk in the matrix, evidence that each control works and a clear record of the risks that remain.',
    'Seis ameaças e o que cada uma custa ao negócio':
        'Six threats and what each one costs the business',
    'Fontes: Estudo de caso MaisPlace 2026-2, seções 4, 7 e 8; matriz v2.2 (riscos 18, 20, 21 e 23)':
        'Sources: MaisPlace case study 2026-2, sections 4, 7 and 8; matrix v2.2 (risks 18, 20, 21 and 23)',
    'Partimos das seis classes de ameaça do estudo de caso: insider, malware, negação de serviço, ataques à aplicação web, comprometimento de credenciais e comprometimento de informações. Para cada uma mostramos como ela aparece na MaisPlace e o que custa ao negócio: venda perdida, perda de rastreabilidade, exposição de dados de clientes. Revisamos o levantamento, como o caso pede: as seis continuam relevantes e acrescentamos ameaças que ganham peso na nuvem, como erro de configuração, leitura errada da responsabilidade compartilhada, cadeia de suprimentos de plugins e phishing. No total, a matriz tem 25 riscos.':
        'We started from the six threat classes in the case study: insider, malware, denial of service, web application attacks, credential compromise and information compromise. For each one we show how it shows up at MaisPlace and what it costs the business: lost sales, loss of traceability, exposure of customer data. We reviewed the assessment, as the case asks: all six remain relevant, and we added threats that weigh more in the cloud, such as misconfiguration, misreading the shared responsibility model, the plugin supply chain and phishing. In total, the matrix has 25 risks.',
    'Insider':
        'Insider',
    'Conta administrativa compartilhada, usada de madrugada sem autor identificado.':
        'Shared administrative account, used in the middle of the night with no identified author.',
    'Impacto: ':
        'Impact: ',
    'ações sem responsável':
        'actions with no owner',
    'Malware e ransomware':
        'Malware and ransomware',
    'Sem gestão de vulnerabilidades e com backup nunca restaurado em teste.':
        'No vulnerability management, and a backup never restored in a test.',
    'parada prolongada da loja':
        'prolonged store outage',
    'Negação de serviço':
        'Denial of service',
    'Loja fora do ar por cerca de duas horas em plena campanha promocional.':
        'Store down for about two hours in the middle of a promotional campaign.',
    'vendas perdidas':
        'lost sales',
    'Ataques à aplicação web':
        'Web application attacks',
    'Plugins do WooCommerce sem rotina de atualização; injeção de SQL.':
        'WooCommerce plugins with no update routine; SQL injection.',
    'pedidos e cadastro expostos':
        'orders and records exposed',
    'Comprometimento de credenciais':
        'Credential compromise',
    'Acesso administrativo sem MFA e credenciais guardadas em arquivos.':
        'Administrative access without MFA and credentials stored in files.',
    'controle da loja por terceiros':
        'store controlled by third parties',
    'Comprometimento de informações':
        'Information compromise',
    'Dados pessoais de clientes em banco pouco isolado da aplicação.':
        'Customer personal data in a database poorly isolated from the application.',
    'LGPD e reputação':
        'LGPD and reputation',
    'Além das seis: ':
        'Beyond the six: ',
    'a matriz inclui ameaças que ganham peso na nuvem, como erro de configuração, leitura errada da responsabilidade compartilhada, cadeia de suprimentos (plugins) e phishing. São 25 riscos, cada um com probabilidade, impacto e controle.':
        'the matrix includes threats that weigh more in the cloud, such as misconfiguration, misreading the shared responsibility model, the supply chain (plugins) and phishing. There are 25 risks, each with likelihood, impact and control.',
    'Vulnerabilidades do legado e CVEs encontradas pelo Wazuh':
        'Legacy vulnerabilities and CVEs found by Wazuh',
    'Fontes: Estudo de caso, seção 8; Relatório do Roteiro 1 (print 17, Wazuh Vulnerability Detection)':
        'Sources: case study, section 8; Lab 1 report (screenshot 17, Wazuh Vulnerability Detection)',
    'O ambiente anterior tinha contas compartilhadas sem MFA, administração remota sem padrão, rede pouco segmentada, nenhuma gestão de vulnerabilidades, logs dispersos e backup sem teste. No Roteiro 1 ligamos a detecção de vulnerabilidades do Wazuh nos dois servidores e ela mostrou 403 CVEs críticas e 1.562 altas, concentradas no pacote linux-aws, o kernel do Ubuntu. Esse é o retrato inicial: sem rotina de atualização, a exposição se acumula.':
        'The previous environment had shared accounts without MFA, no standard for remote administration, a poorly segmented network, no vulnerability management, scattered logs and untested backups. In Lab 1 we enabled Wazuh vulnerability detection on both servers and it showed 403 critical and 1,562 high CVEs, concentrated in the linux-aws package, the Ubuntu kernel. This is the starting picture: without an update routine, exposure accumulates.',
    'Fragilidades do ambiente anterior':
        'Weaknesses of the previous environment',
    'Contas compartilhadas e privilegiadas, sem MFA':
        'Shared and privileged accounts, without MFA',
    'Administração remota sem padrão; credenciais em arquivos':
        'No standard for remote administration; credentials in files',
    'Rede pouco segmentada entre aplicação e banco':
        'Poorly segmented network between application and database',
    'Sem gestão de vulnerabilidades (plugins e sistema)':
        'No vulnerability management (plugins and system)',
    'Logs dispersos; monitoramento só de disponibilidade':
        'Scattered logs; availability-only monitoring',
    'Backup sem teste de restauração':
        'Backup without a restore test',
    'Wazuh Vulnerability Detection (Roteiro 1). ':
        'Wazuh Vulnerability Detection (Lab 1). ',
    'CVEs por severidade em web-server e db-server.':
        'CVEs by severity on web-server and db-server.',
    'O que o print mostra':
        'What the screenshot shows',
    '403 CVEs críticas e 1.562 altas nos dois servidores, concentradas no pacote linux-aws (kernel do Ubuntu). É o retrato inicial: sem rotina de atualização, a exposição se acumula.':
        '403 critical and 1,562 high CVEs on the two servers, concentrated in the linux-aws package (Ubuntu kernel). This is the starting picture: without an update routine, exposure accumulates.',
    'Matriz de risco: 25 cenários, de 8 extremos para 1':
        'Risk matrix: 25 scenarios, from 8 extreme to 1',
    'Fonte: Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.xlsx (v2.2, revisão de 19/11/2026)':
        'Source: Matriz_AmeacasRiscos_MaisPlaceGrupo3_v2.xlsx (v2.2, revised 2026-11-19)',
    'A matriz avalia 25 riscos por probabilidade e impacto, em escala de 1 a 4. Na classificação original, do ambiente legado, 8 são extremos e 14 altos. Depois dos controles implementados, resta 1 extremo e ficam 14 altos. O último a cair foi o de ataques web a plugins, depois do WordPress atualizado e do scan final sem alertas altos. Cada linha traz o controle CIS v8, o que foi implementado e a evidência. As notas residuais são avaliação do grupo.':
        "The matrix rates 25 risks by likelihood and impact, on a scale of 1 to 4. In the original rating, of the legacy environment, 8 are extreme and 14 high. After the implemented controls, 1 extreme remains and 14 are high. The last one to drop was web attacks on plugins, after WordPress was updated and the final scan found no high alerts. Each row has the CIS v8 control, what was implemented and the evidence. The residual scores are the group's assessment.",
    'Original (legado)':
        'Original (legacy)',
    '8 extremos · 14 altos · 3 moderados':
        '8 extreme · 14 high · 3 moderate',
    'Residual (AWS)':
        'Residual (AWS)',
    '1 extremo · 14 altos · 10 moderados':
        '1 extreme · 14 high · 10 moderate',
    'Como ler':
        'How to read it',
    'Probabilidade × impacto, de 1 a 4. Cada risco tem controle CIS v8, implementação e evidência.':
        'Likelihood × impact, from 1 to 4. Each risk has a CIS v8 control, implementation and evidence.',
    'Riscos altos e mitigação: antes × depois':
        'High risks and mitigation: before × after',
    'Fonte: docs/risk-traceability.pt-BR.md, seções 2 e 3; notas da matriz v2.2':
        'Source: docs/risk-traceability.md, sections 2 and 3; matrix v2.2 scores',
    'Este quadro resume o que mudou em cinco frentes. O perímetro ganhou Cloudflare com WAF e Fail2ban. O banco foi para sub-rede privada. O acesso administrativo passou a exigir o Guacamole com TOTP, e o WordPress tem MFA. Os logs chegam ao Wazuh, ao Zabbix, ao CloudWatch e ao CloudTrail. Os backups são diários e a restauração do banco foi testada. A coluna de risco mostra a nota de um risco representativo antes e depois.':
        'This table summarizes what changed on five fronts. The perimeter gained Cloudflare with WAF and Fail2ban. The database moved to a private subnet. Administrative access now requires Guacamole with TOTP, and WordPress has MFA. Logs reach Wazuh, Zabbix, CloudWatch and CloudTrail. Backups are daily and the database restore was tested. The risk column shows the score of a representative risk before and after.',
    'Frente':
        'Front',
    'Antes (legado)':
        'Before (legacy)',
    'Depois (AWS, Grupo 3)':
        'After (AWS, Group 3)',
    'Risco':
        'Risk',
    'Impacto no negócio':
        'Business impact',
    'Perímetro e aplicação':
        'Perimeter and application',
    'Servidor exposto direto à internet, sem WAF.':
        'Server exposed directly to the internet, no WAF.',
    'Cloudflare como proxy e WAF (5 regras), Fail2ban e origem oculta.':
        'Cloudflare as proxy and WAF (5 rules), Fail2ban and hidden origin.',
    'ID 4\n16 → 8':
        'ID 4\n16 → 8',
    'Loja protegida contra ataques web e DoS em campanha.':
        'Store protected against web attacks and DoS during campaigns.',
    'Dados (LGPD)':
        'Data (LGPD)',
    'Aplicação e banco na mesma rede, com poucas restrições.':
        'Application and database on the same network, with few restrictions.',
    'MySQL em sub-rede privada, sem IP público; porta 3306 só do webserver.':
        'MySQL in a private subnet, no public IP; port 3306 only from the webserver.',
    'ID 6\n12 → 8':
        'ID 6\n12 → 8',
    'Menor chance de vazamento da base de clientes.':
        'Lower chance of a customer database leak.',
    'Acesso administrativo':
        'Administrative access',
    'Contas compartilhadas, sem MFA e sem padrão de acesso remoto.':
        'Shared accounts, no MFA and no standard for remote access.',
    'SSH público fechado; Guacamole com TOTP e allowlist; IAM nominal; MFA no WordPress.':
        'Public SSH closed; Guacamole with TOTP and allowlist; named IAM; MFA on WordPress.',
    'ID 1\n16 → 8':
        'ID 1\n16 → 8',
    'Cada ação tem autor; força bruta não alcança os servidores.':
        'Every action has an author; brute force does not reach the servers.',
    'Visibilidade':
        'Visibility',
    'Logs dispersos; monitoramento só de “ligado ou não”.':
        'Scattered logs; monitoring only of “up or down”.',
    'Wazuh (3 agentes), Zabbix (4 hosts), CloudWatch/SNS e CloudTrail.':
        'Wazuh (3 agents), Zabbix (4 hosts), CloudWatch/SNS and CloudTrail.',
    'ID 16\n12 → 6':
        'ID 16\n12 → 6',
    'Incidente investigável: efeito e causa do caso db-01.':
        'Investigable incident: effect and cause of the db-01 case.',
    'Continuidade':
        'Continuity',
    'Backup sem teste de restauração.':
        'Backup without a restore test.',
    'Snapshots diários (DLM, 7 dias) e dump do MySQL com restauração testada.':
        'Daily snapshots (DLM, 7 days) and MySQL dump with a tested restore.',
    'ID 15\n8 → 4':
        'ID 15\n8 → 4',
    'Recuperação da loja comprovada, não presumida.':
        'Store recovery proven, not assumed.',
    'Nota de risco = probabilidade × impacto (1 a 16). A rastreabilidade completa dos riscos altos está no documento de rastreabilidade.':
        'Risk score = likelihood × impact (1 to 16). Full traceability of the high risks is in the traceability document.',
    'Arquitetura na AWS: só os fluxos necessários':
        'Architecture on AWS: only the necessary flows',
    'Fonte: docs/architecture.pt-BR.md e diagrama do grupo (figuras/03_diagrama_arquitetura_aws)':
        "Source: docs/architecture.md and the group's diagram (figuras/en/03_architecture_diagram_aws)",
    'A Cloudflare recebe o tráfego da loja e só ela alcança o webserver nas portas 80 e 443. O webserver fala com o banco, que fica em sub-rede privada e sem IP público, apenas na 3306. A administração entra pelo jump server com Guacamole. Wazuh e Zabbix ficam na instância de monitoramento. Os Security Groups se referenciam por função, então cada servidor só aceita o que precisa.':
        "Cloudflare receives the store's traffic and only Cloudflare reaches the webserver on ports 80 and 443. The webserver talks to the database, which sits in a private subnet with no public IP, only on 3306. Administration comes in through the jump server with Guacamole. Wazuh and Zabbix run on the monitoring instance. The Security Groups reference each other by role, so each server only accepts what it needs.",
    'Evidências: rede, WAF e acesso administrativo':
        'Evidence: network, WAF and administrative access',
    'Fontes: evidencias_aws (capturas de 18/11/2026) e evidencias_novas':
        'Sources: evidencias_aws (screenshots from 2026-11-18) and evidencias_novas',
    'Os Security Groups mostram o menor privilégio de rede: o webserver só recebe 80 e 443 da lista de prefixos da Cloudflare e SSH só do Guacamole; o banco só recebe 3306 do webserver. O WAF bloqueou nosso teste de excesso de requisições em /wp-admin com o erro 1015. O acesso administrativo passa pelo Guacamole com TOTP e allowlist de IP.':
        'The Security Groups show network least privilege: the webserver only receives 80 and 443 from the Cloudflare prefix list and SSH only from Guacamole; the database only receives 3306 from the webserver. The WAF blocked our excessive-requests test on /wp-admin with error 1015. Administrative access goes through Guacamole with TOTP and an IP allowlist.',
    'SG do webserver. ':
        'Webserver SG. ',
    '80/443 só da lista de prefixos da Cloudflare; 22 só do SG do Guacamole; 10050 só do Zabbix (18/11/2026).':
        '80/443 only from the Cloudflare prefix list; 22 only from the Guacamole SG; 10050 only from Zabbix (2026-11-18).',
    'SG do banco. ':
        'Database SG. ',
    '3306 só do SG do webserver; nenhuma regra aberta para a internet (18/11/2026).':
        '3306 only from the webserver SG; no rule open to the internet (2026-11-18).',
    'WAF. ':
        'WAF. ',
    'Rate limit em /wp-admin: erro 1015 da Cloudflare (18/11/2026).':
        'Rate limit on /wp-admin: Cloudflare error 1015 (2026-11-18).',
    'Fail2ban. ':
        'Fail2ban. ',
    '5 falhas de login geram bloqueio de 1 hora na Cloudflare.':
        '5 failed logins trigger a 1-hour block on Cloudflare.',
    'Guacamole. ':
        'Guacamole. ',
    'Jump server com TOTP obrigatório e allowlist de IP.':
        'Jump server with mandatory TOTP and IP allowlist.',
    'VPN. ':
        'VPN. ',
    'OpenVPN com apenas UDP 1194 aberta.':
        'OpenVPN with only UDP 1194 open.',
    'SSH fechado para a internet; administração só pelo Guacamole (TOTP e allowlist), por dentro da VPN.':
        'SSH closed to the internet; administration only through Guacamole (TOTP and allowlist), inside the VPN.',
    'Evidências: monitoramento mostrou efeito e causa no db-01':
        'Evidence: monitoring showed effect and cause on db-01',
    'Fontes: Relatório do Roteiro 4 (capturas de 06 e 10/11/2026), Roteiro 3 e evidencias_novas':
        'Sources: Lab 4 report (screenshots from Nov 6 and 10, 2026), Lab 3 and evidencias_novas',
    'O caso do db-01 mostrou a diferença entre a instância estar ligada e a loja funcionar. O status check da AWS continuou normal enquanto o MySQL travou e a loja deu erro de banco. O Zabbix registrou o efeito, com indisponibilidade e métricas congeladas, e o Wazuh guardou os eventos do servidor que ajudaram a chegar à causa. O alerta por e-mail do Zabbix foi testado. Por isso monitoramos serviço e aplicação, além da instância.':
        'The db-01 case showed the difference between the instance being up and the store working. The AWS status check stayed normal while MySQL hung and the store returned a database error. Zabbix recorded the effect, with unavailability and frozen metrics, and Wazuh kept the server events that helped reach the cause. Zabbix e-mail alerting was tested. That is why we monitor the service and the application, not just the instance.',
    'Zabbix. ':
        'Zabbix. ',
    '4 hosts monitorados e disponíveis: db-01, jump-01, web-01 e o próprio servidor.':
        '4 hosts monitored and available: db-01, jump-01, web-01 and the server itself.',
    'Alerta por e-mail. ':
        'E-mail alert. ',
    'Problema de CPU e resolução notificados pelo Zabbix (10/11/2026).':
        'CPU problem and resolution notified by Zabbix (2026-11-10).',
    'Wazuh. ':
        'Wazuh. ',
    'Agentes do web-01, db-01 e jump-01 ativos; FIM, SCA e detecção de vulnerabilidades.':
        'Agents on web-01, db-01 and jump-01 active; FIM, SCA and vulnerability detection.',
    'Wazuh, incidente do db-01. ':
        'Wazuh, db-01 incident. ',
    'Eventos do db-server na madrugada de 06/11/2026, até o agente desconectar.':
        'db-server events in the early hours of 2026-11-06, until the agent disconnected.',
    'O que o incidente ensinou':
        'What the incident taught us',
    'O status check da EC2 seguiu “ok” com o MySQL travado e a loja fora do ar. O Zabbix mostrou o efeito; o Wazuh, os eventos que levaram à causa.':
        'The EC2 status check stayed “ok” with MySQL hung and the store down. Zabbix showed the effect; Wazuh, the events that led to the cause.',
    'Também ativos: CloudWatch com 4 alarmes e SNS para os 5 integrantes; Fail2ban integrado à Cloudflare; WAF com 5 regras.':
        'Also active: CloudWatch with 4 alarms and SNS to the 5 members; Fail2ban integrated with Cloudflare; WAF with 5 rules.',
    'Scan externo: nenhum alerta alto na superfície pública':
        'External scan: no high alerts on the public surface',
    'Fonte: external-scan/report-2026-11-19.pt-BR.md (scan final) e report-2026-11-18.pt-BR.md; OWASP ZAP Baseline 2.17.0':
        'Source: external-scan/report-2026-11-19.md (final scan) and report-2026-11-18.pt-BR.md; OWASP ZAP Baseline 2.17.0',
    'Antes do scan final atualizamos o WordPress para a 7.1.5, aplicamos os pacotes de segurança nos dois servidores e reiniciamos o servidor web para ativar o kernel corrigido. Depois rodamos de novo o OWASP ZAP em modo baseline contra a loja, de fora. O relatório registrou zero alertas altos, sete médios, dez baixos e dez informativos; o alerta de clickjacking sumiu com os novos cabeçalhos. O scan é passivo, sem login e passa pela Cloudflare, então não cobre rotas autenticadas nem o servidor de origem; por dentro, conferimos versões e integridade dos arquivos. Os médios que restam são a falta de CSP, avisos automáticos de token anti-CSRF e a biblioteca moment.js do próprio WordPress.':
        'Before the final scan we updated WordPress to 7.1.5, applied the security packages on both servers and rebooted the web server to activate the patched kernel. Then we ran OWASP ZAP again in baseline mode against the store, from outside. The report recorded zero high alerts, seven medium, ten low and ten informational; the clickjacking alert disappeared with the new headers. The scan is passive, unauthenticated and goes through Cloudflare, so it does not cover authenticated routes or the origin server; from the inside, we checked versions and file integrity. The remaining medium alerts are the missing CSP, automated anti-CSRF token warnings and the moment.js library bundled with WordPress.',
    'OWASP ZAP Baseline. ':
        'OWASP ZAP Baseline. ',
    'Resumo do relatório gerado em 19/11/2026 04:35 UTC para https://maisplace.net.br, depois das correções.':
        'Summary of the report generated on 2026-11-19 04:35 UTC for https://maisplace.net.br, after the fixes.',
    'Resultado':
        'Result',
    '0 altos · 7 médios · 10 baixos · 10 informativos. Em 18/11 eram 8 médios.':
        '0 high · 7 medium · 10 low · 10 informational. On Nov 18 there were 8 medium.',
    'Limite':
        'Limit',
    'Scan passivo, sem login e através da Cloudflare. Não cobre rotas autenticadas nem o servidor de origem.':
        'Passive scan, unauthenticated and through Cloudflare. Does not cover authenticated routes or the origin server.',
    'Correções antes do scan':
        'Fixes before the scan',
    'WordPress 7.1.5, pacotes de segurança, kernel novo em uso e cabeçalhos no Apache. Restam CSP e os cabeçalhos na borda da Cloudflare.':
        'WordPress 7.1.5, security packages, new kernel in use and headers in Apache. CSP and the headers at the Cloudflare edge remain.',
    'Políticas e boas práticas: identidade, auditoria e backup':
        'Policies and good practices: identity, audit and backup',
    'Fontes: evidencias_aws (capturas de 18/11/2026, recortadas); docs/architecture.pt-BR.md, seção 3':
        'Sources: evidencias_aws (screenshots from 2026-11-18, cropped); docs/architecture.md, section 3',
    'Em identidade, cada integrante tem usuário IAM próprio, com acesso por SSO e política de senha de 14 caracteres, 90 dias e sem reuso. O CloudTrail registra todas as chamadas de API, em todas as regiões, com validação de integridade. Os backups são snapshots diários por DLM e dump do MySQL, e a restauração foi testada em 17 de novembro. Na aplicação, o WordPress tem MFA. Ficam como riscos aceitos a console AWS sem MFA e os volumes sem criptografia.':
        'For identity, each member has their own IAM user, with SSO access and a password policy of 14 characters, 90 days and no reuse. CloudTrail records every API call, in all regions, with integrity validation. Backups are daily DLM snapshots and a MySQL dump, and the restore was tested on November 17. In the application, WordPress has MFA. The AWS console without MFA and the unencrypted volumes remain as accepted risks.',
    'Identidade nominal':
        'Named identity',
    '5 usuários IAM individuais, acesso por SSO e política de senha: 14+ caracteres, 90 dias, sem reuso.':
        '5 individual IAM users, SSO access and password policy: 14+ characters, 90 days, no reuse.',
    'Auditoria':
        'Audit',
    'CloudTrail em todas as regiões, com validação de integridade e logs em bucket S3 privado.':
        'CloudTrail in all regions, with integrity validation and logs in a private S3 bucket.',
    'Backup testado':
        'Tested backup',
    'Snapshots diários por DLM (retenção de 7) e dump do MySQL; restauração conferida em 17/11.':
        'Daily DLM snapshots (retention of 7) and MySQL dump; restore checked on Nov 17.',
    'Hardening da aplicação':
        'Application hardening',
    'MFA TOTP no WordPress; token da Cloudflare com escopo mínimo; UFW no jump server.':
        'TOTP MFA on WordPress; Cloudflare token with minimal scope; UFW on the jump server.',
    'Riscos aceitos e registrados na matriz: ':
        'Accepted risks recorded in the matrix: ',
    'console AWS sem MFA (laboratório) e volumes EBS sem criptografia.':
        'AWS console without MFA (lab) and unencrypted EBS volumes.',
    'Impacto: menos risco extremo, mais continuidade da loja':
        'Impact: less extreme risk, more store continuity',
    'Fonte: Matriz v2.2 e docs/risk-traceability.pt-BR.md (revisão de 19/11/2026)':
        'Source: matrix v2.2 and docs/risk-traceability.md (revised 2026-11-19)',
    'Na matriz, os riscos extremos caíram de 8 para 1, redução de 87,5%. Somando extremos e altos, fomos de 22 para 15. Para o negócio isso significa loja disponível em campanha, dados de clientes isolados, ações administrativas com autor e recuperação testada. Esses números são uma avaliação estruturada do grupo, não uma medição de ataques evitados.':
        'In the matrix, extreme risks dropped from 8 to 1, an 87.5% reduction. Adding extreme and high, we went from 22 to 15. For the business this means a store available during campaigns, isolated customer data, administrative actions with an author and a tested recovery. These numbers are a structured assessment by the group, not a measurement of prevented attacks.',
    'Riscos extremos':
        'Extreme risks',
    'Extremos + altos':
        'Extreme + high',
    'Para o negócio':
        'For the business',
    '• Loja disponível em campanha':
        '• Store available during campaigns',
    '• Dados de clientes isolados (LGPD)':
        '• Customer data isolated (LGPD)',
    '• Cada ação administrativa com autor':
        '• Every administrative action has an author',
    '• Recuperação testada, não presumida':
        '• Recovery tested, not assumed',
    'Notas são avaliação do grupo, não medição de ataques evitados.':
        'Scores are a group assessment, not a count of prevented attacks.',
    'Conclusão, riscos residuais e próximos passos':
        'Conclusion, residual risks and next steps',
    'Fonte: Matriz v2.2 e docs/risk-traceability.pt-BR.md (seção 4)':
        'Source: matrix v2.2 and docs/risk-traceability.md (section 4)',
    'Entregamos a loja na AWS com banco isolado, WAF, administração por jump server com MFA, monitoramento e SIEM, e backup com restauração testada. Permanece um risco extremo, o de segredos de aplicação e integrações, além de lacunas de laboratório como a console AWS sem MFA e a falta de escala automática. Os próximos passos são treinamento, revisão periódica da matriz e dos acessos, e automação com infraestrutura como código e rotação de segredos.':
        'We delivered the store on AWS with an isolated database, WAF, administration through a jump server with MFA, monitoring and SIEM, and backup with a tested restore. One extreme risk remains, application and integration secrets, plus lab gaps such as the AWS console without MFA and the lack of automatic scaling. The next steps are training, periodic review of the matrix and of access, and automation with infrastructure as code and secret rotation.',
    'O que foi entregue':
        'What was delivered',
    '• Loja na AWS com banco em sub-rede privada':
        '• Store on AWS with the database in a private subnet',
    '• Cloudflare com WAF (5 regras) e Fail2ban':
        '• Cloudflare with WAF (5 rules) and Fail2ban',
    '• Administração por jump server com TOTP':
        '• Administration through a jump server with TOTP',
    '• Wazuh, Zabbix, CloudWatch e CloudTrail':
        '• Wazuh, Zabbix, CloudWatch and CloudTrail',
    '• Backup diário com restauração testada':
        '• Daily backup with a tested restore',
    'Riscos que permanecem':
        'Risks that remain',
    '• 1 extremo: segredos de aplicação e integrações':
        '• 1 extreme: application and integration secrets',
    '• Console AWS sem MFA (aceito em laboratório)':
        '• AWS console without MFA (accepted in the lab)',
    '• Volumes EBS sem criptografia':
        '• Unencrypted EBS volumes',
    '• Sem Auto Scaling nem Multi-AZ para campanhas':
        '• No Auto Scaling or Multi-AZ for campaigns',
    'Próximos passos':
        'Next steps',
    'Treinamento: ':
        'Training: ',
    'conscientização contra phishing e exercício de resposta a incidentes.':
        'phishing awareness and incident response exercise.',
    'Revisão periódica: ':
        'Periodic review: ',
    'matriz, Security Groups e acessos a cada trimestre; scan recorrente.':
        'matrix, Security Groups and access every quarter; recurring scan.',
    'Automação: ':
        'Automation: ',
    'infraestrutura como código, rotação de segredos e atualização de pacotes.':
        'infrastructure as code, secret rotation and package updates.',
    'Capacidade: ':
        'Capacity: ',
    'RDS Multi-AZ e Auto Scaling para campanhas.':
        'RDS Multi-AZ and Auto Scaling for campaigns.',
    'A matriz liga cada risco a controle, evidência e risco residual; o que não foi implementado está registrado como plano.':
        'The matrix links each risk to a control, evidence and residual risk; what was not implemented is recorded as a plan.',
    'PRINT PENDENTE':
        'SCREENSHOT PENDING',
    'Wazuh: 3 agentes ativos e alertas recentes':
        'Wazuh: 3 active agents and recent alerts',
    'Zabbix: 4 hosts disponíveis':
        'Zabbix: 4 hosts available',
    'Cloudflare: eventos do WAF com requisições bloqueadas':
        'Cloudflare: WAF events with blocked requests',
    'Fail2ban: IP banido (log + regra na Cloudflare)':
        'Fail2ban: banned IP (log + rule on Cloudflare)',
    'Guacamole: login pedindo o código TOTP':
        'Guacamole: login asking for the TOTP code',
    'VPN: túnel OpenVPN ativo e SG só com UDP 1194':
        'VPN: active OpenVPN tunnel and SG with only UDP 1194',
    'Resumo do scan final, depois das correções':
        'Summary of the final scan, after the fixes',
    'Ainda não implantada; requisito em aberto.':
        'Not deployed yet; open requirement.',
    'SSH fechado para a internet; administração só pelo Guacamole (TOTP e allowlist). VPN OpenVPN ainda não implantada.':
        'SSH closed to the internet; administration only through Guacamole (TOTP and allowlist). OpenVPN not deployed yet.',
    '• VPN (OpenVPN) ainda não implantada':
        '• VPN (OpenVPN) not deployed yet',
}
