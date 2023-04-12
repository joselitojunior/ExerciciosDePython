s = float(input('Digite seu salário: R$'))

por = s * (15/100)
sn = s + por

print('O seu salário com \033[1;36m15%\033[m de aumento é \033[1;32mR${:.2f}\033[m!'.format(sn))
