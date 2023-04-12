n = int(input('Digite um número: '))

if n // 2 == n / 2:
    print('O número é \033[0;32mpar\033[m!')
else:
    print('O número é \033[0;33mímpar\033[m!')
