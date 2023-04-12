print('-' * 50)
from random import randint

lista = []
menor = 0
maior = 0

for c in range(5):
    al = randint(0, 100)
    lista = lista + [al]
    if c == 0:
        menor = al
        maior = al
    elif al < menor:
        menor = al
    elif al > maior:
        maior = al

tupla = tuple(lista)
print(f'\033[1;97mOs números gerados foram: \033[1;34m{tupla}')

print(f'\033[1;97mO menor valor é: \033[1;34m{menor}')
print(f'\033[1;97mO maior valor é: \033[1;34m{maior}\033[m')
print('-' * 50)
