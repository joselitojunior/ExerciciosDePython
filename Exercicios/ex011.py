a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

area = a * l
tinta = area / 2

print(f'\nÁrea da parede: {area}m²\n\033[1;31;44mQuantidade de tinta necessária: {tinta}L\033[m')
