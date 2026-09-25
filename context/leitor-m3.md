# Leitor simulado — OSWork v6.2, Módulo 3 (25/09/2026)

Personas: **Regina, 52, coordenadora pedagógica de escola estadual** (chat às vezes, plano gratuito; notebook Windows da
escola e um próprio) e **Tatiane, 34, professora de matemática** (ChatGPT quase todo dia; MacBook). Capturas do celular
(390px), tema papel. Notas: Regina Windows/Mac · Tatiane Mac.

| Aula | Rodada 1 (R · T) | Rodada 2 (R · T) | Rodada 3 (R · T) | Principais correções |
|---|---|---|---|---|
| 13 | 6 · 8 | 7 · 9 | 8/9 · 9 | `%` do Mac; nomes em inglês no `ls`; Cmd+Espaço; "variação do Bash" no Mac; quadro "Uso Windows: como ter o WSL" (`wsl --install`); 1º acesso ao Ubuntu pede usuário e senha; `ls` vazio é normal |
| 14 | 4 · 7 | 7 · 8 | 8 · 8 | um bloco de copiar por comando, com destino; "é uma linha só"; sem "confira o caminho"; senha do computador (letras não aparecem; computador da escola = parar); WSL cola no Ubuntu; onde procurar na página oficial ("Install") |
| 15 | 5 · 7 | 8 · 8 | 8 · 8 | quadro `.psafe` quebrado em colunas (inline `code` num flex) consertado; "Vai pela conta? Pode pular" no passo da API; plano: remete à página oficial de autenticação |
| 16 | 5 · 7 | 8 · 8 | 9 · 9 | tela real "Trust this folder?" com "Trust and continue" (setas + Enter) e "não use Open restricted"; heredoc explicado + Ctrl+C se parar em `>`; `~` = casinha do Finder; `cat entradas/reuniao.txt` |
| 17 | 7 · 6 | 8 · 8 | 9 · 9 | cada pedido num bloco com "cole dentro do Codex"; "Would you like to make the following edits?" → "Yes, proceed"; "criou sem perguntar também acontece"; `cat` da pauta no passo 3; cartões coerentes com a resposta real |
| 18 | 5 · 6 | 7 · 7 | 8/9 · 9 | prática em 4 blocos (terminal · terminal · Codex · terminal); `/permissions` lido na prática (Esc fecha); "Já fiz esta prática antes" com blocos prontos de `-antes2`; volta só se o diff mostrou mudança não autorizada |

Fatos conferidos nesta máquina (codex-cli 0.156.1): `codex --version`, `codex login status` → "Logged in using ChatGPT",
diálogo "Trust this folder?" (Trust and continue / Open restricted), aprovação "Would you like to make the following edits?"
("Yes, proceed"), `/permissions`, `/quit`. As telas de resposta das aulas 17 e 18 (leitura, plano.md, diff) são saídas
reais do Codex na pasta de treino, encurtadas.

Aceito como limite, não defeito: o curso não mostra a saída do `codex login status` com chave de API nem a tela do
`/permissions` (não conferidas); não diz quais planos incluem o Codex (remete à página oficial, que muda). No Windows,
o WSL exige senha de administrador — em computador da escola, só com o técnico. Ainda **não houve teste com pessoas reais**.
