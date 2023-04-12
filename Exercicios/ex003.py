n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
s = n1 + n2
print('A soma de {}{}{} e {}{}{} vale {}{}{}'.format('\033[0;33m', n1, '\033[m',
                                                     '\033[0;33m', n2, '\033[m',
                                                     '\033[0;32m', s, '\033[m'))
