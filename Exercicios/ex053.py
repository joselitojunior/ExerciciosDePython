f = str(input('\033[1;36mDigite uma frase:\033[m ')).replace(' ', '').lower()
t = len(f)
inverso = ''

for letra in range(t - 1, -1, -1):
    inverso = inverso + f[letra]

print('\n\033[1;97mVocê digitou:\033[m', f+'\n\033[1;97mO inverso:\033[m', inverso+'\n')

if inverso == f:
    print('\033[1;32;107mÉ um palíndromo!\033[m')
else:
    print('\033[1;31;40mNão é um palíndromo.\033[m')