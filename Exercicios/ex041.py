from datetime import date

n = int(input('Digite o \033[1;34mANO\033[m em que você nasceu: '))
ano = date.today().year
idade = ano - n

if idade > 0 and idade <= 9:
    print('\033[1;33mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('\033[1;35mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('\033[1;32mJÚNIOR\033[m')
elif idade > 19 and idade <= 25:
    print('\033[1;35mSÊNIOR\033[m')
elif idade > 25:
    print('\033[1;36mMASTER\033[m')
