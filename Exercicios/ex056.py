somaidade = 0

hmaioridade = 0
nhmaioridade = []
unicohmaioridade = []
qnthmaioridade = 0
ph = 0

qntmmenos20 = 0
qntm = 0

for p in range(1, 5):
    nome = str(input(f'\033[1;97mDigite o \033[1;4;97mnome\033[m\033[1;97m da {p}ª pessoa:\033[m ')).strip()
    idade = int(str(input(f'\033[1;97mDigite a \033[1;4;97midade\033[m\033[1;97m da {p}ª pessoa:\033[m ')).replace(' ', ''))
    sexo = str(input(f'\033[1;97mInforme o \033[1;4;97mgênero\033[m\033[1;97m da {p}ª pessoa:\033[m \n'
                     '\033[1;35mH\033[97m para Homem\033[m\n'
                     '\033[1;36mM\033[97m para Mulher\033[m\n'
                     '\033[1;33mNB\033[97m para Não-Binário\n\n>\033[m ')).lower().replace(' ', '')
    print('')
    somaidade += idade

    if sexo == 'h':
        if ph == 0:
            ph = 1
            if idade > hmaioridade:
                hmaioridade = idade
                nhmaioridade += [nome]
                qnthmaioridade += 1
        elif ph == 1:
            if idade > hmaioridade:
                nhmaioridade = []
                qnthmaioridade = 1
                hmaioridade = idade
                nhmaioridade += [nome]
            elif idade == hmaioridade and idade > 0:
                hmaioridade = idade
                nhmaioridade += [nome]
                qnthmaioridade += 1

    if sexo == 'm':
        qntm += 1
        if idade < 20:
            qntmmenos20 += 1

midade = somaidade / 4

print(f'\033[1;97m• A média da idade das pessoas é de \033[1;4;97m{midade}\033[m\033[1;97m anos.\033[m')

if qnthmaioridade > 1:
    print(f'• \033[1;97mOs {qnthmaioridade} homens mais velhos têm {hmaioridade} anos, são eles: \033[1;4;97m{nhmaioridade}\033[m')
if qnthmaioridade == 1:
    print(f'• \033[1;97mO homem mais velho tem {hmaioridade} anos, ele se chama: \033[1;4;97m{nhmaioridade}\033[m')
if qnthmaioridade == 0:
    print('• \033[1;31mNão há nenhum homem inserido na lista.\033[m')

if qntmmenos20 == 0 and qntm >= 1:
    print('• \033[1;97mNão há \033[1;4;97mnenhuma\033[m\033[1;97m mulher com menos de 20 anos.\033[m')
if qntmmenos20 == 0 and qntm == 0:
    print('• \033[1;31mNão há nenhuma mulher inserida na lista.\033[m')
if qntmmenos20 == 1:
    print('• \033[1;97mHá \033[1;4;97m1\033[m\033[1;97m mulher com menos de 20 anos.\033[m')
if qntmmenos20 > 1:
    print(f'• \033[1;97mHá \033[1;4;97m{qntmmenos20}\033[m\033[1;97m mulheres com menos de 20 anos.\033[m')
