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
