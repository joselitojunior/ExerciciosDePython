n = int(input('\033[1;97mDigite um número inteiro:\033[m '))

s = 0       #soma começa com 0

if n < 0:       #negativo para positivo
    n = n * -1

if n > 1:
    for c in range(1, n+1):
        if n % c == 0:
            s = s + 1
    if s == 2:
        print('\033[1;32;107mÉ um número primo!\033[m')
    else:
        print('\033[0;31mNão é um número primo.\033[m')

else:
    print('\033[0;31mNão é um número primo.\033[m')
