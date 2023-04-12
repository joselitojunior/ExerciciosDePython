from mdl.tudo import *

linha__()
nome = str(input(f'{branco}Digite um nome: ')).strip().title().split()
linha_()
print(f'{branco}Primeiro nome: {verde}{nome[0]}\n'
      f'{branco}Último nome: {vermelho}{nome[-1]}')
linha__()
