qnt1 = 0
qnt2 = 0
neg = 0

print('\033[1;97m=' * 50)
matriz = [[], [], []]
for c in range(9):
    while True:
        n = str(input(f'\033[1;97mInsira o número \033[35m[{qnt1 + 1}, {qnt2 + 1}]\033[97m: '))
        if len(n) != 0:
            if n[0] == '-':
                neg = 1
                n = n.replace('-', '')
            if n.isnumeric():
                n = int(n)
                if neg == 1:
                    neg = 0
                    n = n * -1
                if qnt1 == 0:
                    matriz[0].append(n)
                elif qnt1 == 1:
                    matriz[1].append(n)
                elif qnt1 == 2:
                    matriz[2].append(n)
                qnt2 += 1
                if qnt2 == 3:
                    qnt2 = 0
                    qnt1 += 1
                break
print('\033[1;97m=' * 50)
print(f'\033[1;34m{"MATRIZ:":^50}\033[97m')
qnt1 = 0
qnt2 = 0
for c in range(9):
    if qnt2 == 0:
        print(' ' * 14, end='')
    print(f'[\033[34m{matriz[qnt1][qnt2]:^5}\033[97m]', end='')
    if qnt2 == 2:
        print('')
    qnt2 += 1
    if qnt2 == 3:
        qnt2 = 0
        qnt1 += 1
print('\033[1;97m=' * 50)
