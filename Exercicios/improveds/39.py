from mdl.tudo import *
from datetime import datetime

ano_atual = datetime.today().year
ano = 0
linha__()
while True:
    try:
        ano = int(input(f'{branco}Digite o ano de seu nascimento: '))
    except:
        continue
    else:
        break
linha_()
if ano_atual - ano == 18:
    print(f'{branco}Você deve se alistar ao exército {verde}este ano{branco}!')
elif ano_atual - ano < 18:
    restante = 18 - (ano_atual - ano)
    print(f'{branco}Você deve se alistar ao exército em {azul}{ano_atual + restante}{branco}.')
elif ano_atual - ano > 18:
    atraso = (ano_atual - ano) - 18
    print(f'{branco}Você deveria ter se alistado em {azul}{ano_atual - atraso}{branco}...')
linha__()
