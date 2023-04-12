pt = int(input('Digite o primeiro termo da \033[0;33mPA\033[m: '))
r = int(input('Digite a razão da \033[0;33mPA\033[m: '))

p = pt

if r > 0:
    for final in range(0, 9):
        p = p + r
    for c in range(pt, p+1, r):
        print(c)
elif r < 0:
    for final in range(0, 9):
        p = p + r
    for c in range(pt, p-1, r):
        print(c)
else:
    for c in range(0, 10):
        print(pt)
