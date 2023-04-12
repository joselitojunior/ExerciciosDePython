from mdl.tudo import *


def tiraa(frasee):
    frasee = frasee.replace('ã', 'a').replace("á", "a").replace("â", "a").replace("à", "a")
    return frasee


def tiranalpha(frasee):
    for letra in frasee:
        if not letra.isalpha():
            frasee = frasee.replace(letra, '')
    return frasee


linha__()
frase = tiraa(str(input(f'{branco}Digite uma frase: ')).strip().lower())
frase = tiranalpha(frase)
linha_()
print(f'{branco}Quantidade da letra "a" na frase: {verde}{frase.count("a")}')
if frase.find("a") >= 0:
    print(
        f'{branco}A {amarelo}primeira{branco} letra "a" aparece na posição: '
        f'{verde}{frase.replace(" ", "").find("a") + 1}')
if frase.rfind("a") >= 0:
    print(
        f'{branco}A {vermelho}última{branco} letra "a" aparece na posição: '
        f'{verde}{frase.replace(" ", "").rfind("a") + 1}')
linha__()
