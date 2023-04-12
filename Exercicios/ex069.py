from math import trunc
p = 0
mais18 = 0
homens = 0
mulheresm20 = 0

while True:
    p += 1
    print('-' * 50)
    print(' ' * 13, f'\033[1;97mCadastro da \033[4m{p}\033[m\033[1;97mª pessoa\033[m')
    print(' ' * 17, '\033[1;31mH\033[1;97m para Homem'
                       '\n', ' ' * 16, '\033[1;35mM\033[1;97m para Mulher'
                       '\n', ' ' * 14, '\033[1;33mNB\033[1;97m para Não-Binário'
                       '\n', ' ' * 13, '\033[1;32mGF\033[1;97m para Gênero-Fluído'
                       '\n', ' ' * 16, '\033[1;36mA\033[1;97m para Agênero')
    genero = str(input('\033[1;97mGênero: \033[m')).lower().replace(' ', '')
    while genero != 'h' and genero != 'm' and genero != 'nb' and genero != 'gf' and genero != 'a':
        print('\n\033[1;97;41mPor favor, informe um gênero válido!\033[m')
        genero = str(input('\033[1;31mH\033[1;97m para Homem'
                           '\n\033[1;35mM\033[1;97m para Mulher'
                           '\n\033[1;33mNB\033[1;97m para Não-Binário'
                           '\n\033[1;32mGF\033[1;97m para Gênero-Fluído'
                           '\n\033[1;36mA\033[1;97m para Agênero'
                           '\n\n> \033[m')).lower().replace(' ', '')
    i = input('\033[1;97mIdade: \033[m')
    inum = i.isnumeric()
    if not inum:
        while not inum:
            print('\n\033[1;97;41mPor favor, informe a idade corretamente!\033[m')
            i = input('\033[1;97mIdade: \033[m')
            inum = i.isnumeric()
    i = trunc(int(i))
    print('-' * 50)
    if i >= 18:
        mais18 += 1
    if genero == 'h':
        homens += 1
    if genero == 'm' and i < 20:
        mulheresm20 += 1
    continuar = str(input('''\033[1;97mDeseja cadastrar mais pessoas?\033[m
\033[1;32m[SIM] \033[1;97mpara continuar
\033[1;31m[NÃO] \033[1;97mpara finalizar
> ''')).lower().replace(' ', '').replace('ã', 'a')
    while continuar != 'nao' and continuar != 'sim':
        print('\n\033[1;97;41mPor favor, informe uma resposta válida!\033[m\n')
        continuar = str(input('''\033[1;97mDeseja cadastrar mais pessoas?\033[m
\033[1;32m[SIM] \033[1;97mpara continuar
\033[1;31m[NÃO] \033[1;97mpara finalizar
> ''')).lower().replace(' ', '').replace('ã', 'a')
    if continuar == 'nao':
        print('\n\033[1;97mPrograma \033[1;31mfinalizado\033[1;97m!\033[m')
        print('-' * 50)
        break
if mais18 == 1:
    print(f'\033[1;97mHá \033[1;35m{mais18} \033[1;97mpessoa cadastrada com mais de 18 anos.\033[m')
else:
    print(f'\033[1;97mHá \033[1;35m{mais18} \033[1;97mpessoas cadastradas com mais de 18 anos.\033[m')
if homens == 1:
    print(f'\033[1;97mHá \033[1;35m{homens} \033[1;97mhomem cadastrado.\033[m')
else:
    print(f'\033[1;97mHá \033[1;35m{homens} \033[1;97mhomens cadastrados.\033[m')
if mulheresm20 == 1:
    print(f'\033[1;97mHá \033[1;35m{mulheresm20} \033[1;97mmulher cadastrada com menos de 20 anos.\033[m')
else:
    print(f'\033[1;97mHá \033[1;35m{mulheresm20} \033[1;97mmulheres cadastradas com menos de 20 anos.\033[m')
print('-' * 50)
