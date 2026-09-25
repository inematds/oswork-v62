# Módulo 4 — Pastas, Markdown e segredos (aulas 19–24)

Objetivo do v2: montar a casa digital e separar conhecimento de credenciais. Laboratório: "Organize seu segundo cérebro operacional".
Fonte: OSWork v2, `MODULES[3]`. Personagens: **Denise** (coordenadora pedagógica) e **Lúcia** (professora de ciências do 8º ano).

Terminal: todas as práticas usam o mesmo terminal do módulo 3, com o comando exato e o que conferir. Tudo acontece na
pasta de treino `~/projetos` (dados fictícios). Os modelos vêm do kit do v2 (`https://inematds.github.io/oswork/materiais/`).
Cada aula dá a saída para quem pulou a anterior (o comando que cria o que falta). O módulo inteiro monta o laboratório do v2:
pastas (19) → README (20) → config com os 4 arquivos (21) → .env.example (22) → .gitignore (23) → AGENTS.md + "Leia primeiro" (24).

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 19 | Uma pasta representa um contexto | fundamento | desenhar a árvore de `~/projetos` (config + um projeto de treino com entradas e saídas) e criá-la com um comando | tarefa (terminal), 8 min | a pasta existe; como escrever o que ela é? |
| 20 | Markdown é texto organizado | ferramenta | escrever o README do projeto de treino em Markdown, com cada campo real ou "a definir" | tarefa (terminal + editor), 10 min | README explica o projeto; e o que vale para todos os projetos? |
| 21 | Cada arquivo tem um trabalho | ferramenta | pôr os 4 arquivos em config e dizer, para cada nota, em qual deles ela mora | tarefa (terminal + análise com gabarito), 10 min | e a senha do bot, vai em qual? em nenhum |
| 22 | Segredos não são conhecimento compartilhável | fundamento | criar o `.env.example` com nomes de variáveis e valores fictícios, sem nenhum valor real | tarefa (terminal), 8 min | como garantir que o `.env` nunca entre no histórico? |
| 23 | Ignore antes do primeiro commit | ferramenta | criar o `.gitignore` antes do primeiro commit e dizer qual linha segura o `.env` e qual libera o `.env.example` | tarefa (terminal), 8 min | com tudo guardado, o que a IA deve ler primeiro? |
| 24 | Faça uma limpeza de contexto | ferramenta | acrescentar ao README uma seção "Leia primeiro" com 3 caminhos que existem e estão em dia | tarefa (terminal + editor), 10 min | módulo 5: o AGENTS.md orienta a execução |

## Metáforas de abertura (inéditas; ambiente de escola)

- **19 — o arquivo de aço da secretaria:** uma gaveta por turma; ninguém guarda a turma A na gaveta da B. Pasta = gaveta de um contexto.
- **20 — o roteiro de experimento:** Lúcia já escreve roteiro com Título, Materiais e Procedimento; Markdown é o mesmo, com `#` e `-`.
- **21 — os livros da secretaria:** livro de atas, livro de ocorrências, caderno de procedimentos — cada um com um trabalho.
- **22 — o quadro de chaves da portaria:** a lista de quais chaves existem pode ficar à vista; as chaves, não.
- **23 — o malote conferido antes de lacrar:** depois que o malote saiu, tirar o papel da lista não traz o papel de volta.
- **24 — o mural da sala dos professores:** aviso vencido atrapalha mais do que mural vazio.
