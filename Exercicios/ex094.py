pessoa = dict()
galera = list()
generos = ('h', 'homem', 'm', 'mulher', 'nb', 'não-binário', 'gf', 'gênero-fluído', 'a', 'agênero')
run = 'on'
qnt = 0
s = 0
m = list()
acima_media = list()

print('\033[1;97m' + '=' * 50)
print('   \033[1;97mDIGITE "\033[32mok\033[97m" PARA PARAR O CADASTRO DE PESSOAS')
print('\033[1;97m' + '=' * 50)
while run == 'on':
    qnt += 1
    while True:
        nome = str(input(f'\033[1;97mNome da \033[34m{qnt}ª\033[97m pessoa: ')).lower().strip().title()
        if nome == 'Ok':
            run = 'off'
            qnt -= 1
            print('\033[1;97m' + '=' * 50)
            break
        elif nome.isalpha():
            pessoa['nome'] = nome
            break
    if run == 'on':
        while True:
            genero = str(input('\n\033[31m[H]\033[97m para\033[31m HOMEM'
                             '\n\033[32m[M]\033[97m para\033[32m MULHER'
                             '\n\033[33m[NB]\033[97m para\033[33m NÃO-BINÁRIO'
                             '\n\033[34m[GF]\033[97m para\033[34m GÊNERO-FLUÍDO'
                             '\n\033[35m[A]\033[97m para\033[35m AGÊNERO'
                             f'\n\033[97m> ')).lower().strip()
            if genero == 'ok':
                run = 'off'
                qnt -= 1
                print('\033[1;97m' + '=' * 50)
                break
            if genero == 'h' or genero == 'm' or genero == 'nb' or genero == 'gf' or genero == 'a':
                pessoa['genero'] = generos[generos.index(genero) + 1]
                break
    if run == 'on':
        while True:
            idade = str(input(f'\n\033[1;97mIdade da \033[34m{qnt}ª\033[97m pessoa: ')).replace(' ', '')
            if idade == 'ok':
                run = 'off'
                qnt -= 1
                print('\033[1;97m' + '=' * 50)
                break
            if int(idade) > 0 and idade.isnumeric():
                idade = int(idade)
                s += idade
                pessoa['idade'] = idade
                galera.append(pessoa.copy())
                pessoa.clear()
                print('\033[1;97m' + '-' * 50)
                break
media = s / qnt
print(f'\033[1;97mPessoas cadastradas:\033[34m {qnt}')
print(f'\033[1;97mMédia de idade das pessoas: \033[34m{media:.2f}')
print(f'\033[1;97mMulheres cadastradas:\033[34m ', end='')
for i, v in enumerate(galera):
    if galera[i]['genero'] == 'mulher':
        m.append(galera[i]["nome"])
print(m)
print('\033[1;97mPessoas acima da média:\033[34m ', end='')
for i, v in enumerate(galera):
    if galera[i]['idade'] > media:
        acima_media.append(galera[i]['nome'])
print(acima_media)
print('\033[1;97m' + '=' * 50)
