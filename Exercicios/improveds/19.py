from mdl.tudo import *
from random import choice

linha__()
lista = list()
for c in range(4):
    aluno = str(input(f'{branco}Digite o nome do {ciano}{c + 1}º{branco} aluno: ')).strip().title()
    linha_()
    lista.append(aluno)

print(f'{branco}O aluno que deverá apagar o quadro é o: {ciano}{choice(lista)}')
linha__()
