# Falhas — OSWork v6.2

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-10 | Regex que pôs aspas em `%USERPROFILE%` em todo o HTML entrou no JSON dos cartões (aula 19, critério "espinha" reprovou) e puxou pontos finais para dentro das aspas | Restringir a troca a `<pre>/<code>` e validar `json.loads` dos `cards-N` depois de qualquer troca em lote | prompt |
| 2026-10-10 | Tradutor não traduz as respostas de terminal (`span.out`): mensagens do Windows ficaram em PT no EN/ES | `scripts/pos-traducao.py` com as mensagens reais do Windows, rodado depois de cada tradução | infra |
| 2026-10-07 | Tradutor do v6 rejeitou 4× (EN e ES) o parágrafo do gh auth login com "&gt;" e "↑↓"; ficou em PT sem erro visível | Conferir sobras de PT na aula depois de traduzir; traduzir a unidade de `*-faltando.json` no cache e rodar `--so-montar` | infra |
| 2026-09-25 | traduzir-curso.py abortou o EN: 1 parágrafo com 2 `.gterm` (aula 35) rejeitado 4 rodadas, nada gravado | tradução manual do trecho no cache `i18n/en.json` + rerodar; proteção sugerida: gravar o resto e listar o que faltou em vez de `sys.exit` | infra |
| 2026-09-25 | aula 6 caiu para 9/10 (Work/Desktop sem `.gterm` no gancho) ao remontar com os módulos novos | `.gterm` nos dois termos do `.na-hook` | prompt |
