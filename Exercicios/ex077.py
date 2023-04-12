print('\033[1;97m-' * 30)

listagem = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

t = len(listagem)

for palavras in listagem:
    print(f'\033[1;35m{palavras.upper()}\033[1;97m:', end=' ')
    for letras in palavras:
        if letras in vogais:
            print(letras, end=' ')
    print('\n', end='')
print('\033[1;97m-' * 30)