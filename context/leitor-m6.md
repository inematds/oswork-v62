# Leitor simulado — OSWork v6.2, Módulo 6 (25/09/2026)

Personas: **Regina, 52, coordenadora pedagógica de escola estadual** (chat às vezes) e
**Tatiane, 34, professora de matemática** (ChatGPT todo dia). Capturas do celular (390px), tema papel.

| Aula | Rodada 1 (R · T) | Rodada 2 (R · T) | Rodada 3 (R · T) | Principais correções |
|---|---|---|---|---|
| 31 | 7 · 8 | 8 · 9 | 9 · 9 | "branch" tirado do núcleo; `mkdir -p`/`cd`/`.git` explicados; Git < 2.28 (`unknown switch`), Mac (janela de ferramentas) e WSL no "Se travou"; prática em 3 blocos com um copiar cada |
| 32 | 5 · 7 | 7 · 8 | 8 · 9 | por que o `git diff` vem vazio no corpo do step; cabeçalho do diff ("pule até @@"); promessa sem "já salvo"; linguagem de etapa 1/2/3; exemplo do step 4 com a mesma personagem do terminal; resposta em português; `cd` se fechar o terminal |
| 33 | 6 · 8 | 7 · 9 | 8 · 9 | exemplo de config por pasta corrigido; .gitignore não vale para arquivo já separado/salvo; caso `git add .` → `git rm --cached`; nome/e-mail trocados antes de colar; arquivo oculto |
| 34 | 5 · 7 | 7 · 8 | 8 · 9 | diagrama "caminho direto × divergiu" (legível a 390px, cores na legenda); origin/main e "On branch main" explicados; não rodar merge/rebase "nem se um chat mandar"; cenário da anotação no clone ligado à aula 33 |
| 35 | 6 · 8 | 8 · 9 | 8 · 9 | HEAD como marcador de página; saída real do `git diff` (com linhas de contexto); `git status` antes do bloco 1; caso "local changes would be overwritten"; `--no-edit` explicado; restore = mudanças ainda não separadas |
| 36 | 7 · 8 | 6 · 8 | 7 · 9 → corrigido | push leva todas as versões que o destino não tem; ponto 3 respondido por "up to date / ahead by N"; `--no-pager`; leitura do `show --stat` (+/−, ignorar o código longo, linha "This reverts commit"); e-mail de privacidade do GitHub; "Segredos" só nas versões que iriam; quadro "Só leitura" sem `<code>` (quebrava o flex) |

Pendências da rodada 3 aplicadas (diff com contexto na 35, "Segredos"/linha ausente no status na 36, nota de linha
omitida na 34). Auditoria 10/10 nas seis aulas; motor 26/26.

Aberto (fora do alcance do módulo): o motor põe botão "copiar" também nos terminais de exemplo e copia o bloco
inteiro, com as respostas junto (`curso.js`, linha do "copiar"); a leitora pode colar saída no terminal. Sugestão para o
motor: em `.terminal`, copiar só as linhas com `.pr`. `<code>` dentro de `.psafe` quebra o layout (o `.psafe` é flex) —
usei aspas no lugar. Ainda **não houve teste com pessoas reais** (`TESTE-HUMANO.md` §2).
