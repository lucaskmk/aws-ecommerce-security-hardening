**English** | [Português](README.pt-BR.md)

# Lab 4: final delivery

`Roteiro4_Relatorio_Final.docx` is the delivered document (4 tasks, 18 answers, 39 figures). The report is in Portuguese; the English summary of Lab 4 is in [`labs/README.md`](../../README.md).

## How to regenerate the DOCX

The text lives in the scripts. To change the report, edit them and run in this folder:

```bash
pip install -r requirements.txt    # python-docx
python build.py Roteiro4_Relatorio_Final.docx
```

- `build.py`: cover, Tasks 2 to 4 and conclusions.
- `t1_section.py`: Task 1, from `../task1-zabbix-https/`.
- `t3_testes.py`: results of the alert tests.
- `evidencias_sidney/` and `evidencias_lucas/`: figures used in the document.

## Environment state on 2026-11-10

| Item | Status |
|---|---|
| Hosts in Zabbix | Zabbix server, db-01, jump-01 and web-01, all available |
| web-01 | Template Linux by Zabbix agent active, with custom Apache items |
| Dashboard | "G3 - Visao geral (Roteiro 4)" |
| Group triggers | Tag `grupo = G3-roteiro4` |
| E-mail | Email media type and "Report problems to Zabbix administrators" action enabled |

## Points of attention

- db-01 has 1 GB of RAM, no swap, and has already hung several times. If the site shows a database error, restart the instance.
- Access to the interfaces depends on your IP being in the 443 and 22 rules of the `g3-sc-wazuh` Security Group.
- Passwords and keys must not be added to this repository.
