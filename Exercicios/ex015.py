km = float(input('Quantos quilómetros foram percorridos com o carro? '))
dias = float(input('Por quantos dias ele foi alugado?'))

print('\n'+'\033[1;33m-\033[m' * (15),'\nO preço total é de \033[0;32mR${:.2f}\033[m.'.format((km * 0.15) + (dias * 60)),'\n'+'\033[1;33m-\033[m' * (15))
