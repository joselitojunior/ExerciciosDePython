from random import randint

n = -1
nc = (randint(0,10))
p = 0

while n != nc:
    n = int(input('\033[1;97mDigite um número de 0 à 10:\033[m '))
    p += 1
    if n != nc:
        print(f'\033[1;31mVocê errou... Tente novamente!\033[m\n')
print(f'\n\033[1;97mPARABÉNS! VOCÊ ACERTOU O NÚMERO \033[1;32m{nc}\033[m\033[1;97m!!!\033[m')
if p == 1:
    print(f'\033[1;97mQue sorte! Você acertou no PRIMEIRO palpite :)\033[m')
else:
    print(f'\033[1;97mVocê deu \033[4m{p}\033[m\033[1;97m palpites até acertar.\033[m')
