from mdl.tudo import *

linha__()
while True:
    try:
        t = float(input(f'{branco}Informe a temperatura em ºC: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}Essa temperatura em fahrenheit é: {amarelo}{to_int(t * 1.8 + 32)}ºF')
linha__()
