print('\033[1;31m[999]\033[1;97m para finalizar.')
print('\033[1;97mDigite um número:\033[m')
s = qnt = 0
while True:
    n = int(input('\033[1;97m> \033[m'))
    if n == 999:
        break
    qnt += 1
    s += n
print(f'\n\033[1;97mVocê digitou \033[1;4;35m{qnt}\033[m\033[1;97m números'
      f'\nA soma entre eles é: \033[1;4;35m{s}\033[m')
