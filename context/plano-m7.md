# Módulo 7 — Telegram como interface de trabalho (plano)

Objetivo do v2: executar um bot restrito de consulta e entender onde a IA entra. Laboratório: "Um bot que responde sem
executar mensagens". Base técnica: o bot do kit do OSWork v2 (`materiais/bot/` dentro de `oswork-kit.zip`): `bot.py`
(só biblioteca padrão, sem IA), `.env.example`, `vendas.csv` (3 vendas fictícias, total R$ 100,00), `README.md`.
Comandos reais usados nas aulas: `python3 bot.py --self-test`, `cp .env.example .env`, `chmod 600 .env`,
`python3 bot.py --identify`, `python3 bot.py`, Ctrl+C. Respostas reais do bot copiadas do `bot.py`.

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 37 | Telegram é a interface, não o agente | fundamento | desenhar o caminho celular → Telegram → bot → função permitida → resposta e marcar onde uma IA seria útil | tarefa, 8 min (papel) + autoteste opcional | o bot precisa de uma senha própria: onde ela fica? |
| 38 | Crie o bot e proteja o token | ferramenta | criar o bot no BotFather e guardar o token do bot só no `.env`, com leitura restrita | tarefa no terminal, 10 min | quem tem o token opera o bot, mas quem pode conversar com ele? |
| 39 | Autorize pessoas e ações | ferramenta | descobrir o seu ID numérico com `--identify` e colocá-lo na lista de acesso | tarefa no terminal, 8 min | com a lista pronta, como o bot fica escutando? |
| 40 | Comece com long polling | ferramenta | ligar o bot, receber /status e /relatorio no celular e conferir o total com `vendas.csv` | tarefa no terminal, 10 min | o bot funciona sem IA; onde ela entraria sem estragar o total? |
| 41 | Conecte capacidades em etapas | fundamento | escrever um contrato de integração em cinco linhas e testar no chat que o resumo não muda o total | prompt, 10 min | antes de levar para uma VPS, provar que ele falha bem |
| 42 | Teste operação e falhas | ferramenta | rodar o autoteste e quatro testes reais, registrando o que foi simulado e o que foi testado no Telegram | tarefa no terminal, 12 min | módulo 8: VPS do zero, o bot ligado sem o seu computador |

Personagens: **Denise** (coordenadora pedagógica) e **Lúcia** (professora de ciências do 8º ano). Caso-fio do módulo:
Lúcia monta um bot pessoal de consulta para a lojinha fictícia do grêmio (caderno, caneta, agenda = os dados do kit);
Denise avalia se a escola poderia usar o mesmo desenho para consultas da secretaria.

Metáforas de abertura (inéditas; nenhuma repete as do módulo 1):
- 37 — **o interfone da portaria**: o aparelho só leva a voz; quem decide abrir o portão é a pessoa na portaria.
- 38 — **a chave do portão da escola**: quem tem a cópia entra, não importa o nome; perdeu, troca-se a fechadura (revogar).
- 39 — **a lista de quem pode buscar o aluno**: confere-se o documento, não o nome que a pessoa diz.
- 40 — **o escaninho da sala dos professores**: o bot vai ao escaninho e espera um pouco (long polling); o webhook seria o carteiro tocando a campainha.
- 41 — **boletim com nota e parecer**: a nota é calculada; o parecer escrito comenta, mas nunca muda a nota.
- 42 — **a passagem de som antes da reunião de pais**: testa-se o microfone com o auditório vazio, e anota-se o que foi ensaio e o que foi real. (Trocada: o módulo 5 já usa "simulado de evacuação".)
