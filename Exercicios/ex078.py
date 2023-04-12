num = list()
menor = 0
maior = 0
pmen = list()
pmai = list()

print('\033[1;97m-\033[m' * 50)
for c in range(5):
    num.append(int(input(f'\033[1;97mDigite o \033[4m{c + 1}\033[m\033[1;97mº número:\033[m ')))
    if c == 0:
        menor = num[c]
        maior = num[c]
        pmen.append(c)
        pmai.append(c)
    else:
        if num[c] < menor:
            menor = num[c]
            pmen.clear()
            pmen.append(c)
        elif num[c] == menor:
                pmen.append(c)
        if num[c] > maior:
            maior = num[c]
            pmai.clear()
            pmai.append(c)
        elif num[c] == maior:
            pmai.append(c)
print('\033[1;97m-\033[m' * 50)
print(f'\033[1;97mLISTA: \033[1;35m{num}\n')
print(f'\033[1;97mMENOR número: \033[1;34m{menor}')
print(f'\033[1;97mPosição:\033[m ', end='')
for d in range(0, len(pmen)):
    if d == len(pmen) - 1:
        print(f'\033[1;34m{pmen[d]}\033[1;97m.')
    elif d == len(pmen) - 2:
        print(f'\033[1;34m{pmen[d]}\033[1;97m', end=' \033[1;97me ')
    else:
        print(f'\033[1;34m{pmen[d]}\033[1;97m', end=', ')
print(f'\n\033[1;97mMAIOR número: \033[1;34m{maior}')
print(f'\033[1;97mPosição: \033[m', end='')
for d in range(0, len(pmai)):
    if d == len(pmai) - 1:
        print(f'\033[1;34m{pmai[d]}\033[1;97m.')
    elif d == len(pmai) - 2:
        print(f'\033[1;34m{pmai[d]}\033[1;97m', end=' \033[1;97me ')
    else:
        print(f'\033[1;34m{pmai[d]}\033[1;97m', end=', ')
print('-' * 50)
