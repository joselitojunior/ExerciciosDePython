s = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n // 2 == n / 2:
        s = s + n

print(f'\n\033[1;32mA soma apenas entre os números pares é de: \033[4m{s}\033[m')
