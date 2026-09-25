# Módulo 6 — Git e GitHub sem perder trabalho (plano)

Objetivo do v2 (MODULES[5]): salvar uma versão, inspecionar diferenças e recuperar uma mudança de treino.
Laboratório: "Seu primeiro ponto de recuperação". Pergunta de conferência do v2: "git commit já envia os arquivos ao
GitHub?" → Não. Commit registra localmente; push envia ao remoto configurado.

Pasta de treino do módulo: `~/projetos/treino-git` (criada na aula 31; cada aula traz o bloco de comandos para quem
pulou). Clone da aula 34 em pasta separada: `~/projetos/clone-curso` (repositório público do curso,
`https://github.com/inematds/oswork-v62.git`). Todas as saídas de terminal mostradas nas aulas foram conferidas nesta
máquina em 25/09/2026 (git 2.43.0); códigos de commit variam em cada computador.

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 31 | Git é o histórico do projeto | fundamento | dizer o que são Git, repositório, commit e GitHub, e começar um histórico só na pasta de treino | tarefa (terminal), 8 min: `git --version`, `mkdir -p`, `cd`, `git init -b main`, `git status` | o histórico está vazio: antes de salvar, olhar o que vai entrar |
| 32 | Observe antes de preparar | ferramenta | ler `git status`, `git diff` e `git diff --cached` e dizer em que etapa cada arquivo está | tarefa (terminal), 10 min: criar README.md e notas-privadas.txt, `git add README.md`, explicar a saída vazia | o README está separado; falta salvar com o seu nome e uma mensagem que explique |
| 33 | Salve uma versão com intenção | ferramenta | configurar autoria só no treino, deixar a nota privada de fora com .gitignore e criar o primeiro commit com mensagem concreta | tarefa (terminal), 10 min: `git config`, `.gitignore`, `git add`, `git commit -m`, `git log --oneline` | e um projeto que já está no GitHub? copiar e atualizar sem estragar |
| 34 | Clone e atualize com cuidado | ferramenta | clonar o repositório do curso numa pasta separada, conferir o estado e atualizar com `git pull --ff-only`, sabendo parar | tarefa (terminal), 8 min: `git clone`, `git status`, `git log --oneline -3`, `git pull --ff-only` | e quando uma versão salva estava errada? |
| 35 | Recupere sem apagar o histórico | ferramenta | criar um segundo commit de treino, desfazê-lo com `git revert` e conferir o README aberto | tarefa (terminal), 12 min: mudar o título, `git diff`, commit, `git log`, `git revert --no-edit HEAD`, `cat README.md` | salvar e desfazer ficou no seu computador; enviar ao GitHub é outro passo |
| 36 | Publique só o que revisou | ferramenta | fazer a conferência de quatro pontos antes de um push (destino, estado, conteúdo do commit, segredos) e decidir enviar ou não | tarefa (terminal), 10 min: `git remote -v`, `git status`, `git show --stat` no treino e no clone | módulo 7: Telegram — o token do bot é o primeiro segredo que nunca pode ir num push |

Personagens: **Denise** (coordenadora pedagógica) e **Lúcia** (professora de ciências do 8º ano).

Metáforas de abertura (inéditas no curso; conferidas contra os planos dos módulos 2, 3, 4, 5 e 7):
- **31 — o diário de classe:** uma linha por dia, com data e assinatura; nada se apaga, acrescenta-se uma linha nova.
- **32 — a mesa de montagem da prova:** você separa as folhas que entram nesta versão antes de grampear.
- **33 — a legenda atrás da foto:** foto de evento sem legenda não diz nada dez anos depois; "update" é foto sem legenda.
- **34 — a apostila da rede:** você recebe a cópia; a atualização chega como páginas novas. Se você riscou a mesma página, para e compara.
- **35 — a errata do jornal da escola:** o erro não some da edição anterior; a errata publicada corrige e mostra que houve correção.
- **36 — a nota lançada no sistema da secretaria:** no caderno, só você vê; lançada, todo mundo com acesso vê. Confira turma, aluno e nota antes de lançar.

Cenas: 31 Lúcia acrescentando uma linha datada no diário de classe, notebook ao lado · 32 Denise separando folhas
de prova em montes antes de grampear · 33 Lúcia escrevendo a legenda no verso da foto da feira de ciências ·
34 Denise comparando a apostila nova da rede com a sua, cheia de anotações · 35 Denise mostrando a errata no jornal
da escola · 36 Lúcia na secretaria conferindo o caderno de notas com a tela antes de lançar.

Termos novos (fora do glossário), definidos com .gterm nas aulas: `revert`, `restore` (aula 35), `origin` (aula 36).
