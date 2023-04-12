casa = float(str(input('Digite o valor da casa: R$')).strip().replace('.', '').replace(',', '.'))
salario = float(str(input('Digite o valor do seu salário mensal: R$')).strip().replace('.', '').replace(',', '.'))
anos = float(input('Digite a quantidade de anos que você quer estar pagando pela casa: '))

meses = anos * 12
pm = casa / meses
porcentagem = salario * (30/100)

if pm > porcentagem:
    print('Você \033[1;31mNÃO\033[m pode comprar esta casa, pois a prestação mensal excedeu \033[0;31m30%\033[m'
          f' do seu salário mensal.\n\n\033[0;31mPrestação: R${pm:.2f}\033[m\n\033[0;31m30% do salário: '
          f'R${porcentagem:.2f}\033[m')
else:
    print(f'\n\033[0;32mPARABÉNS! Você pode comprar essa casa!\033[m\nA prestação mensal para o pagamento da casa será'
          f' de \033[1;32mR${pm:.2f}\033[m!')
