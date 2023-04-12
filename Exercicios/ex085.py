neg = 0
numeros = [[], []]

print('\033[1;97m=' * 50)

for c in range(7):
    while True:
        n = str(input(f'\033[1;97mDigite o {c + 1}º \033[34mnúmero: '))
        if len(n) != 0:
            if '-' in n[0]:
                neg = 1
                n = n.replace('-', '', 1)
            if n.isnumeric():
                n = int(n)
                if neg == 1:
                    n = n * -1
                    neg = 0
                if n % 2 == 0:
                    numeros[0].append(n)
                else:
                    numeros[1].append(n)
                break
numeros[0].sort()
numeros[1].sort()
print('\033[1;97m=' * 50)

print(f'\033[1;97mPares:\033[34m ', end='')
for i, v in enumerate(numeros[0]):
    if i == len(numeros[0]) - 1:
        print(f'{v}\033[m\033[97m.')
    elif i == len(numeros[0]) - 2:
        print(v, end=' \033[97me\033[34m ')
    else:
        print(v, end='\033[97m,\033[34m ')
print(f'\033[1;97mÍmpares:\033[34m ', end='')
for i, v in enumerate(numeros[1]):
    if i == len(numeros[1]) - 1:
        print(f'{v}\033[m\033[97m.')
    elif i == len(numeros[1]) - 2:
        print(v, end=' \033[97me\033[34m ')
    else:
        print(v, end='\033[97m,\033[34m ')
print('\033[1;97m=' * 50)
