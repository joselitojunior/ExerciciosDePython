from random import randint
n = int(input('Digite um número de 0 à 5: '))

nc = (randint(0,5))

if nc == n:
    print(f'\033[1;32mPARABÉNS! VOCÊ ACERTOU O NÚMERO {nc}!!!\033[m')
else:
    print(f'\033[0;31mVocê errou... O número escolhido pelo computador era {nc} :(\033[m')
