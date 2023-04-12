n = int(input('Digite um número: '))

d = n * 2
t = n * 3
rq = n**(1/2)

print('\033[0;34mDobro: {}\033[m\n\033[0;36mTriplo: {}\033[m\n\033[0;31mRaiz quadrada: {:.2f}\033[m'.format(d, t, rq))
