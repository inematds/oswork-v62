#!/usr/bin/env python3
"""Pré-carrega o cache do traduzir-curso.py (i18n/en.json, i18n/es.json) com as traduções JÁ REVISADAS do OSWork v2.

Uso (na pasta do curso, antes do traduzir-curso.py):  python3 scripts/semear-traducao.py [--v2 ~/projetos/oswork]
O v2 guarda o catálogo em i18n/source.json ({id: {"source": texto PT}}) e as traduções em i18n/{en,es}.json ({id: texto}).
O cache do v6 é {unidade PT (HTML interno escapado): tradução}. Semeia só textos sem marcação (o complementar gera
<p>{texto}</p>); trechos em que o complementar.py marcou um termo com .gterm continuam indo para o tradutor.
Nunca sobrescreve uma entrada que já está no cache.
"""
import html, json, pathlib, sys

base = pathlib.Path(".").resolve()
v2 = pathlib.Path(sys.argv[sys.argv.index("--v2") + 1] if "--v2" in sys.argv else "~/projetos/oswork").expanduser()
fonte = json.loads((v2 / "i18n" / "source.json").read_text(encoding="utf-8"))
(base / "i18n").mkdir(exist_ok=True)
for lang in ("en", "es"):
    tr = json.loads((v2 / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
    dest = base / "i18n" / f"{lang}.json"
    cache = json.loads(dest.read_text(encoding="utf-8")) if dest.exists() else {}
    novos = 0
    for k, v in fonte.items():
        if v.get("kind") != "text" or k not in tr:
            continue
        pt = html.unescape(v["source"]).strip()
        chave = html.escape(pt, quote=False)
        if chave not in cache and tr[k].strip():
            cache[chave] = html.escape(html.unescape(tr[k]).strip(), quote=False)
            novos += 1
    dest.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{lang}: {novos} traduções revisadas do v2 semeadas ({len(cache)} no cache)")
