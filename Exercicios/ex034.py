s = float(str(input('Digite o valor do seu salário em reais: R$')).strip())

if s > 1250:
    au = s * (10/100)
    print(f'O aumento do salário de R${s} em \033[0;32m10%\033[m é de \033[1;4;32mR${au:.2f}\033[m')
else:
    au = s * (15/100)
    print(f'O aumento do salário de R${s} em \033[0;32m15%\033[m é de \033[1;4;32mR${au:.2f}\033[m')
