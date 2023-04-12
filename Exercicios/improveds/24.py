from mdl.tudo import *

linha__()
cidade = str(input(f'{branco}Digite o nome da cidade: ')).strip().lower().split()
linha_()
if cidade[0] == "santo":
    print(f'{branco}O primeiro nome da cidade {verde}é "Santo"{branco}!')
else:
    print(f'{branco}O primeiro nome da cidade {vermelho}não é "Santo"{branco}.')
linha__()
