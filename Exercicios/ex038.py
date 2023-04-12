n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O \033[0;34mprimeiro\033[m número (\033[0;34m{n1}\033[m) é \033[4mMAIOR\033[m que'
          f' o \033[0;33msegundo\033[m (\033[0;33m{n2}\033[m).')
elif n1 < n2:
    print(f'O \033[0;33msegundo\033[m número (\033[0;33m{n2}\033[m) é \033[4mMAIOR\033[m que'
          f' o \033[0;34mprimeiro\033[m (\033[0;34m{n1}\033[m).')
elif n1 == n2:
    print('\033[4mNão\033[m existe um número maior, \033[0;36mAMBOS\033[m são iguais!')
