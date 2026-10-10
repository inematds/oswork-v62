# Leitor simulado — edição cmd (1.5.1, 10/10/2026)

Personas: Lúcia (34, professora de ciências) e Denise (58, coordenadora), Windows 11 em português, cmd dentro do Terminal.

## Rodada 1
| Aula | Nota | Travou em | Correção |
|---|---|---|---|
| 13 | 8 | tela real do `dir` (volume, `.`/`..`, totais); "duas letras"; PowerShell "janela azul" | figura com a saída real e "pule…"; texto corrigido; PowerShell pelo `PS` |
| 16 | 6 | aviso "colar várias linhas"; nome de usuário com espaço; acento no `type`; tela de sandbox do Codex | aspas em todo `"%USERPROFILE%\…"` (29 aulas); aviso "Colar mesmo assim"; `notepad` no lugar do `type`; nota do sandbox |
| 19 | 8 | aviso de colar várias linhas | aviso no passo da prática |
| 38 | 6 | QR do Telegram no computador; selecionar só o valor no Bloco de Notas; "três comandos" × sete | caminho completo do QR; passo de apagar e colar; título do passo; .env "só seu" sem exagero |
| 44 | 7 | como cadastrar a chave; impressão digital sem painel | opção "SSH key" do painel + `type` do .pub; `ssh-keygen -lf` no console; gabarito com `ssh -p` |
| 49 | 7 | termos do winget (Y); tela real do `ssh -T` | aviso do Y; tela com a impressão digital do GitHub; Enter no fim do bloco 2 |

Efeito colateral corrigido: as aspas entraram num cartão (JSON inválido na aula 19) e engoliram pontos finais; reparado e conferido (cards JSON válidos nas 49).

## Rodada 2 (aulas 16 e 38)
- 16: nota 4 → 8 "com os arquivos no ar" (o 404 era só porque `materiais/treino/` ainda não foi publicado). Ajuste: separar `curl: (6)` (internet) de `curl: (22)` (arquivo fora do site).
- 38: nota 7. Ajustes: prática reordenada (Telegram no computador → BotFather → bloco → Bloco de Notas); `if not exist .env copy …` para colar o bloco de novo nunca apagar o token.
