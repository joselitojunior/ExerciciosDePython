from datetime import date
from time import sleep

n = int(input('Digite o \033[1;36mANO\033[m do seu nascimento: '))
ano = date.today().year
idade = ano - n

if idade == 18:
    print('\n'+'\033[1;33m=\033[m' * 150, '\nVocê deve se alistar \033[1;4;33mESSE\033[m ano!\n'+'\033[1;33m=\033[m' * 150)
elif idade < 18:
    print('\n'+'\033[1;32m=\033[m' * 150, '\nVocê ainda \033[1;4;32mVAI\033[m se alistar!')
    restante = 18 - idade
    sleep(0.9)
    print('\n.')
    sleep(0.9)
    print('.')
    sleep(0.9)
    print('.')
    sleep(1.5)
    if restante > 1:
        print(f'\nFaltam \033[1;32m{restante} anos\033[m para o seu alistamento \033[4mobrigatório\033[m no serviço militar.')
        print('\033[1;32m=\033[m' * 150)
    elif restante == 1:
        print(f'\nFalta \033[1;32m{restante} ano\033[m para o seu alistamento \033[4mobrigatório\033[m no serviço militar.')
        print('\033[1;32m=\033[m' * 150)
elif idade > 18:
    restante = idade - 18
    print('\033[1;31m=\033[m' * 150 + '\nJá \033[1;4;31mPASSOU\033[m o tempo para o seu alistamento.')
    sleep(0.9)
    print('\n.')
    sleep(0.9)
    print('.')
    sleep(0.9)
    print('.')
    sleep(1.5)
    if restante > 1:
        print(f'\nSe passaram \033[1;31m{restante} anos\033[m após o ano que você deveria ter feito o seu alistamento.')
        print('\033[1;31m=\033[m' * 150)
    elif restante == 1:
        print(f'\nSe passou \033[1;31m{restante} ano\033[m após o ano que você deveria ter feito o seu alistamento.')
        print('\033[1;31m=\033[m' * 150)
