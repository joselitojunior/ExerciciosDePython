r = 'nao'
while r == 'nao':
    genero = str(input('\033[1;97mQual o seu gênero?'
                       '\n\033[1;31mH\033[1;97m para Homem'
                       '\n\033[1;35mM\033[1;97m para Mulher'
                       '\n\033[1;33mNB\033[1;97m para Não-Binário'
                       '\n\033[1;32mGF\033[1;97m para Gênero-Fluído'
                       '\n\033[1;36mA\033[1;97m para Agênero'
                       '\n\n> \033[m')).lower().replace(' ', '')
    while genero != 'h' and genero != 'm' and genero != 'nb' and genero != 'gf' and genero != 'a':
        print('\n\033[1;97;41mPor favor, informe um gênero válido!\033[m')
        genero = str(input('\033[1;97m\n\033[1;31mH\033[1;97m para Homem'
                           '\n\033[1;35mM\033[1;97m para Mulher'
                           '\n\033[1;33mNB\033[1;97m para Não-Binário'
                           '\n\033[1;32mGF\033[1;97m para Gênero-Fluído'
                           '\n\033[1;36mA\033[1;97m para Agênero'
                           '\n\n> \033[m')).lower().replace(' ', '')
    if genero == 'h':
        ngenero = 'Homem'
    if genero == 'm':
        ngenero = 'Mulher'
    if genero == 'nb':
        ngenero = 'Não-Binário'
    if genero == 'gf':
        ngenero = 'Gênero-Fluído'
    if genero == 'a':
        ngenero = 'Agênero'
    print(f'\n\033[1;97mSeu gênero é: \033[1;32m{ngenero}\033[m')
    r = 'erro'
    while r != 'sim' and r != 'nao':
        r = str(input('\n\033[1;97;43mDeseja confirmar?\033[m'
                      '\n\033[1;4;32mSIM\033[m\033[1;97m para confirmar.'
                      '\n\033[1;4;31mNÃO\033[m\033[1;97m para voltar e redefinir os dados.'
                      '\n\n> \033[m')).lower().replace(' ', '').replace('ã', 'a')
        if r != 'sim' and r != 'nao':
            print('\n\033[1;97;41mPor favor, informe uma resposta válida!\033[m')
print('\n\033[1;97mDado cadastrado, obrigado!\033[m')
