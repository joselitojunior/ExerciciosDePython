from mdl.tudo import *
from datetime import datetime

ano = 0
ano_atual = datetime.today().year
linha__()
while True:
    try:
        ano = int(input(f'{branco}Digite seu ano de nascimento: '))
    except:
        continue
    else:
        break
linha_()
idade = ano_atual - ano
print(f'{branco}Idade: {amarelo}{idade}{branco} anos.')
print(f'{branco}Categoria: ', end=f'{azul}')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
linha__()
