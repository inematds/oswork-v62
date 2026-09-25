# Módulo 8 — VPS do zero e operação 24/7 (aulas 43–48)

Objetivo do v2: preparar um plano de implantação, supervisão, backup e verificação do serviço.
Laboratório do v2: "Da pasta local a um serviço supervisionado" (vai no complementar da aula 48).
Fonte: `~/projetos/oswork/conteudo/modulos.py`, `MODULES[7]`; kit do v2 (`materiais/plano-vps.md`, `materiais/bot/`:
`bot.py`, `oswork-bot.service`, `vendas.csv`, `.env.example`). Toda saída de tela das aulas usa as frases reais do kit
(`/status`, `/relatorio`, mensagens de log do `bot.py`, `--self-test`) ou campos entre colchetes; nenhum IP, preço, PID
ou provedor inventado.

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 43 | Uma VPS é uma máquina sob sua responsabilidade | fundamento | preencher "Antes de contratar" do plano: o que roda, quem cuida, quanto, sistema, como desligar | tarefa, 8 min (plano-vps.md ou nota) | com a máquina alugada, a primeira porta é o acesso |
| 44 | Entre por SSH e preserve acesso | ferramenta | dizer em que máquina está pelo que o terminal mostra e aplicar a regra da segunda sessão | análise, 8 min (caso da porta trocada + gabarito) | lá dentro, o que colocar na máquina? |
| 45 | Instale só o necessário | ferramenta | conferir Python 3 e Git no terminal e criar ~/projetos, sem nada além | tarefa, 8 min (terminal, comandos que não mudam o sistema) | com o bot lá dentro, quem pode bater na porta? |
| 46 | Proteja a rede e as credenciais | ferramenta | listar as portas necessárias e deixar um .env de treino com chmod 600, conferido com ls -l | tarefa, 8 min (terminal, pasta de treino) | falta alguém que ligue o bot e o religue |
| 47 | Systemd supervisiona o processo | ferramenta | adaptar os 4 campos da unidade do kit e ler no status e no log se o bot roda | tarefa, 10 min (editor + grep na cópia do kit) | ligado e religado não quer dizer cuidado |
| 48 | Disponibilidade exige rotina de cuidado | ferramenta | fazer backup de vendas.csv fora da pasta, restaurar numa pasta separada e provar com diff e o total | tarefa, 10 min (terminal) | fim do curso: as entregas finais e o próximo teste de restauração |

Personagens: **Denise** (coordenadora pedagógica) e **Lúcia** (professora de ciências do 8º ano), com o bot de treino do
kit (módulo 7), que responde `/status` e `/relatorio` com dados fictícios.

Metáforas de abertura (inéditas; tema do módulo): a chave da sala alugada (A43), a fechadura trocada — não devolva a
chave velha antes de testar a nova (A44), a mala de mão (A45), a portaria da escola com lista de quem entra e o
carteiro que sai para buscar a correspondência (A46), o zelador que acende as luzes toda manhã e anota no livro de
ocorrências (A47), o simulado de incêndio — só vale o que foi ensaiado (A48).

Termos novos do módulo (fora do `glossario.json`, definidos com `.gterm`): porta, chave pública, impressão digital,
console de recuperação, unidade.
