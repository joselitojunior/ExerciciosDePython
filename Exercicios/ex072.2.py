tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
print('-' * 50)

while True:
    n = input('\033[1;97mDigite um número de 0 à 20:\033[m ').replace(' ', '')
    nnum = n.isnumeric()
    while not nnum:
        print('\n\033[1;31mPor favor, informe um número válido.\033[m')
        n = input('\033[1;97mDigite um número de 0 à 20:\033[m ').replace(' ', '')
        nnum = n.isnumeric()
    intn = int(n)
    while intn < 0 or intn > 20:
        print('\n\033[1;31mPor favor, informe um número válido.\033[m')
        n = input('\033[1;97mDigite um número de 0 à 20:\033[m ').replace(' ', '')
        nnum = n.isnumeric()
        if nnum:
            intn = int(n)
    if intn >= 0 and intn <= 20:
        print(f'\n\033[1;34m{tupla[intn].title()}\033[m')
        print('-' * 50)
        continuar = str(input('\033[1;97;43mDeseja continuar?\033[m'
              '\n\033[1;32m[SIM] \033[1;97mpara continuar.'
              '\n\033[1;31m[NÃO] \033[1;97mpara finalizar.\033[1;97m'
              '\n\n> \033[m')).lower().replace(' ', '').replace('ã', 'a')
        while continuar != 'nao' and continuar != 'sim':
            print('\n\033[1;97;41mPor favor, informe uma opção válida.\033[m')
            continuar  = str(input('\033[1;97m>\033[m ')).lower().replace(' ', '').replace('ã', 'a')
        if continuar == 'nao':
            break
        elif continuar == 'sim':
            print('-' * 50)
print('-' * 50)
print('\033[1;32mFinalizado!\033[m')
