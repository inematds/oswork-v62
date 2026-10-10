# Goal — cmd-sem-wsl

- **Início:** 2026-10-10 19:17 · **Agente:** Claude (sessão interativa, /formato-curso-v6 ativo)
- **Tetos:** tempo ~8 h de trabalho · sem API (Codex só pela assinatura) · memória: testes com Playwright normais

## Resultado
OSWork v6.2 1.5.1: no Windows o aluno usa o **cmd** (sem WSL/Linux) das aulas 13 a 42 e 49; a VPS (módulo 8, aulas 43–48) continua Linux e abre com a tabela cmd → Linux. PT/EN/ES publicados.

Pedido do Nei (10/10/2026): "começa com cmd sem linux, depois vai pra uma VPS usando linux".

## Critérios de pronto (verificáveis)

**Função**
- [ ] `grep -liE 'wsl|ubuntu|sudo |apt |/home/|~/' aulas/aula-{13..42}.html aulas/aula-49.html` → vazio
- [ ] `grep -lE 'mkdir -p|\bcat |\bls\b|nano |python3|chmod|printf' aulas/aula-{13..42}.html aulas/aula-49.html` → vazio (exceto citação explícita da tabela cmd→Linux)
- [ ] `grep -c 'C:\\Users' aulas/aula-13.html aulas/aula-19.html` → ≥1 cada
- [ ] aula 43 (ou a 1ª aula do módulo 8 que entra na VPS) contém a tabela `dir→ls`, `type→cat`, `cls→clear`
- [ ] `node ~/.claude/skills/formato-curso-v6/scripts/auditar-curso.cjs curso.html` (e en/, es/) → 49 aulas, todas ≥9, sem falha nos critérios 7/8/10
- [ ] `node ~/.claude/skills/formato-curso-v6/scripts/testar-motor.cjs` ×3 → 26/26

**Regressão**
- [ ] blocos de código PT × EN/ES idênticos salvo trocas conhecidas (script de conferência em `context/`)
- [ ] `grep -c "\[Nome\|\[Resultado" landing.html` → 0
- [ ] aulas 1–12 e 43–48: diff só nos pontos que citam o terminal local (kicker/links intactos)

**Limite**
- [ ] tag `v1.4.1-wsl` existe no remoto (edição antiga recuperável)
- [ ] nenhum push de `main` antes do portão dos 3 idiomas
- [ ] nenhuma API além do GitHub; Codex só `codex exec` pela assinatura

**Teste rápido por ciclo:** montar-curso + auditar-curso no PT
**Teste completo no final:** montar → traduzir en es → auditar ×3 → testar-motor ×3 → conferência de código → leitor simulado nas aulas 13, 19, 38, 49
