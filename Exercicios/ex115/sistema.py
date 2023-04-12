from ex115.lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'
if not arqexiste(arq):
    criararq(arq)

while True:
    opc = menu()
    if opc == 1:
        lerarq(arq)
        sleep(1.5)
    elif opc == 2:
        linha_()
        print(f'CADASTRAR PESSOAS'.center(50))
        linha_()
        nome = str(input('Digite o nome da pessoa: ')).strip()
        idade = 0
        while True:
            try:
                idade = int(input('Digite a idade da pessoa: '))
            except:
                print(f'\n{vermelho}Digite uma idade válida!{branco}')
                continue
            else:
                break
        cadastrar(arq, nome, idade)
        sleep(1.5)
    elif opc == 3:
        print(f'{azul}{"Programa finalizado com sucesso!":^50}')
        linha__()
        break
