pessoas = list()
dados = list()
qnt = 0
qntp = 0
qntl = 0
maior = 0
menor = 0
maiorp = list()
menorp = list()
run = 'on'

print('\033[1;97m=' * 50)
print('\033[1;31mOBS:\033[97m DIGITE "\033[31msair\033[97m" PARA FINALIZAR O PROGRAMA')
print('\033[1;97m=' * 50)

while run == 'on':
    qnt += 1
    if len(pessoas) != 0:
        print('\033[1;97m-' * 50)
    while True:
        nome = str(input(f'\033[1;97mDigite o \033[32mnome\033[97m da \033[34m{qnt}ª\033[97m pessoa:\033[m ')).strip()
        nomesemespaco = nome.replace(' ', '')
        if nome == 'sair':
            print('\033[1;97m=' * 50)
            qnt -= 1
            run = 'off'
            break
        elif nomesemespaco.isalpha():
            nome = nome.title()
            break
    if run == 'on':
        while True:
            peso = str(input(f'\033[1;97mDigite o \033[35mpeso\033[97m da \033[34m{qnt}ª\033[97m pessoa (em KG): '))
            peso = peso.lower().replace('kg', '', 1).strip()
            if peso == 'sair':
                print('\033[1;97m=' * 50)
                qnt -= 1
                run = 'off'
                break
            peso2 = peso
            if ',' in peso:
                peso2 = peso.replace(',', '', 1)
                dec = 1
            if peso2.isnumeric():
                if dec == 1:
                    dec = 0
                    peso = float(peso.replace(',', '.', 1))
                else:
                    peso = int(peso)
                break
    if run == 'on':
        dados.append(nome)
        dados.append(peso)
        pessoas.append(dados[:])
        dados.clear()
if len(pessoas) != 0:
    for i, v in enumerate(pessoas):
        if i == 0:
            maior = v[1]
            menor = v[1]
            maiorp.append(v[0])
            menorp.append(v[0])
            qntp = 1
            qntl = 1
        else:
            if v[1] > maior:
                qntp = 1
                maior = v[1]
                maiorp = [v[0]]
            elif v[1] < menor:
                qntl = 1
                menor = v[1]
                menorp = [v[0]]
            elif v[1] == maior:
                maiorp.append(v[0])
                qntp += 1
            elif v[1] == menor:
                menorp.append(v[0])
                qntl += 1

if len(pessoas) != 0:
    print(f'\033[1;97mPessoas cadastradas: \033[32m{qnt}')
    if qntp == 1:
        print(f'\033[97mPessoa mais pesada: \033[34m{maiorp[0]}\033[97m.')
    else:
        print(f'\033[1;97mPessoas mais pesadas:\033[34m ', end='')
        for i, v in enumerate(maiorp):
            if i == len(maiorp) - 1:
                print(f'{v}\033[97m.')
            elif i == len(maiorp) - 2:
                print(v, end=' \033[97me\033[34m ')
            else:
                print(v, end='\033[97m,\033[34m ')
    if qntl == 1:
        print(f'\033[97mPessoa mais leve: \033[34m{menorp[0]}\033[97m.')
    else:
        print(f'\033[1;97mPessoas mais leves:\033[34m ', end='')
        for i, v in enumerate(menorp):
            if i == len(menorp) - 1:
                print(f'{v}\033[97m.')
            elif i == len(menorp) - 2:
                print(v, end=' \033[97me\033[34m ')
            else:
                print(v, end='\033[97m,\033[34m ')
else:
    print(f'\033[1;97mPessoas cadastradas: \033[31m{qnt}')
    print(f'\033[97mPessoa mais pesada: \033[31mNenhuma')
    print(f'\033[97mPessoa mais leve: \033[31mNenhuma')
print('\033[1;97m=' * 50)