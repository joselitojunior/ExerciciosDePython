pt = int(input('Digite o primeiro termo da \033[0;33mPA\033[m: '))
r = int(input('Digite a razão da \033[0;33mPA\033[m: '))
decimo = pt + (10 - 1) * r

if r > 0:
    while pt <= decimo:
        print(f'\033[1;97m{pt}\033[m')
        pt = pt + r
if r < 0:
    while pt >= decimo:
        print(f'\033[1;97m{pt}\033[m')
        pt = pt + r
if r == 0:
    for r0 in range(1,11):
        print(f'\033[1;97m{pt}\033[m')