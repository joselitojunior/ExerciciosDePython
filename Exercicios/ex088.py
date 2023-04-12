from random import randint
from time import sleep

palpites = list()
qnt = 0

print('\033[1;97m=' * 50)

while True:
    jogos = str(input('\033[1;97mQuantidade de \033[36mjogos: '))
    if jogos.isnumeric():
        jogos = int(jogos)
        break
for c in range(jogos):
    palpites.append(list())
    for d in range(6):
        n = randint(1, 60)
        if len(palpites[c]) >= 1:
            while n in palpites[c]:
                qnt += 1
                n = randint(1, 60)
        palpites[c].append(n)
    palpites[c].sort()
    if c > 0:
        while palpites[c] in palpites[0:len(palpites) - 1]:
            palpites[c].clear()
            for d in range(6):
                n = randint(1, 60)
                if len(palpites[c]) >= 1:
                    while n in palpites[c]:
                        qnt += 1
                        n = randint(1, 60)
                palpites[c].append(n)
            palpites[c].sort()

print('\033[1;97m=' * 50)
for c in range(jogos):
    if c == 0:
        print(f'\033[1;97m{c + 1}º palpite: \033[33m{palpites[c]}')
    else:
        sleep(0.6)
        print(f'\033[1;97m{c + 1}º palpite: \033[33m{palpites[c]}')
print(F'\n\033[36m{"BOA SORTE!!!":^50}')
print('\033[1;97m=' * 50)
