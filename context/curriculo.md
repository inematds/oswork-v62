# OSWork v6.2 — currículo

Formato: `formato-curso-v6` 6.2 com **perfil técnico**, módulos e material complementar.
`<meta name="curso" content="oswork62">`. Fonte do conteúdo: **OSWork v2** (`~/projetos/oswork`, `conteudo/modulos.py`),
integral: 8 módulos, 48 tópicos. O `oswork-v6` (7 aulas para leigo) continua como está.

## Passo 0 — descoberta (decidido com o Nei em 24/09/2026)

1. **Aluno:** profissional que já usa chat de IA no trabalho e quer montar um ambiente de trabalho com IA — arquivos,
   instruções, Codex, Git, bot e servidor. Aprende o técnico: essa é a missão do curso ("o público tem que aprender
   estes conhecimentos mais técnicos").
2. **Profissões-alvo:** **coordenadora** (coordena equipe, reuniões, processos) e **professora** (prepara material,
   corrige, organiza turmas) — as mesmas do v2. Nomes e cenas diferentes do `oswork-v6` (lá: gestora Sílvia, professor).
3. **Tecnologia:** usa chat de IA, e-mail, planilha e pastas; nunca programou. O terminal aparece a partir do módulo 3,
   sempre com o comando exato e o que conferir.
4. **Sai fazendo (curso inteiro):** pasta organizada com instruções verificáveis, uma Skill, histórico Git, um bot restrito
   e um plano de operação supervisionada numa VPS (entregas finais do v2).
5. **Tempo:** aulas de ~15 min. O aprofundamento integral do v2 fica no material complementar, fora desse tempo.

## Estrutura

- **1 aula por tópico do v2** → 48 aulas em 8 módulos (6 por módulo).
- **Núcleo** (≤900 palavras, ~15 min) ensina o tópico no jeito v6: cena, promessa, 4 steps com visual real, prática, fecho.
- **Complementar** = texto integral do tópico no v2 (O que é · Por que aprender · Conceitos-chave · Na prática ·
  ação do tópico · figura), gerado por `scripts/complementar.py` direto do `modulos.py` — nada reescrito à mão.
  A **última aula de cada módulo** leva também o fechamento do módulo no v2: laboratório, bloco do laboratório,
  critério de pronto, rubrica, "Confira o que ficou", resumo e fontes.
- Jargão: definido com `.gterm` em cada aula em que aparece; glossário em `context/glossario.json` (mesma definição
  em todo o curso) e página de glossário gerada.

## Módulo 1 — Modelos: escolha pela tarefa (piloto para aprovação)

Objetivo do v2: comparar modelos com uma tarefa real e um critério de qualidade. Laboratório: "Sua ficha de decisão".

| Aula | Tópico v2 | Tipo | Promessa | Prática | Gancho |
|---|---|---|---|---|---|
| 1 | IA como sistema de trabalho | fundamento | desenhar as 7 peças e apontar a que falta numa tarefa real | tarefa, 8 min | se o modelo é uma peça, que tipos de peça existem? |
| 2 | Tipos de IA e para que servem | fundamento | dizer o tipo de modelo que cada tarefa pede antes do nome | tarefa, 8 min | dentro do mesmo modelo ainda há um controle: o esforço |
| 3 | Modelo não é esforço de raciocínio | fundamento | repetir um pedido mudando só o esforço e dizer se melhorou | prompt, 10 min | "melhorou" precisa de régua |
| 4 | Crie uma régua de qualidade | ferramenta | escrever 3 critérios antes e decidir entre 2 respostas | análise, 10 min | testar custa: de quem é a conta? |
| 5 | Entenda acesso e cobrança | fundamento | identificar o método de acesso e registrar sem a credencial | tarefa, 8 min | com conta certa, até onde deixar a IA ir sozinha? |
| 6 | Delimite a autonomia | ferramenta | escrever autorização com arquivos, resultado, 3 verificações e parada | prompt, 10 min | módulo 2: chat, Work e Desktop |

Personagens do módulo: **Denise**, coordenadora pedagógica de uma escola; **Lúcia**, professora de ciências do 8º ano.
Metáforas de abertura (inéditas no ecossistema v6): bancada de oficina (A1), bandejas de triagem (A2), botão de volume
× estação de rádio (A3), a régua sobre a ata — o próprio conceito do v2 (A4), duas faturas (A5), bilhete de autorização (A6).
