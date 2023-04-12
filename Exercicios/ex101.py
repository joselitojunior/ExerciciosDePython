from datetime import date
data = date.today().year


def voto(ano):
    idade = data - ano
    if 16 <= idade < 18 or idade >= 65:
        retorno = 'VOTO OPCIONAL'
        return retorno
    elif idade < 16:
        retorno = 'NÃO VOTA'
        return retorno
    else:
        retorno = 'VOTO OBRIGATÓRIO'
        return retorno


print('\033[1;97m'+'=' * 50)
resp = voto(int(input('\033[1;97mDigite o ano do seu nascimento: ')))
print(f'\033[1;34mSituação:\033[1;97m {resp}')
print('\033[1;97m'+'=' * 50)
