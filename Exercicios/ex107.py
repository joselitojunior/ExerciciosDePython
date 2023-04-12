from ex107 import moeda

print('\033[1;97m'+'=' * 50)
n = int(input('Digite o preço: \033[1;32mR$\033[1;97m'))
print('\033[1;97m'+'-' * 50)
print(f'A metade de {n} é {moeda.metade(n)}\n'
      f'O dobro de {n} é {moeda.dobro(n)}\n'
      f'Aumentando 10%, temos {moeda.aumentar(n, 10)}\n'
      f'Reduzindo 13%, temos {moeda.diminuir(n, 13)}')
print('\033[1;97m'+'=' * 50)
