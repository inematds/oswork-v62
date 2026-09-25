# Falhas — OSWork v6.2

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-25 | traduzir-curso.py abortou o EN: 1 parágrafo com 2 `.gterm` (aula 35) rejeitado 4 rodadas, nada gravado | tradução manual do trecho no cache `i18n/en.json` + rerodar; proteção sugerida: gravar o resto e listar o que faltou em vez de `sys.exit` | infra |
| 2026-09-25 | aula 6 caiu para 9/10 (Work/Desktop sem `.gterm` no gancho) ao remontar com os módulos novos | `.gterm` nos dois termos do `.na-hook` | prompt |
