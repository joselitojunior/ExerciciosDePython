n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais outro número:' ))

if n1 >= n2 and n1 >= n3:
    print(f'O maior número é: \033[0;32m{n1:.0f}\033[m')

if n2 > n1 and n2 >= n3:
    print(f'O maior número é: \033[0;32m{n2:.0f}\033[m')

if n3 > n1 and n3 > n2:
    print(f'O maior número é: \033[0;32m{n3:.0f}\033[m')

if n1 <= n2 and n1 <= n3:
    print(f'O menor número é: \033[0;31m{n1:.0f}\033[m')

if n2 < n1 and n2 <= n3:
    print(f'O menor número é \031[0;32m{n2:.0f}\033[m')

if n3 < n1 and n3 < n2:
    print(f'O menor número é: \031[0;32m{n3:.0f}\033[m')
