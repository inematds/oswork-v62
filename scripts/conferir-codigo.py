#!/usr/bin/env python3
"""Confere se a tradução não estragou os comandos: compara, aula por aula, os blocos copiáveis
(pre.pcode) do PT com os do EN e do ES. Compara só o "esqueleto" de cada linha: o comando,
as opções (/b, -e, --id), os caminhos com \\ ou %USERPROFILE% e os endereços http.
Uso: python3 scripts/conferir-codigo.py   (sai com 1 se houver diferença)
"""
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CMDS = r'(?:cd|mkdir|dir|type|copy|xcopy|move|ren|del|notepad|findstr|fc|curl|tar|explorer|winget|npm|codex|git|gh|ssh|ssh-keygen|py|python3|ls|cat|grep|sudo|nano|chmod|cp)'
# os arquivos de treino têm uma pasta por idioma
TROCAS = {'en': [('/materiais/treino-en/', '/materiais/treino/')], 'es': [('/materiais/treino-es/', '/materiais/treino/')]}


def blocos(arq):
    s = arq.read_text(encoding='utf-8')
    out = {}
    for sec in re.finditer(r'<section class="view" id="v-aula-(\d+)".*?(?=<section class="view"|\Z)', s, re.S):
        n = sec.group(1)
        pcs = re.findall(r'<pre class="pcode">(.*?)</pre>', sec.group(0), re.S)
        out[n] = [html.unescape(re.sub(r'<[^>]+>', '', p)) for p in pcs]
    return out


def esqueleto(bloco, lang='pt'):
    for a, b in TROCAS.get(lang, []):
        bloco = bloco.replace(a, b)
    linhas = []
    for l in bloco.splitlines():
        l = l.strip()
        m = re.match(CMDS + r'\b', l)
        if not m:
            continue
        toks = re.findall(r'%USERPROFILE%[^\s"]*|https?://\S+|(?<!\w)--?[\w-]+|(?<=\s)/[a-z]\b|\S*\\\S*', l)
        linhas.append(m.group(0) + ' ' + ' '.join(toks))
    return linhas


def main():
    pt = blocos(ROOT / 'curso.html')
    erros = 0
    for lang in ('en', 'es'):
        tr = blocos(ROOT / lang / 'curso.html')
        for n, bl in pt.items():
            a = [esqueleto(b) for b in bl]
            b = [esqueleto(x, lang) for x in tr.get(n, [])]
            if a != b:
                erros += 1
                print(f'{lang} aula {n}: blocos diferentes')
                for x, y in zip(a, b):
                    if x != y:
                        print('  PT:', x)
                        print(f'  {lang.upper()}:', y)
                if len(a) != len(b):
                    print(f'  quantidade de blocos: PT {len(a)} × {lang} {len(b)}')
    print('OK: comandos iguais nos três idiomas' if not erros else f'{erros} aula(s) com diferença')
    sys.exit(1 if erros else 0)


if __name__ == '__main__':
    main()
