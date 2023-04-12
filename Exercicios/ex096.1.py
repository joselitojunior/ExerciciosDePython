def area(largura, comprimento):
    a = largura * comprimento
    print(f'\033[35mÁrea: {a}m²')


def linha_():
    print('\033[1;97m'+'-' * 50)


def linha__():
    print('\033[1;97m' + '=' * 50)


linha__()
while True:
    largura = str(input('\033[34mLargura (em METROS): ')).lower().replace('m', '', 1).strip()\
        .replace('.', '').replace(',', '.', 1)
    if largura.replace('.', '', 1).isnumeric():
        if '.' in largura:
            largura = float(largura)
        else:
            largura = int(largura)
        break
while True:
    comprimento = str(input('\033[36mComprimento (em METROS): ')).lower().replace('m', '', 1).strip()\
        .replace('.', '').replace(',', '.', 1)
    if comprimento.replace('.', '', 1).isnumeric():
        if '.' in comprimento:
            comprimento = float(comprimento)
        else:
            comprimento = int(comprimento)
        break
linha__()
area(largura=largura, comprimento=comprimento)
linha__()
