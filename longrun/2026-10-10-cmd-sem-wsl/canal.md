# Canal — cmd-sem-wsl (só acrescentar; nunca reescrever)

Conhecimento do projeto que a compactação perde: fatos descobertos, aprendizados, glossário, armadilhas, onde estão as coisas.
Não é estado da tarefa (isso vai em state/plan/progress). Preencha cedo — o hook avisa na faixa 1 (~50% do contexto).

Formato: `- AAAA-MM-DD HH:MM · fato|aprendizado|glossário|armadilha · texto`


## 10/10/2026
- Convenções em `context/cmd-convencoes.md` (ler após compactação).
- Protótipo PT: aulas 13 e 19 reescritas para cmd, auditor 10/10 nas duas.
- Kit do bot (oswork repo, materiais/bot/bot.py): sem chamada Unix; `load_env` usa `read_text()` sem encoding → trocar para `encoding='utf-8-sig'` (Notepad com BOM quebraria a 1ª chave). Fazer no repo oswork no fim.
- "Cmd+V" casa com o termo cmd no auditor: evitar ou pôr gterm.
- Não delegar aulas a subagente (Lesson 06/10); leitor simulado pode.
- PT completo: 13–42+49 no cmd, 43–48 na VPS (tabela na aula 44, alternativa cmd em 45/47/48). Auditor PT 49/49 média 10.0, motor 26/26.
- Arquivos de treino hospedados: materiais/treino{,-en,-es}/ (README.md, AGENTS.md, reuniao.txt, index.html). Pós-tradução: trocar URL /materiais/treino/ → /materiais/treino-en|es/ nos en/es.
- Próximo: leitor simulado (13,19,38,44,49) → traduzir en es → conferir código PT×EN/ES → auditar/motor ×3 → bot.py utf-8-sig no repo oswork → VERSION 1.5.1 → push → portal card 288.
