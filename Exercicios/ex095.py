galera = list()
pessoa = dict()
run = 'on'
qnt = 0
s_list = list()

print('\033[1;97m'+'=' * 60)
print('      DIGITE "\033[32mok\033[97m" PARA PARAR O CADASTRAMENTO')
print('\033[1;97m'+'=' * 60)

while run == 'on':
    s = 0
    qnt += 1
    if qnt != 1:
        print('\033[1;97m' + '-' * 60)
    while True:
        nome = str(input(f'\033[33mNome\033[97m do \033[34m{qnt}º\033[97m jogador: ')).lower().strip().title()
        if nome == 'Ok':
            run = 'off'
            qnt -= 1
            break
        elif nome.isalpha():
            pessoa['Nome'] = nome
            break
    if run == 'on':
        while True:
            jogos = str(input(f'\033[36mQuantidade\033[97m de jogos de {nome}: ')).strip().lower()
            if jogos == 'ok':
                run = 'off'
                qnt -= 1
                break
            elif jogos.isnumeric():
                jogos = int(jogos)
                pessoa['Jogos'] = jogos
                break
    if run == 'on':
        pessoa['Gols'] = list()
        for c in range(jogos):
            if run == 'on':
                while True:
                    gols = str(input(f'\033[34mGols\033[97m no {c + 1}º jogo: ')).strip().lower()
                    if gols == 'ok':
                        run = 'off'
                        qnt -= 1
                        break
                    elif gols.isnumeric():
                        gols = int(gols)
                        s += gols
                        pessoa['Gols'].append(gols)
                        break
    if run == 'on':
        galera.append(pessoa.copy())
        s_list.append(s)
    pessoa.clear()
print('\033[1;97m' + '=' * 60, '\n')
print(f'\033[36m{"Nº":<3}\033[33m{"Nome":<27}\033[34m{"Gols":<25}\033[32m{"Total":<2}')
print('\033[1;97m' + '-' * 60)
for i, v in enumerate(galera):
    print(f'\033[97m{i + 1:<3}{galera[i]["Nome"]:<27}{str(galera[i]["Gols"]):<25}\033[32m{s_list[i]:<2}')
print('\033[1;97m' + '-' * 60, '\n')
print('\033[1;97m' + '=' * 74)
print('\033[97mDIGITE "\033[31msair\033[97m" PARA SAIR OU DIGITE O \033[36mNÚMERO DO JOGADOR\033[97m PARA VER OS '
      'DETALHES')
print('\033[1;97m' + '=' * 74)
while True:
    inp = str(input('\033[1;97m> ')).lower().strip()
    if inp == 'sair':
        print('\033[1;97m=' * 74)
        break
    elif inp.isnumeric():
        inp = int(inp)
        if 0 < inp <= qnt:
            print(f'{galera[inp - 1]["Nome"]:^74}')
            for i, v in enumerate(galera[inp - 1]["Gols"]):
                if v != 1:
                    print(f'{f"Jogo {i + 1}: {v} gols":^74}')
                else:
                    print(f'{f"Jogo {i + 1}: 1 gol":^74}')
            print('\033[1;97m' + '-' * 74)
        else:
            print(f'\033[1;31m{f"O jogador número {inp} não foi encontrado.":^74}')
            print('\033[1;97m' + '-' * 74)
