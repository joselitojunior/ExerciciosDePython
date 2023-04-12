from math import sin, cos, tan, radians
ang = float(input('Valor do ângulo: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('\n')
print('\033[4;32mSeno:\033[m {:.2f}\n\033[4;32mCosseno:\033[m {:.2f}\n\033[4;32mTangente:\033[m {:.2f}'.format(seno, cosseno, tangente))
