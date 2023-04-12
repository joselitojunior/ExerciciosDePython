ano = int(input('Em que ano você esta? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano \033[1;32mbissexto\033[m!')
else:
    print('\033[4;31mNão\033[0;31m é um ano bissexto.\033[m')
