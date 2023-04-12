from mdl.tudo import *

linha__()
nome = str(input(f'{branco}Digite o seu nome: ')).strip()
linha_()
print(f'{branco}Nome com letras maiúsculas: {verde}{nome.upper()}\n'
      f'{branco}Nome com letras minúsculas: {verde}{nome.lower()}\n'
      f'{branco}Quantidade de letras: {verde}{len(nome.replace(" ", ""))}\n'
      f'{branco}Quantidade de letras no primeiro nome: {verde}{len(nome.split()[0])}')
linha__()
