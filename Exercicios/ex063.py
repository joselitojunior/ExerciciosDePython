qnt = int(input('\033[1;97mDigite a quantidade de elementos da Sequência de Fibonacci:\033[m '))
elementos = 1
primeiro = 0
antecessor1 = primeiro
antecessor2 = antecessor1
while elementos <= qnt:
    if elementos == 1:
        primeiro = antecessor1 + antecessor2
        print(f'\033[1;97m{primeiro}\033[m', end=' -> ')
        elementos += 1
        primeiro = 1
    if elementos > 1:
        antecessor2 = antecessor1
        antecessor1 = primeiro
        print(f'\033[1;97m{primeiro}\033[m', end=' -> ')
        primeiro = antecessor1 + antecessor2
        elementos += 1
