import urllib.error
import urllib.request

from cores import *

try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'{vermelho}O site "http://www.pudim.com.br" não está acessível no momento!')
else:
    print(f'{verde}O site "http://www.pudim.com.br" está acessível!')
