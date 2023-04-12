galera = list()
qnt = 0
run = 'ok'

print('\033[1;97m=' * 70)
print('\033[1;97m          DIGITE "\033[32mok\033[97m" PARA FINALIZAR O CADASTRAMENTO')
print('\033[1;97m=' * 70+'\n')
while run == 'ok':
    qnt += 1
    while True:
        nome = str(input(f'\033[1;97mNome do \033[34m{qnt}º\033[97m aluno: ')).strip().title()
        if nome == 'ok' or nome == 'Ok' or nome == 'OK' or nome == 'oK':
            qnt -= 1
            run = 'off'
            break
        elif nome.replace(' ', '').isalpha():
            galera.append(list())
            galera[qnt - 1].append(nome)
            break
    if run == 'ok':
        galera[qnt - 1].append(list())
        for c in range(2):
            if run == 'ok':
                while True:
                    nota = str(input(f'\033[34m{c + 1}ª\033[97m nota: '))
                    if nota == 'ok' or nota == 'Ok' or nota == 'OK' or nota == 'oK':
                        galera.pop()
                        qnt -= 1
                        run = 'off'
                        break
                    else:
                        nota2 = nota
                        dec = 0
                        if ',' in nota:
                            nota2 = nota.replace(',', '', 1)
                            dec = 1
                        if nota2.isnumeric():
                            if dec == 1:
                                dec = 0
                                nota = float(nota.replace(',', '.'))
                            else:
                                nota = int(nota)
                            galera[qnt - 1][1].append(nota)
                            break
        print('\033[1;97m-' * 70)
print('\n'+'\033[1;97m=' * 70)
print(f'\033[1;97m{"BOLETINS":^62}\n')
print('\033[1;34mNúmero:             \033[32mNome:                                       \033[35mMédia:')
for i, pessoa in enumerate(galera):
    media = (pessoa[1][0] + pessoa[1][1]) / 2
    print(f'\033[34m{i + 1:<20}\033[32m{pessoa[0]:<44}\033[35m{media}')
print('\033[1;97m=' * 70)
print('\033[1;97m DIGITE "\033[31msair\033[97m" PARA SAIR OU DIGITE O \033[34mNÚMERO DO ALUNO\033[97m PARA VER A NOTA')
print('\033[1;97m=' * 70)
while True:
    inp = str(input('\033[1;97m> ')).lower().strip()
    if inp == 'sair':
        print('\033[1;97m=' * 70)
        break
    elif inp.isnumeric():
        inp = int(inp)

        if inp <= len(galera) and inp > 0:
            print(f'\033[1;97mNotas de {galera[inp -1][0]}:\033[34m {galera[inp - 1][1][0]} \033[97me\033[34m {galera[inp - 1][1][1]}')
            print('\033[1;97m-' * 70)
