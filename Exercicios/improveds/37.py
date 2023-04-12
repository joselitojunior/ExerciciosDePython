from mdl.tudo import *

resp = 0
n = 0
linha__()
while True:
    try:
        n = int(input(f'{branco}Digite um número inteiro: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}Base de conversão:\n'
          f'{azul}[ 1 ]{branco} converter para binário.\n'
          f'{roxo}[ 2 ]{branco} converter para octal.\n'
          f'{amarelo}[ 3 ]{branco} converter para hexadecimal.')
while True:
    try:
        resp = int(input(f'{branco}> '))
    except:
        continue
    else:
        if resp == 1 or resp == 2 or resp == 3:
            print(f'\n{branco}Sua opção: {resp}')
            break
linha_()
if resp == 1:
    print(f'{branco}{sublinhado}{n}{nada}{branco} em {azul}binário{branco} é: {bin(n)[2:]}')
elif resp == 2:
    print(f'{branco}{sublinhado}{n}{nada}{branco} em {roxo}octal{branco} é: {oct(n)[2:]}')
else:
    print(f'{branco}{sublinhado}{n}{nada}{branco} em {amarelo}hexadecimal{branco} é: {hex(n)[2:]}')
linha__()
