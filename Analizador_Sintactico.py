# Programa base

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk import load_parser
cp = load_parser('gramatica_base.fcfg')
infile = open('materialpracticasintaxis/textos.txt', encoding='utf-8')
# Mostramos por pantalla lo que leemos desde el fichero
# Si pinta es verdader pinta el arbol
pinta = False
with open('resutado.txt', 'w') as f:
    f.write('')
for i, line in enumerate(infile):
    print(line)
    with open('resutado.txt', 'a') as f:
        f.write(line)
    tokens=line.split()
    trees = cp.parse(tokens)
    for tree in trees:
        print(tree)
        with open('resutado.txt', 'a') as f:
            f.write(tree.pformat()+"\n")
        if pinta:
            tree.draw()
    with open('resutado.txt', 'a') as f:
        f.write("\n")
        f.write("=" * 50)
        f.write("\n")
infile.close()

