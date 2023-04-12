frase = str(input('Digite uma frase: '))
frase = frase.strip().lower()

print('A letra "a" apareceu', frase.count('a'), 'vezes.')
print('A primeira letra "a" aparece na posição: {}'.format(frase.find('a')+1))
print('A última letra "a" aparece na posição: {}'.format(frase.rfind('a')+1))
