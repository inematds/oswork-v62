# Módulo 5 — AGENTS, Skills e memória (plano)

Objetivo do v2: criar instruções de projeto e uma capacidade reutilizável com critério de revisão.
Laboratório do v2: "Sua primeira Skill de relatório" (vai no complementar da aula 30).

Ponto de partida do aluno (vem dos módulos 3 e 4, sempre com saída para quem pulou): a pasta de treino
`~/projetos/meu-primeiro-projeto` (README.md, AGENTS.md, entradas/, saidas/) e a pasta `~/projetos/config`
(memoria.md, falhas.md, dicas.md, decisoes.md). Dados fictícios: `entradas/vendas.csv` do kit (Caderno 35.50,
Caneta 9.50, Agenda 55.00). Codex aberto com `codex` dentro da pasta (módulo 3). Terminal só com comando exato,
nada destrutivo, nenhum segredo em tela.

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 25 | AGENTS.md orienta a execução | fundamento | reescrever o AGENTS.md do projeto de treino com cinco regras que dá para conferir | tarefa, 10 min (editor de texto) | essas regras valem em qualquer pasta? global × projeto |
| 26 | Global e projeto se complementam | fundamento | dizer quais instruções valem numa pasta e conferir o resumo do Codex contra os arquivos | tarefa, 10 min (terminal + Codex, só leitura) | regra diz o que respeitar; e o procedimento que se repete toda semana? |
| 27 | Skills empacotam procedimentos | ferramenta | criar a Skill relatorio-semanal na pasta certa, com cabeçalho de nome e descrição | tarefa, 10 min (terminal + editor) | a Skill não lembra do que você combinou ontem: memória |
| 28 | Memória precisa de manutenção | fundamento | escrever uma memória curta e datada e fazer o agente citar o fato que usou | tarefa, 10 min (editor + chat ou Codex) | e quando algo dá errado, o que vai para o registro? |
| 29 | Falhas viram proteções pequenas | ferramenta | registrar uma falha fictícia em falhas.md e escrever a checagem que a pega antes | tarefa, 10 min (terminal, só leitura) | a Skill funciona uma vez; funciona sempre? |
| 30 | Teste a capacidade reutilizável | ferramenta | testar a Skill com três casos e corrigir só a menor regra | tarefa, 12 min (Codex) | módulo 6: Git, para não perder o que você construiu |

Personagens: **Denise** (coordenadora pedagógica de uma escola) e **Lúcia** (professora de ciências do 8º ano).
Alternância: 25 Lúcia · 26 Denise · 27 Lúcia · 28 Denise · 29 Lúcia · 30 Denise (exemplos internos alternam as duas).

Metáforas de abertura (inéditas no ecossistema v6, tiradas da escola):
- **A25 — a placa na porta do laboratório.** "Use óculos antes de acender o bico de Bunsen" se confere; "tenha cuidado" não.
- **A26 — regimento da escola × combinados da sala.** O regimento vale em toda a escola; o combinado da turma decide ali dentro.
- **A27 — o fichário de roteiros de experimento.** A regra da porta vale sempre; o roteiro sai do fichário só no dia do experimento.
- **A28 — o mural da sala dos professores.** Poucos avisos, datados, e alguém tira o velho; não é o grupo de mensagens inteiro.
- **A29 — a fita antiderrapante no degrau.** Depois do escorregão, ninguém reconstrói a escada: põe a fita e confere.
- **A30 — o simulado de evacuação.** Ensaia o dia normal, a porta bloqueada e o pedido fora do protocolo antes do dia real.

Visuais (sequência diferente do módulo 1): 25 janela/lado/lado/janela · 26 janela/diag/lado/terminal · 27 lado/terminal/lado/janela ·
28 janela/lado/tela/janela · 29 janela/lado/diag+terminal/tela · 30 janela/tela(2 casos)/tela/lado.
