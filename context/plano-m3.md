# Módulo 3 — Terminal e Codex na prática (aulas 13–18)

Objetivo do v2: abrir um projeto de treino no Codex e produzir uma alteração verificável.
Laboratório do v2: "Primeiro projeto acompanhado". Primeiro módulo com terminal: toda prática traz o comando exato
num `.terminal`/`.pcode` e o que conferir na saída. Nada destrutivo; nenhum segredo impresso; tudo na pasta de treino
`~/projetos/meu-primeiro-projeto` com arquivos fictícios.

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 13 | Terminal é uma porta de entrada | fundamento | abrir o terminal, rodar `pwd` e `ls` e dizer em que pasta está e o que tem nela | tarefa, 8 min | o terminal abre; agora falta o programa que vai trabalhar nele: o Codex |
| 14 | Instale pela fonte oficial | ferramenta | instalar o Codex pelo endereço oficial e confirmar com `codex --version` | tarefa, 10 min | instalado não é conectado: de qual conta sai o uso? |
| 15 | Autentique sem espalhar segredos | ferramenta | entrar com `codex login`, conferir com `codex login status` e anotar só o método na ficha | tarefa, 8 min | conectado, mas em qual pasta ele vai trabalhar? |
| 16 | Entre na pasta antes de pedir | ferramenta | criar a pasta de treino com README.md e entradas/reuniao.txt, entrar nela e abrir o Codex ali | tarefa, 10 min | o Codex está na pasta certa; o primeiro pedido é só de leitura |
| 17 | Faça uma primeira tarefa de leitura | ferramenta | pedir uma leitura sem edição, depois autorizar só plano.md e conferir o arquivo | prompt, 12 min | ele escreveu um arquivo; e se escrever o errado? |
| 18 | Use permissões e recuperação | ferramenta | guardar um ponto de retorno, criar AGENTS.md com duas regras e conferir que só ele mudou | tarefa, 10 min | módulo 4: a estrutura de pastas e instruções que o agente lê sempre |

Personagens: **Denise** (coordenadora pedagógica) e **Lúcia** (professora de ciências do 8º ano), alternando por step.

Metáforas de abertura (inéditas no curso): mapa "você está aqui" da escola (A13) · lacre da caixa entregue (A14) ·
crachá na catraca × senha do cofre (A15) · a sala da turma certa antes de começar a aula (A16) · vistoria antes da
reforma (A17) · chaveiro da escola: a chave de uma sala, não a chave mestra (A18).

Fatos técnicos vêm do v2 (MODULES[2]): `pwd`, `ls`, `cd`, `mkdir -p`, instalador `curl -fsSL https://chatgpt.com/codex/install.sh | sh`,
`codex --version`, `codex login`, `codex login status`, `printenv OPENAI_API_KEY | codex login --with-api-key`, "command not found",
README.md × AGENTS.md, plano.md com três ações e uma verificação, permissões do cliente ≠ instrução escrita.
Saídas reais conferidas nesta máquina em 25/09/2026: `codex --version` → `codex-cli 0.156.1`; `codex login status` → `Logged in using ChatGPT`.
