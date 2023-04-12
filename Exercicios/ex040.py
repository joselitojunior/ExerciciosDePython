nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
me = (nota1 + nota2) / 2
me = float(f'{me:.1f}')

print(f'\nSua \033[4mmédia\033[m foi de: {me}')

if me < 5:
    print('\033[1;31mREPROVADO\033[m')
elif me >= 5 and me <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
elif me > 6.9:
    print('\033[1;32mAPROVADO\033[m')
