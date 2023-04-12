n = 0
s = 0
qnt = 0

print('\033[1;97mDigite um número:\033[m')
while n != 999:
    n = int(float(input('\033[1;97m>\033[m ')))
    if n != 999:
        s = s + n
        qnt += 1
print(f'\n\033[1;97mVocê digitou \033[1;4;35m{qnt}\033[m\033[1;97m números'
      f'\nA soma entre eles é: \033[1;4;35m{s}\033[m')
