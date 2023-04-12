print('\033[1;33m-\033[m' * 160)
print(F'\033[1;34m{"TABELA DO BRASILEIRÃO":^160}\033[m')
print('\033[1;97m-\033[m' * 160)
tupla = ('Fortaleza',
         'Athletico-PR',
         'Atlético-MG',
         'Bragantino',
         'Fluminense',
         'Palmeiras',
         'Bahia',
         'Atlético-GO',
         'Flamengo',
         'Corinthias',
         'Sport Recife',
         'Ceará SC',
         'Santos',
         'Internacional',
         'Cuiabá',
         'São Paulo',
         'Chapecoense',
         'Juventude',
         'América-MG',
         'Grêmio',)
for pos in range(0,20):
    if tupla[pos] == 'Chapecoense':
            p = pos + 1
print(f'\033[1;97mOs cinco primeiros são: \033[1;34m{tupla[0]}, {tupla[1]}, '
      f'{tupla[2]}, {tupla[3]} \033[1;97me \033[1;34m{tupla[4]}\033[1;97m.')
print(f'\033[1;97mOs quatro últimos são: \033[1;34m{tupla[-4]}, {tupla[-3]}, '
      f'{tupla[-2]}, \033[1;97me \033[1;34m{tupla[-1]}\033[1;97m.')
tupla = sorted(tupla)
print('Em ordem alfabética:', end=' ')
for c in range(0,20):
    if c < 18:
        print(f'\033[1;34m{tupla[c]}', end=', ')
    elif c == 18:
        print(f'\033[1;34m{tupla[c]}', end=' ')
    else:
        print(f'\033[1;97me \033[1;34m{tupla[c]}\033[1;97m.')
print(f'O time Chapecoense está na posição: \033[1;34m{p}\033[m')
print('\033[1;32m-\033[m' * 160)
