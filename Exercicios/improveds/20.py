from mdl.tudo import *
from random import shuffle

linha__()
lista = list()
for c in range(4):
    lista.append(str(input(f'{branco}Digite o nome do {ciano}{c + 1}º{branco} aluno: ')).strip().title())
    linha_()

shuffle(lista)
print(f'{branco}A ordem de apresentação dos alunos é: ')
for pos, aluno in enumerate(lista):
    print(f'{azul}{pos + 1}º{branco}: {aluno}')
linha__()
