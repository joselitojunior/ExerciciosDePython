print('\033[1;97m-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('\033[1;97m-' * 50)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.3, 'Livro', 34.9)
t = len(listagem)
for c in range(0, t, 2):
    tp = len(listagem[c])
    print(f'\033[1;35m{listagem[c]}\033[1;97m', end='')
    tp = 53 - tp
    rs = '\033[1;32mR$\033[m'
    print(f'{rs:.>{tp}}', end='')
    preco = f'{listagem[c + 1]:.2f}'
    print(f'\033[1;32m{preco:>7}')
print('\033[1;97m-' * 50)
