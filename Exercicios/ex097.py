def escreva(txt):
    tamanho = len(txt) + 4
    print('\033[1;97m'+'~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('\033[1;97m' + '~' * tamanho)


escreva('Olá, Mundo!')
escreva('Curso de Python no YouTube')
escreva('CeV')
