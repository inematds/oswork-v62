#!/usr/bin/env python3
"""Depois de traduzir-curso.py: acerta nos en/ e es/ o que o tradutor não toca.
1. Endereço dos arquivos de treino: /materiais/treino/ -> /materiais/treino-en|es/.
2. Respostas do Windows dentro das telas de terminal (<span class="out">), que ficam em português,
   pelas mensagens reais do Windows em inglês e espanhol, e as linhas rem/→ do curso.
Uso (sempre depois de traduzir): python3 scripts/pos-traducao.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TROCAS = {
    'en': [
        ("'codex' não é reconhecido como um comando interno\nou externo, um programa operável ou um arquivo em lotes.",
         "'codex' is not recognized as an internal or external command,\noperable program or batch file."),
        (' O volume na unidade C não tem nome.', ' Volume in drive C has no label.'),
        (' O Número de Série do Volume é 1A2B-3C4D', ' Volume Serial Number is 1A2B-3C4D'),
        (' Pasta de C:\\Users\\denise', ' Directory of C:\\Users\\denise'),
        ('               0 arquivo(s)              0 bytes', '               0 File(s)              0 bytes'),
        ('               5 pasta(s)   80.000.000.000 bytes disponíveis', '               5 Dir(s)  80,000,000,000 bytes free'),
        ('        1 arquivo(s) copiado(s).', '        1 file(s) copied.'),
        ('4 arquivo(s) copiado(s)', '4 File(s) copied'),
        ('Comparando os arquivos meu-primeiro-projeto-antes\\AGENTS.md e MEU-PRIMEIRO-PROJETO\\AGENTS.md',
         'Comparing files meu-primeiro-projeto-antes\\AGENTS.md and MEU-PRIMEIRO-PROJETO\\AGENTS.md'),
        ('Comparando os arquivos meu-primeiro-projeto-antes\\README.md e MEU-PRIMEIRO-PROJETO\\README.MD',
         'Comparing files meu-primeiro-projeto-antes\\README.md and MEU-PRIMEIRO-PROJETO\\README.MD'),
        ('FC: nenhuma diferença encontrada', 'FC: no differences encountered'),
        ('  - Não envie nem publique nada.', '  - Do not send or publish anything.'),
        ('  - Todo resultado vem com a verificação que você observou.', '  - Every result comes with the verification you observed.'),
        ('  - Esta tarefa não autoriza publicar nada.', '  - This task does not authorize publishing anything.'),
        ('Instalado com êxito', 'Successfully installed'),
        ('Arquivo não encontrado', 'File Not Found'),
        ('O sistema não pode encontrar o arquivo especificado.', 'The system cannot find the file specified.'),
        ('rem fechou e abriu o cmd de novo', 'rem closed and reopened cmd'),
        ('rem fechou o cmd e abriu outro', 'rem closed cmd and opened a new one'),
        ('→ o navegador abre; entre com a conta do ChatGPT e volte ao cmd', '→ the browser opens; sign in with your ChatGPT account and come back to cmd'),
        ('Prompt de Comando', 'Command Prompt'),
    ],
    'es': [
        ("'codex' não é reconhecido como um comando interno\nou externo, um programa operável ou um arquivo em lotes.",
         "'codex' no se reconoce como un comando interno o externo,\nprograma o archivo por lotes ejecutable."),
        (' O volume na unidade C não tem nome.', ' El volumen de la unidad C no tiene etiqueta.'),
        (' O Número de Série do Volume é 1A2B-3C4D', ' El número de serie del volumen es: 1A2B-3C4D'),
        (' Pasta de C:\\Users\\denise', ' Directorio de C:\\Users\\denise'),
        ('               0 arquivo(s)              0 bytes', '               0 archivos              0 bytes'),
        ('               5 pasta(s)   80.000.000.000 bytes disponíveis', '               5 dirs  80.000.000.000 bytes libres'),
        ('        1 arquivo(s) copiado(s).', '        1 archivo(s) copiado(s).'),
        ('4 arquivo(s) copiado(s)', '4 archivo(s) copiado(s)'),
        ('Comparando os arquivos meu-primeiro-projeto-antes\\AGENTS.md e MEU-PRIMEIRO-PROJETO\\AGENTS.md',
         'Comparando archivos meu-primeiro-projeto-antes\\AGENTS.md y MEU-PRIMEIRO-PROJETO\\AGENTS.md'),
        ('Comparando os arquivos meu-primeiro-projeto-antes\\README.md e MEU-PRIMEIRO-PROJETO\\README.MD',
         'Comparando archivos meu-primeiro-projeto-antes\\README.md y MEU-PRIMEIRO-PROJETO\\README.MD'),
        ('FC: nenhuma diferença encontrada', 'FC: no se encontraron diferencias'),
        ('  - Não envie nem publique nada.', '  - No envíes ni publiques nada.'),
        ('  - Todo resultado vem com a verificação que você observou.', '  - Todo resultado viene con la verificación que observaste.'),
        ('  - Esta tarefa não autoriza publicar nada.', '  - Esta tarea no autoriza publicar nada.'),
        ('Instalado com êxito', 'Instalado correctamente'),
        ('Arquivo não encontrado', 'No se encuentra el archivo'),
        ('O sistema não pode encontrar o arquivo especificado.', 'El sistema no puede encontrar el archivo especificado.'),
        ('rem fechou e abriu o cmd de novo', 'rem cerró y volvió a abrir el cmd'),
        ('rem fechou o cmd e abriu outro', 'rem cerró el cmd y abrió otro'),
        ('→ o navegador abre; entre com a conta do ChatGPT e volte ao cmd', '→ se abre el navegador; entra con la cuenta de ChatGPT y vuelve al cmd'),
        ('rem Edite o .env localmente; nunca compartilhe valores.', 'rem Edita el .env localmente; nunca compartas los valores.'),
        ('rem Preencha ALLOWED_USER_IDS com seu ID e encerre a identificação.', 'rem Completa ALLOWED_USER_IDS con tu ID y termina la identificación.'),
        ('Prompt de Comando', 'Símbolo del sistema'),
    ],
}


def main():
    for lang, trocas in TROCAS.items():
        p = ROOT / lang / 'curso.html'
        s = p.read_text(encoding='utf-8')
        s = s.replace('/oswork-v62/materiais/treino/', f'/oswork-v62/materiais/treino-{lang}/')
        for a, b in trocas:
            s = s.replace(a, b)
        p.write_text(s, encoding='utf-8')
        sobras = [a for a, _ in trocas if a in s]
        print(f'{lang}: ok' + (f' · sobrou: {sobras}' if sobras else ''))


if __name__ == '__main__':
    main()
