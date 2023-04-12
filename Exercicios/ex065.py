r = 'sim'
s = 0
maior = 0
menor = 0
qnt = 0
qntn = 0

while r == 'sim':
    n = int(float(input('\033[1;97mDigite um número:\033[m'
                        '\n\033[1;97m>\033[m ')))
    qntn += 1
    r = str(input('\n\033[1;97mDeseja continuar?\033[m'
                  '\n\033[1;32m[SIM] \033[1;97mpara continuar.\033[m'
                  '\n\033[1;31m[NAO] \033[1;97mpara parar.'
                  '\n\n> \033[m')).lower().strip().replace('ã', 'a')
    while r != 'sim' and r != 'nao':
        r = str(input('\n\033[1;31mEscolha uma opção válida!\033[m'
                      '\n\033[1;97m>\033[m ')).lower().strip().replace('ã', 'a')
    if r == 'nao':
        print('\n\033[1;32mFinalizado!\033[m')
    s += n
    if qnt == 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if qnt == 0:
        qnt = 1
        maior = n
        menor = n
    print('')
print(f'\033[1;97mA média dos números é: \033[1;4;35m{s / qntn}\033[m')
print(f'\033[1;97mO maior número é: \033[1;4;35m{maior}\033[m'
      f'\n\033[1;97mO menor número é: \033[1;4;35m{menor}\033[m')
