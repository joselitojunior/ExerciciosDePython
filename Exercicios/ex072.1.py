tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
print('-' * 50)
n = input('\033[1;97mDigite um número de 0 à 20:\033[m ').replace(' ', '')

nnum = n.isnumeric()

while True:
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
        break
print(f'\n\033[1;34m{tupla[intn].title()}\033[m')
print('-' * 50)
