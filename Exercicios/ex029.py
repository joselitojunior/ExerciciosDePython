vel = float(str(input('Qual a velocidade do carro em km/h? ')).strip().replace('km/h', ''))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'Seu carro foi \033[1;31mmultado\033[m por ultrapassar 80km\nValor da multa: \033[4mR${multa:.2f}\033[m')
else:
    print('\033[0;32mO carro não ultrapassou o limite!\033[m \033[1;31mS2\033[m')
