# OSWork v6.2 — Sua IA precisa de um sistema

Curso do INEMA.CLUB PRO no `formato-curso-v6` (6.2, perfil técnico). Conteúdo **integral do OSWork v2**
(`inematds/oswork`): uma aula curta por tópico do v2, com o texto completo do tópico no material complementar
de cada aula. O OSWork v6 (7 aulas para leigo) é outro curso e continua separado.

- Abrir: `landing.html` ou `curso.html#trilha` — funciona offline e guarda o progresso no navegador.
- Estado atual: **curso completo — 8 módulos, 49 aulas** (auditoria 10/10 em todas; aula 49 = SSH, gh e GitHub Pages). Ainda sem teste com pessoas reais.

## Mais no INEMA.CLUB

- [Ficha deste curso](https://www.inema.club/cursos/288-oswork-v6-2-sua-ia-precisa-de-um-sistema/)
- [Guia: como aprender inteligência artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.inema.club/cursos/)

## Como é feito

| Arquivo | Papel |
|---|---|
| `aulas/aula-N.html` | núcleo da aula (≤900 palavras, ~15 min), escrito à mão |
| `scripts/complementar.py` | gera o material complementar entre `<!--COMP-->` e `<!--/COMP-->` direto do `modulos.py` do v2 |
| `context/glossario.json` | uma definição por termo técnico; o complementar marca os termos com ela |
| `scripts/semear-traducao.py` | pré-carrega EN/ES com as traduções revisadas do v2 |
| `scripts/pos-traducao.py` | depois de traduzir: links dos arquivos de treino por idioma e mensagens do Windows em EN/ES nas telas de terminal |
| `scripts/conferir-codigo.py` | confere que os comandos copiáveis são iguais em PT, EN e ES |
| `materiais/treino{,-en,-es}/` | arquivos de treino que as aulas baixam com `curl` |
| `context/cmd-convencoes.md` | tabela Bash → cmd usada na edição 1.5 (Windows no cmd, VPS em Linux) |
| `curso.html` | montado — não editar à mão |

Atualizar (atenção: desde a 1.5.1 o material complementar das aulas 13–49 foi adaptado ao cmd à mão; rodar `complementar.py` volta o texto do v2 com Bash/WSL): `python3 scripts/complementar.py` → `python3 ~/.claude/skills/formato-curso-v6/scripts/montar-curso.py .`
→ `python3 scripts/semear-traducao.py` → `python3 ~/.claude/skills/formato-curso-v6/scripts/traduzir-curso.py . en es`
→ `python3 scripts/pos-traducao.py` → `python3 scripts/conferir-codigo.py`
→ `auditar-curso.cjs` e `testar-motor.cjs` em `curso.html`, `en/curso.html` e `es/curso.html`.

<!-- inema-backlink:v1 -->
## Mais no INEMA.CLUB

- [Ficha completa deste curso](https://www.inema.club/cursos/288-oswork-v6-2-sua-ia-precisa-de-um-sistema/)
- [Guia: como aprender inteligência artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.inema.club/cursos/)
<!-- /inema-backlink:v1 -->
