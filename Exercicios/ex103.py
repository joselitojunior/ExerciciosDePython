vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def ficha(nome='<desconhecido>', gols=0):
    print(f'\nO jogador {nome.capitalize()} fez {gols} gol(s).')


print(branco+'=' * 50)
n = str(input(f'{branco}Nome do jogador: '))
g = str(input(f'{branco}Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
print(branco + '=' * 50)
