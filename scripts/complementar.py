#!/usr/bin/env python3
"""Gera o material complementar de cada aula a partir do OSWork v2 — texto integral, sem reescrever.

Uso (na pasta do curso):  python3 scripts/complementar.py [--v2 ~/projetos/oswork]
- Aula N = tópico ((N-1)//6 + 1, (N-1)%6 + 1) do v2 (8 módulos × 6 tópicos, na ordem do v2).
- Conteúdo: O que é · Por que aprender · Conceitos-chave · Na prática · ação do tópico (Faça/Evite, Sequência ou
  Experimente agora, como no build do v2) · figura do tópico, quando houver.
- A última aula de cada módulo recebe também o fechamento do módulo no v2: laboratório, bloco do laboratório,
  critério de pronto, rubrica, "Confira o que ficou", resumo do módulo e fontes.
- Substitui o trecho entre <!--COMP--> e <!--/COMP--> em aulas/aula-N.html (aula sem os marcadores é ignorada).
- Termo de context/glossario.json que aparece no complementar sem .gterm na aula ganha .gterm na 1ª ocorrência
  (fora de link, pre e code); se só aparece em link, entra numa linha "Termos desta seção".
Idempotente. Lê o build.py do v2 como texto (não o executa: ele grava arquivos).
"""
import ast, html, json, pathlib, re, sys

base = pathlib.Path(".").resolve()
v2 = pathlib.Path(sys.argv[sys.argv.index("--v2") + 1] if "--v2" in sys.argv else "~/projetos/oswork").expanduser()
sys.path.insert(0, str(v2 / "conteudo"))
import modulos as M  # noqa: E402

build = (v2 / "scripts" / "build.py").read_text(encoding="utf-8")
def lit(pat):
    m = re.search(pat, build, re.S | re.M)
    if not m:
        sys.exit(f"build.py do v2 mudou: não achei {pat[:40]!r}")
    return ast.literal_eval(m.group(1))
SOURCES = lit(r"^SOURCES=(\[.*?\])\n")
SNIPPETS = lit(r"^SNIPPETS=(\[.*?\])\n")
RUBRICA = lit(r"for row in (\[\('Escopo'.*?\)\]):")
FONTES_POR_MOD = lit(r"sourcebox\((\[\[.*?\]\])\[i\]\)")
EVITE = lit(r'\{E\((\["Aceitar.*?"\])\[j==4\]\)\}')
GLOS = {k: v for k, v in json.loads((base / "context" / "glossario.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}

E = lambda s: html.escape(s, quote=False)

def figura(spec):
    if not spec:
        return ""
    if spec["kind"] == "grid":
        itens = "".join(f"<li>{E(x)}</li>" for x in spec["items"])
    elif spec["kind"] == "columns":
        itens = "".join(f"<li><b>{E(a)}</b> — {E(b)}</li>" for a, b in spec["items"])
        itens += "".join(f"<li>{E(x)}</li>" for x in spec.get("base", []))
    else:  # tree, flow etc.: rótulos em lista, na ordem do v2
        itens = "".join(f"<li>{E(x if isinstance(x, str) else x[0])}</li>" for x in spec.get("items", []))
    return f'<figure class="comp-fig"><ul>{itens}</ul><figcaption>{E(spec["caption"])}</figcaption></figure>'

def topico(i, j):
    tp = M.MODULES[i]["topics"][j - 1]
    h = (f'<section class="comp-sec"><h3>O que é</h3><p>{E(tp["what"])}</p><h3>Por que aprender</h3><p>{E(tp["why"])}</p>'
         f'<h3>Conceitos-chave</h3><p>{E(tp["keys"])}</p><h4>Na prática</h4><p>{E(tp["example"])}</p>')
    if j in (1, 4):
        h += f'<h4>✓ Faça</h4><p>{E(tp["action"])}</p><h4>✗ Evite</h4><p>{E(EVITE[j == 4])}</p>'
    elif j == 3:
        h += (f'<h4>Sequência para experimentar</h4><ol><li>Prepare uma cópia de treino.</li><li>{E(tp["action"])}</li>'
              '<li>Registre o resultado observado e a próxima correção.</li></ol>')
    else:
        h += f'<h4>Experimente agora</h4><p>{E(tp["action"])}</p>'
    return h + figura(M.FIGURES.get((i, j))) + "</section>"

def fechamento(i):
    m = M.MODULES[i]
    passos = "".join(f"<li>{E(s)}</li>" for s in m["steps"])
    rub = "".join(f"<li><b>{E(a)}</b> — {E(b)} <i>Se não passou:</i> {E(c)}</li>" for a, b, c in RUBRICA)
    fontes = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in (SOURCES[k] for k in FONTES_POR_MOD[i]))
    resumo = "".join(f'<li>{E(tp["keys"])}</li>' for tp in m["topics"])
    return (f'<section class="comp-sec"><h3>Laboratório do módulo: {E(m["lab"])}</h3>'
            '<p>Use arquivos fictícios e uma pasta de treino. As práticas com instalação, Telegram ou VPS podem exigir tempo adicional para cadastro e configuração.</p>'
            f'<ol>{passos}</ol><h4>{E(SNIPPETS[i][0])}</h4>'
            '<p>Leia o bloco antes de usar. Campos como Seu Nome e usuario@ip-da-vps são exemplos para adaptar; comandos administrativos pertencem somente ao seu ambiente de treino.</p>'
            f'<pre><code>{E(SNIPPETS[i][1])}</code></pre>'
            f'<h4>Critério de pronto</h4><p>{E(m["goal"])} Registre o arquivo produzido, o teste executado e o resultado observado.</p></section>'
            '<section class="comp-sec"><h3>Critérios para revisar sua entrega</h3><p>Use esta rubrica depois do laboratório. Cada linha pede uma evidência; marcar leitura não significa que a prática foi executada.</p>'
            f'<ul>{rub}</ul></section>'
            f'<section class="comp-sec"><h3>Confira o que ficou</h3><p>{E(m["check"])}</p>'
            f'<details class="mais"><summary>Ver resposta comentada</summary><p>{E(m["answer"])}</p><p>Se sua resposta foi diferente, volte ao tópico correspondente e escreva a diferença em uma frase. A checagem não bloqueia seu estudo.</p></details>'
            f'<h4>Resumo do módulo</h4><ul>{resumo}</ul></section>'
            '<section class="comp-sec"><h3>Consulte a fonte</h3><p class="comp-fontes">Ferramentas verificadas em 20/09/2026; nomes de telas e disponibilidade podem mudar.</p>'
            f'<ul class="comp-fontes">{fontes}</ul></section>')

def rx(forma):
    return re.compile(r"(?<![\w])" + re.escape(forma) + r"(?![\w])", re.I)

def marca_termos(comp, nucleo):
    definidos = [re.sub(r"<[^>]+>", "", t) for t in re.findall(r'<span class="gterm"[^>]*>(.*?)</span>', nucleo, re.S)]
    so_em_link = []
    for k, g in GLOS.items():
        for forma in g["formas"]:
            r = rx(forma)
            if any(r.search(d) for d in definidos):
                continue
            partes, pilha, feito, visto = re.split(r"(<[^>]+>)", comp), [], False, False
            for n, p in enumerate(partes):
                if p.startswith("<"):
                    t = re.match(r"</?([a-z0-9]+)", p)
                    if t and t.group(1) in ("a", "pre", "code", "span", "summary"):
                        if p.startswith("</"):
                            if pilha:
                                pilha.pop()
                        else:
                            pilha.append(t.group(1))
                    continue
                if not r.search(p):
                    continue
                visto = True
                if pilha:
                    continue
                partes[n] = r.sub(lambda m: f'<span class="gterm" data-def="{html.escape(g["def"])}" data-gl="{k}">{m.group(0)}</span>', p, count=1)
                feito = True
                break
            comp = "".join(partes)
            if feito:
                definidos.append(forma)
            elif visto:
                so_em_link.append((k, forma))
    if so_em_link:
        extra = ", ".join(f'<span class="gterm" data-def="{html.escape(GLOS[k]["def"])}" data-gl="{k}">{E(f)}</span>' for k, f in so_em_link)
        comp = comp[: comp.rindex("</details>")] + f'<p class="comp-termos">Termos desta seção: {extra}.</p></details>'
    return comp

feitas = 0
for p in sorted((base / "aulas").glob("aula-*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
    s = p.read_text(encoding="utf-8")
    if "<!--COMP-->" not in s:
        continue
    n = int(re.search(r"\d+", p.stem).group())
    i, j = (n - 1) // 6, (n - 1) % 6 + 1
    if i >= len(M.MODULES):
        sys.exit(f"{p.name}: não há tópico correspondente no v2")
    tp = M.MODULES[i]["topics"][j - 1]
    corpo = topico(i, j) + (fechamento(i) if j == 6 else "")
    resumo = "Texto completo do tópico no OSWork v2" + (" e fechamento do módulo" if j == 6 else "") + ". Não conta no tempo da aula."
    comp = (f'<details class="complementar">\n  <summary>Material complementar · {E(tp["title"])}<small>{resumo}</small></summary>\n'
            f'  {corpo}\n</details>\n')
    nucleo = re.sub(r"<!--COMP-->.*?<!--/COMP-->", "", s, flags=re.S)
    comp = marca_termos(comp, nucleo)
    s = re.sub(r"<!--COMP-->.*?<!--/COMP-->", lambda _: "<!--COMP-->\n" + comp + "<!--/COMP-->", s, flags=re.S)
    p.write_text(s, encoding="utf-8")
    feitas += 1
    print(f"{p.name}: módulo {i + 1}, tópico {j} — {tp['title']}" + (" + fechamento do módulo" if j == 6 else ""))
print(f"{feitas} aulas com complementar")
