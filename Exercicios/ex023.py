numero = int(input('Digite um número de 0 á 9999: '))
u = str(numero // 1 % 10)
d = str(numero // 10 % 10)
c = str(numero // 100 % 10)
m = str(numero // 1000 % 10)
print('Unidade:', '\033[0;32m'+u+'\033[m')
print('Dedeza:', '\033[0;32m'+d+'\033[m')
print('Centena:', '\033[0;32m'+c+'\033[m')
print('Milhar:', '\033[0;32m'+m+'\033[m')
