m = int(input('Digete aqui algum valor em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'\033[1;31;47mQuilómetros: {km}\033[m\n\033[1;31;47mHectômetros: {hm}\033[m\n\033[1;31;47mDecâmetros: {dam}\033[m\n\033[1;31;47mDecímetros: {dm}\033[m\n\033[1;31;47mCentímetros: {cm}\033[m\n\033[1;31;47mMilímetros: {mm}\033[m')
