from ex115.lib.interface import *
from cores import *


def arqexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arq):
    try:
        a = open(arq, 'wt+', encoding='utf-8')
        a.close()
    except:
        print(f'{vermelho}ERRO!')


def lerarq(arq):
    try:
        a = open(arq, 'rt', encoding='utf-8')
    except:
        print(f'{vermelho}ERRO!')
    else:
        linha_()
        print(f'PESSOAS CADASTRADAS'.center(50))
        linha_()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>1} anos')
        a.close()


def cadastrar(arq, nome='DESCONHECIDO', idade=0):
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print(f'{vermelho}ERRO!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{vermelho}ERRO!')
        else:
            print(f'{verde}Pessoa registrada!')
            a.close()