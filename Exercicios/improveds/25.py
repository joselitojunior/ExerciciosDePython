from mdl.tudo import *

linha__()
nome = str(input(f'{branco}Digite um nome: ')).strip().lower().split()
linha_()
if 'silva' in nome:
    print(f'{verde}Há{branco} "Silva" no nome.')
else:
    print(f'{vermelho}Não há{branco} "Silva" no nome.')
linha__()
