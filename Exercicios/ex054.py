from datetime import date

anoatual = date.today().year
qnt = 0

for pessoas in range(1, 8):
    ano = int(input(f'\033[1;97mDigite o ano do nascimento da {pessoas}ª pessoa: \033[m'))
    if ano <= anoatual - 18:
        qnt += 1

qntm = 7 - qnt

if qnt > 1 or qnt == 0:
    print(f'\n\033[1;32m{qnt} pessoas são de maiores.\033[m')
else:
    print(f'\n\033[1;32m{qnt} pessoa é de maior.\033[m')
if qntm > 1 or qntm == 0:
    print(f'\033[1;31m{qntm} pessoas são de menores.\033[m')
else:
    print(f'\033[1;31m{qntm} pessoa é de menor.\033[m')
