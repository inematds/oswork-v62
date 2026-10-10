# Convenções cmd (edição 1.5.x, 10/10/2026)

Pedido do Nei: começa com cmd, sem Linux; depois vai para a VPS usando Linux.
Aulas 13–42 e 49 = cmd do Windows. Aulas 43–48 = Linux na VPS (aula 44 traz a tabela cmd → Linux).
Edição WSL preservada na tag `v1.4.1-wsl`. Fonte das convenções: oswork-quick/conteudo/pt.json (conferido nas docs em 07/10).

## Tabela de troca
| antes (Bash/WSL) | agora (cmd) |
|---|---|
| `pwd` | `cd` (sozinho) |
| `ls` | `dir /b` (nomes) ou `dir` |
| `ls -a` | `dir /a /b` |
| `cat arq` | `type arq` |
| `head -4 arq` | `type arq` (arquivo curto) ou `more arq` |
| `mkdir -p a/b` | `mkdir a\b` (cria as de cima) |
| `cp arq dest` | `copy arq dest` |
| `cp -r pasta dest` | `xcopy pasta dest\ /e /i` (ou `robocopy pasta dest /e`) |
| `diff -r` | `fc arq1 arq2` (um arquivo por vez) |
| `nano arq` | `notepad arq` |
| `printf '…' > arq` | `notepad arq` (conteúdo digitado/colado) — evitar `echo` em .env (espaço no fim) |
| `chmod 600 .env` | não existe; o .env fica na pasta pessoal do usuário + `.gitignore` |
| `grep -n x arq` | `findstr /n x arq` |
| `python3` | `py` (instalar com `winget install -e --id Python.Python.3.12`) |
| `~` / `~/projetos` | `%USERPROFILE%` / `%USERPROFILE%\projetos` |
| `explorer.exe .` / `open .` | `explorer .` |
| `curl … | sh` (Codex) | `npm install -g @openai/codex` (Node: `winget install -e --id OpenJS.NodeJS.LTS`) |
| `sudo apt install gh` | `winget install -e --id GitHub.cli` |
| `git` | `winget install -e --id Git.Git` |
| prompt `$` / `denise@notebook:~$` | `C:\Users\denise>` (no HTML: `&gt;`) |
| `command not found` | `'x' não é reconhecido como um comando interno ou externo, um programa operável ou um arquivo em lotes.` |
| `git version 2.43.0` | `git version 2.47.0.windows.1` |

- Depois de todo `winget install`: fechar e abrir o cmd (PATH). Primeiro winget pode pedir para aceitar termos: Y.
- Colar no cmd: botão direito do mouse ou Ctrl+V.
- Mac: só uma nota `details.mais` na aula 13 (Terminal, pwd/ls; tabela na aula 44).
- Termo `cmd` precisa de `.gterm` em toda aula que o cita (perfil técnico). Cuidado: "Cmd+V" casa com o termo.
- Nomes de exemplo: Lúcia (professora), Denise (coordenadora) → `C:\Users\lucia`, `C:\Users\denise`.
- type mostra acento trocado (cp850): nota 'use notepad arq' na 1ª ocorrência (aula 17)
