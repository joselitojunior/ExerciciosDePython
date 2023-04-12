dados = dict()
s = 0

print('\033[1;97m'+'=' * 50)
dados['Nome'] = str(input('\033[1;33mNome\033[97m do jogador: ')).lower().strip().title()
jogos = int(input(f'\033[36mQuantidade\033[97m de jogos de {dados["Nome"].title()}: '))
dados['Gols'] = list()
for c in range(jogos):
    dados['Gols'].append(int(input(f'\033[34mGols\033[97m no {c + 1}º jogo: ')))
    s += dados['Gols'][c]
dados['Total'] = s
print('\033[1;97m'+'=' * 50)
print(dados)
print('\033[1;97m'+'=' * 50)
for k, v in dados.items():
    print(f'\033[1;97m{k}: {v}')
print('\033[1;97m'+'=' * 50)
print(f'\033[1;33m{dados["Nome"]}\033[97m jogou \033[36m{jogos}\033[97m partidas.')
for i, v in enumerate(dados['Gols']):
    if v > 1:
        print(f'{i + 1}ª partida: {v} gols')
    else:
        print(f'{i + 1}ª partida: {v} gol')
if dados['Total'] > 1:
    print(f'\033[1;97mTotal: {dados["Total"]} gols')
else:
    print(f'\033[1;97mTotal: {dados["Total"]} gol')
print('\033[1;97m'+'=' * 50)
