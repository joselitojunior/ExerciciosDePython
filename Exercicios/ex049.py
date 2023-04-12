n = int(input('Digite um número: '))

print('\n', end='')

for c in range(0, 10):
    m = n * c
    print(f'{n} x {c} = \033[4;35m{m}\033[m')
