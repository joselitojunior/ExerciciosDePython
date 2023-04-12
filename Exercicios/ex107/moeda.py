def centralize(txt, n=0):
    print(f'{txt:^{n}}')


def linha__():
    print('\033[1;97m'+'=' * 30)


def linha_():
    print('\033[1;97m'+'-' * 30)


def formatar(num, f):
    if f:
        num = str(f'{num:.2f}').replace('.', ',', 1)
    return num


def aumentar(num, aumento=0, f=False):
    num = num + (aumento / 100 * num)
    num = formatar(num, f)
    return num


def diminuir(num, reducao=0, f=False):
    num = num - (reducao / 100 * num)
    num = formatar(num, f)
    return num


def dobro(num, f=False):
    num = num * 2
    num = formatar(num, f)
    return num


def metade(num, f=False):
    num = num / 2
    num = formatar(num, f)
    return num


def moeda(num):
    num = str(f'{num:.2f}').replace('.', ',', 1)
    return num


def resumo(num=0, aumento=0, reducao=0, f=False):
    linha_()
    centralize('RESUMO DO VALOR', 30)
    linha_()
    print(f'Preço analisado:      {f"R${num}"}\n'
          f'Dobro do preço:       {f"R${dobro(num, f)}"}\n'
          f'Metade do preço:      {f"R${metade(num, f)}"}\n'
          f'{aumento}% de aumento:       {f"R${aumentar(num, aumento, f)}"}\n'
          f'{reducao}% de redução:       {f"R${diminuir(num, reducao, f)}"}')
    linha_()
