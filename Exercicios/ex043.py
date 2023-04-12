peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite a sua altura (em metros): '))

imc = peso / (altura * altura)
imc = round(imc, 2)

if imc < 18.5:
    print('\nVocê está \033[0;31mabaixo\033[m do peso ideal.')
elif imc >= 18.5 and imc <25:
    print('\n\033[1;32mVocê está no peso ideal!\033[m')
elif imc >= 25 and imc <30:
    print('\nVocê está com \033[0;31msobrepeso\033[m.')
elif imc >= 30 and imc <= 40:
    print('\nVocê está com \033[1;31mobesidade\033[m.')
elif imc > 40:
    print('\n\033[1;31mVocê está com obesidade mórbida.\033[m')
