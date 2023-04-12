vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def ajuda(var):
    help(var)

def linha_():
    print(branco+'-' * 50)


def linha__():
    print(branco+'=' * 50)


linha__()
print(f'{azul}\033[107m{"CENTRAL DE AJUDA PYTHON":^50}\033[m')
while True:
    linha__()
    print()
    comando = input(f'\033[1;97;42m{"Digite o comando:":^50}\033[m\033[1;97m\n> ').strip().lower()
    print()
    if comando == 'fim':
        break
    linha__()
    print(f'\033[1;97;43m')
    ajuda(comando)
    print(f'\033[m', end='')
linha__()
