r1 = float(input('Digite a medida da 1ª reta: '))
r2 = float(input('Digite a medida da 2ª reta: '))
r3 = float(input('Digite a medida da 3ª reta: '))

if r1 >= r2 and r1 >= r3:
    if r2 + r3 > r1:
        print('\033[1;32mDá para fazer um triângulo!\033[m')
    else:
        print('\033[0;31mNão dá pra fazer um triângulo.\033[m')

if r2 > r1 and r2 >= r3:
    if r1 + r3 > r2:
        print('\033[1;32mDá para fazer um triângulo!\033[m')
    else:
        print('\033[0;31mNão dá pra fazer um triângulo.\033[m')

if r3 > r1 and r3 > r2:
    if r1 + r2 > r3:
        print('\033[1;32mDá para fazer um triângulo!\033[m')
    else:
        print('\033[0;31mNão dá pra fazer um triângulo.\033[m')
