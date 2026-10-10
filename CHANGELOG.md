# Changelog — OSWork v6.2

## 1.5.1 — 2026-10-10

- No Windows, o curso passa a usar o **cmd** (Prompt de Comando), sem WSL/Linux, das aulas 13 a 42 e na 49: `cd` sozinho e `dir` no lugar de `pwd` e `ls`, `%USERPROFILE%\projetos`, `explorer .`, `notepad` no lugar do `nano`, `type`, `copy`/`xcopy`, `fc`, `findstr`; Codex por `winget` (Node.js) + `npm install -g @openai/codex`; Git, gh e Python por `winget`; bot com `py`.
- Módulo 8 (VPS) continua em Linux: a aula 44 traz a tabela cmd → Linux na primeira entrada por `ssh`; as práticas 45–48 rodam na VPS, com alternativa no cmd para quem ainda não tem VPS.
- Arquivos de treino hospedados em `materiais/treino{,-en,-es}/` (baixados com `curl`, sem acento quebrado pelo cmd).
- Edição WSL preservada na tag `v1.4.1-wsl`. Pedido do Nei em 10/10/2026: "começa com cmd sem linux, depois vai pra uma VPS usando linux".

## 1.4.1 — 2026-10-07

- Aula 49 (módulo 6, 7ª aula): chave SSH, `gh auth login` com SSH, repositório público ou privado (`gh repo create`) e GitHub Pages, com prática de publicar uma página de treino. Leitor simulado em 3 rodadas (5 → 7,5 → ver `context/leitor-simulado.md`).
- Aula 19: o passo 4 mostra a mesma pasta na janela de arquivos do Windows (`explorer.exe .`, endereço `\\wsl.localhost\Ubuntu\…`; `open .` no Mac); terminal de exemplo com `/home/denise`; prática com o passo da janela.
- Módulo 6 passa a 7 aulas (kickers e navegação 36 → 49 → 37). Definição de "chave pública" passa a citar GitHub e VPS.

## 1.3.1 — 2026-09-25

- Vídeo-aulas: página `videos/` com um player por módulo (avatar e voz do Nei, capítulos por aula, legendas). Publicados M1, M2 e M4 em PT; os demais entram conforme ficam prontos. MP4/SRT na release `video-v1.0.0`.
- Landing PT: link "Assista às vídeo-aulas".

## 1.2.1 — 2026-09-25

- Landing: mostra só os 8 módulos, fechados, e o clique abre as aulas de cada um (formato-curso-v6 6.3.3).
- Menu do curso: novo item "Trilhas", que volta para a landing para escolher o módulo. PT/EN/ES (tradução: US$ 0,02).

## 1.1.1 — 2026-09-25

- Botão "copiar" dos terminais de exemplo copia só os comandos (sem `$` e sem a resposta).
- Caixa de segurança da prática não quebra mais em colunas no celular.
- Aula 26: regra do AGENTS.md conferida na documentação oficial do Codex — sem ressalva ("prevalece"); definição de
  AGENTS.override.md exata (o Codex ignora o AGENTS.md da mesma pasta). Pasta `~/.agents/skills` (aula 27) confirmada.

## 1.1.0 — 2026-09-25

Módulos 2 a 8 (aulas 7–48): curso completo com os 48 tópicos do v2, uma aula por tópico, complementar integral e
fechamento de cada módulo. Planos em `context/plano-m2..m8.md`, leitor simulado (3 rodadas) em `context/leitor-m2..m8.md`.
Glossário com 88 termos (29 novos); `.gterm` de Work e Desktop no gancho da aula 6; definição de Desktop mais precisa.
Cenas pelo Codex. Auditoria: PT 10/10 nas 48 aulas; EN e ES 48/48 aprovadas (média 9,9 — frases longas da tradução); motor 26/26 nos três. Tradução: US$ 0,50 acumulado.

## 1.0.0 — 2026-09-24

Módulo 1 (Modelos: escolha pela tarefa) completo, piloto do formato v6 com perfil técnico: 6 aulas, uma por tópico
do v2; material complementar com o texto integral do tópico e, na aula 6, o fechamento do módulo (laboratório,
rubrica, checagem, resumo, fontes); glossário gerado; cenas pelo Codex; PT/EN/ES.
