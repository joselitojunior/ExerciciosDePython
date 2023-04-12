from random import randint
from operator import itemgetter
dado = dict()
ranking = dict()
qnt = 0

print('\033[1;97m'+'=' * 50)
print('         \033[1;97mDIGITE "\033[32mjogar\033[97m" PARA JOGAR O DADO')
print('\033[1;97m'+'=' * 50)
while True:
    if str(input('\033[1;97m> ')) == 'jogar':
        qnt += 1
        dado[f'numero{qnt}'] = randint(1, 6)
        print(dado[f'numero{qnt}'], '\n')
    if qnt == 4:
        break
print('\033[1;97m'+'=' * 50)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\033[33m{i + 1}º lugar:\033[97m {v[0]} com o número {v[1]}')
print('\033[1;97m'+'=' * 50)
