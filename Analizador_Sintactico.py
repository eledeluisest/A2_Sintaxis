# Programa base

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk import load_parser
cp = load_parser('gramatica_base.fcfg')
infile = open('materialpracticasintaxis/textos.txt', encoding='utf-8')
# Mostramos por pantalla lo que leemos desde el fichero
for i, line in enumerate(infile):
    print(line)
    tokens=line.split()
    trees = cp.parse(tokens)
    for tree in trees:
        print(tree)
        print("="*10+"OK"+"="*10)
        # tree.draw()
infile.close()

