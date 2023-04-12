print('-' * 50)

qnt50 = 0
qnt20 = 0
qnt10 = 0
qnt1 = 0

saque = input('\033[1;97;42mSaque:\033[m\033[1;97m R$').replace('.', '').replace(',00', '')
saquesv = saque.replace(',', '')
nsaque = saquesv.isnumeric()

while True:
    while ',' in saque and nsaque == True:
        print('\n\033[1;31mVocê não pode sacar moedas.\033[m')
        saque = input('\033[1;97;42mSaque:\033[m\033[1;97m R$').replace('.', '').replace(',00', '')
        saquesv = saque.replace(',', '')
        nsaque = saquesv.isnumeric()
    while ',' in saque and nsaque == False:
        print('\n\033[1;31mPor favor, insira um valor válido.\033[m')
        saque = input('\033[1;97;42mSaque:\033[m\033[1;97m R$').replace('.', '').replace(',00', '')
        saquesv = saque.replace(',', '')
        nsaque = saquesv.isnumeric()
    while nsaque == False:
        print('\n\033[1;31mPor favor, insira um valor válido.\033[m')
        saque = input('\033[1;97;42mSaque:\033[m\033[1;97m R$').replace('.', '').replace(',00', '')
        saquesv = saque.replace(',', '')
        nsaque = saquesv.isnumeric()
    if ',' not in saque and nsaque == True:
        break

intsaque = int(saque)
while intsaque >= 50:
    intsaque = intsaque - 50
    qnt50 += 1
while intsaque >= 20:
    intsaque = intsaque - 20
    qnt20 += 1
while intsaque >= 10:
    intsaque = intsaque - 10
    qnt10 += 1
while intsaque >= 1:
    intsaque = intsaque - 1
    qnt1 += 1

print('')
if qnt50 == 1:
    print(f'\033[1;34m{qnt50} \033[1;97mcédula de \033[1;32mR$50,00')
elif qnt50 > 1:
    print(f'\033[1;34m{qnt50} \033[1;97mcédulas de \033[1;32mR$50,00')
if qnt20 == 1:
    print(f'\033[1;34m{qnt20} \033[1;97mcédula de \033[1;32mR$20,00')
elif qnt20 > 1:
    print(f'\033[1;34m{qnt20} \033[1;97mcédulas de \033[1;32mR$20,00')
if qnt10 == 1:
    print(f'\033[1;34m{qnt10} \033[1;97mcédula de \033[1;32mR$10,00')
elif qnt10 > 1:
    print(f'\033[1;34m{qnt10} \033[1;97mcédulas de \033[1;32mR$10,00')
if qnt1 == 1:
    print(f'\033[1;34m{qnt1} \033[1;97mcédula de \033[1;32mR$1,00')
elif qnt1 > 1:
    print(f'\033[1;34m{qnt1} \033[1;97mcédulas de \033[1;32mR$1,00')
print('\033[m-' * 50)
