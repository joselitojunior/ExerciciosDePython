vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
branco = '\033[1;97m'
nada = '\033[m'
sublinhado = '\033[4m'


def linha_(qnt=50):
    print(f'\033[1;97m'+'-' * qnt)


def linha__(qnt=50):
    print(f'\033[1;97m'+'=' * qnt)


def to_int(n, vrg=-1):
    from math import trunc
    if str(n).replace('.', '', 1).isnumeric():
        n = float(n)
        if trunc(n) == n:
            n = int(n)
            return n
        else:
            if vrg >= 0:
                n = str(f'{n:.{vrg}f}')
                if trunc(float(n)) == float(n):
                    n = int(float(n))
            return n


def trueorfalse(n):
    if n == True:
        n = f'\033[1;32m{True}\033[m'
        return n
    elif n == False:
        n = f'\033[1;31m{False}\033[m'
        return n


def monetario(n):
    n = f"{float(n):.2f}".replace('.', ',', 1)
    n1 = n[::-1]
    dec = n[-3:]
    n1 = n1[3:]
    if len(n1) <= 3:
        n = 'R$' + n
        return n
    else:
        n1 = n1[:3] + '.' + n1[3:]
        while True:
            if len(n1[n1.rfind('.') + 1:]) > 3:
                n1 = n1[:n1.rfind('.') + 4] + '.' + n1[n1.rfind('.') + 4:]
            else:
                n1 = 'R$' + n1[::-1] + dec
                return n1


def decimais(n, vrg=0):
    if str(n).replace('.', '', 1).isnumeric():
        n = f'{n:.{vrg}f}'
        return n
