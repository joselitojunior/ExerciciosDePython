def linha_():
    print('\033[1;97m' + '-' * 50)


def linha__():
    print('\033[1;97m' + '=' * 50)


def area():
    a = 1
    linha__()
    for c in range(2):
        if c == 0:
            v = 'Largura'
        elif c == 1:
            v = 'Comprimento'
        while True:
            variavel = str(input(f'\033[34m{v} (em METROS): ')).lower().replace('m', '', 1).strip() \
                .replace('.', '').replace(',', '.', 1)
            if variavel.replace('.', '', 1).isnumeric():
                if '.' in variavel:
                    variavel = float(variavel)
                    a = a * variavel
                else:
                    variavel = int(variavel)
                    a = a * variavel
                break
    linha__()
    print(f'\033[35mÁrea: {a}m²')


area()
linha__()
