n = int(input('\033[1;97mDigite um número:\033[m '))        #COM WHILE
prox = n
f = n
while prox != 1:
    prox -= 1
    f = f * prox
print(f'\033[1;97m{n}! = {f}\033[m')

#n = int(input('\033[1;97mDigite um número:\033[m '))     #COM FOR
#f = n
#for prox in range(n - 1, 0, -1):
#    f = f * prox
#print(f'\033[1;97m{n}! = {f}\033[m')
