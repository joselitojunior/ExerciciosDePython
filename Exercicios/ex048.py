s = 0
for c in range(1,501, 2):
    if c // 3 == c / 3:
        s = s + c
print(f'\n\033[0;97mA soma entre todos os números ímpares de 1 à 500 e multiplos de três é: \033[4m{s}')
