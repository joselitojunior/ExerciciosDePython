def tirapontos(p):
    p1 = p
    while '.' in p:
        pos = p.find('.')
        if pos + 3 > len(p) - 1:
            print(f'\n\033[1;31m"{p1}" não é um preço válido!')
            p = str(input('\033[1;97m> '))
            p1 = p
        elif p[pos + 1].isnumeric() and p[pos + 2].isnumeric() and p[pos + 3].isnumeric():
            p = p.replace('.', '', 1)
        else:
            print(f'\n\033[1;31m"{p1}" não é um preço válido!')
            p = str(input('\033[1;97m> '))
            p1 = p
    return p


def leiadinheiro(txt):
    p = str(input(txt))
    while True:
        p = tirapontos(p)
        if p[0] == '-':
            print(f'\n\033[1;31mPor favor! Digite um valor positivo.')
            p = str(input('\033[1;97m> '))
        elif p.replace(',', '').isnumeric():
            p = float(p.replace(',', '.'))
            break
        else:
            print(f'\n\033[1;31m"{p}" não é um preço válido!')
            p = str(input('\033[1;97m> '))
    return p
