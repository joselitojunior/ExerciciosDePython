from mdl.tudo import *

linha__()
algo = input(f'{branco}Digite algo: ')
linha_()
print(f'{branco}Tipo: {azul}{type(algo)}\n'
      f'{branco}Numérico: {trueorfalse(algo.isnumeric())}\n'
      f'{branco}Alfabético: {trueorfalse(algo.isalpha())}\n'
      f'{branco}Alfanumérico: {trueorfalse(algo.isalnum())}\n'
      f'{branco}Minúsculo: {trueorfalse(algo.islower())}\n'
      f'{branco}Maiúsculo: {trueorfalse(algo.isupper())}\n'
      f'{branco}Todo com espaço:{trueorfalse(algo.isspace())}\n'
      f'{branco}Capitalizado: {trueorfalse(algo.istitle())}')
linha__()
