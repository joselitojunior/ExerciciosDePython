num = int(input('\033[1;32mDigite um número inteiro:\033[m '))
print('''\nEscolha uma das bases para conversão:
[ 1 ] converter para \033[1;35mBINÁRIO\033[m
[ 2 ] converter para \033[1;35mOCTAL\033[m
[ 3 ] converter para \033[1;35mHEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'\n{num} convertido para \033[1;35mBINÁRIO\033[m é igual a \033[4m{bin(num)[2:]}\033[m')
elif opção == 2:
    print(f'\n{num} convertido para \033[1;35mOCTAL\033[m é igual a \033[4m{oct(num)[2:]}\033[m')
elif opção == 3:
    print(f'\n{num} convertido para \033[1;35mHEXADECIMAL\033[m é igual a \033[4m{hex(num)[2:]}\033[m')
else:
    print('\n\033[0;31mOpção inválida. Tente novamente.\033[m')
