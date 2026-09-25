# Leitor simulado — OSWork v6.2, Módulo 8 (25/09/2026)

Personas: **Regina, 52, coordenadora pedagógica de escola estadual** (chat às vezes, plano gratuito) e
**Tatiane, 34, professora de matemática** (ChatGPT quase todo dia; práticas no notebook, Windows/WSL ou Mac).
Capturas do celular (390px), tema papel.

| Aula | Rodada 1 (R · T) | Rodada 2 (R · T) | Principais correções |
|---|---|---|---|
| 43 | 8 · 9 | 9 · 9 | figura do plano com as 6 linhas (API incluída); as 5 partes do plano-vps.md apresentadas na prática; mensalidade "ligada ou parada"; exemplo da Lúcia refeito (placa de vídeo parada) |
| 44 | 6 · 8 | 8 · 9 | chave pública: "o painel do provedor guia; hoje não precisa criar"; motivo de trocar a porta; três rotas viraram `.lado` Sessão 1 × Sessão 2 + saída de emergência; gabarito cita as linhas reais da parte Acesso |
| 45 | 7 · 7 | 8 · 8 | WSL no Windows; Lúcia sem "Git: falta" (contradizia o módulo 5); Y maiúsculo = padrão; aviso do Mac (janela das ferramentas de linha de comando) |
| 46 | 6 · 6 | 7 · 8 | `.gitignore` nomeado (módulo 4); trios dono/grupo/outros explicados; firewall do painel com ação clara; "próxima aula" no lugar de número; aviso WSL para o chmod; diagrama vertical legível no celular |
| 47 | 4 · 5 | 6 · 7 → corrigido | cópia para /etc/systemd/system e daemon-reload explicados; molde com o caminho do kit descompactado (~/projetos/oswork-kit/bot); bloco "cole no arquivo" separado de "rode no terminal"; nano com Ctrl+O/Ctrl+X; como trazer o zip do Downloads para o WSL; "passos" no lugar de "steps" |
| 48 | 7 · 7 | 7 · 9 → corrigido | vendas.csv e /relatorio apresentados; `df -h /`; exemplos de lugar externo; evidências 2 (self-test do kit) e 4 (journalctl sem token); `cd` + `ls vendas.csv` no início da prática; aviso WSL para o diff |

Defeito de layout achado na rodada 1: `.psafe` (display:flex) com `<code>`/`<a>` no meio quebrava em colunas no celular.
Correção nas aulas: `.psafe` só com texto corrido; kit, link e caminhos foram para um parágrafo "Onde está…" logo abaixo.
(Vale avisar a skill: o `.psafe` não aceita elemento inline sem quebrar.)

Pendências da rodada 2 (47: WSL/Downloads, editor; 45: Mac; 46: frase do WSL; 44/47: "step") aplicadas na correção
final. Auditoria depois das correções: 43–48 em 10/10; motor 26/26. Rodada 3 não foi necessária: os "travei" que
sobraram eram pontuais e foram corrigidos direto. Ainda **não houve teste com pessoas reais** (`TESTE-HUMANO.md` §2).
Aceito como decisão: as práticas 44 (análise) e 47 (só editar a unidade) não exigem VPS; ligar o serviço fica no
plano e no laboratório do complementar da aula 48.
