from mdl.tudo import *

lista = list()
linha__()
for c in range(2):
    while True:
        try:
            lista.append(float(input(f'{branco}Digite a {c + 1}ª nota: ')))
        except:
            continue
        else:
            break
linha_()
media = (lista[0] + lista[1]) / 2
print(f'{branco}Média: {azul}{to_int(media, 2)}')
if media < 5:
    print(f'{branco}Situação do aluno: {vermelho}REPROVADO')
elif 5 <= media <= 6.9:
    print(f'{branco}Situação do aluno: {amarelo}RECUPERAÇÃO')
elif media >= 7:
    print(f'{branco}Situação do aluno: {verde}APROVADO')
linha__()
