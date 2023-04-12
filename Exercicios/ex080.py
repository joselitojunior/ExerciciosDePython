print('\033[1;97m=' * 50)

lista = list()
for inputs in range(0, 5):
    while True:
        num = input('\033[1;35mDigite um número: ')
        if num.isnumeric() == True:
            break
    num = int(num)
    if inputs == 0 or num > lista[-1]:
        lista.append(num)
    else:
        qnt = 0
        while qnt <= len(lista):
            if num <= lista[qnt]:
                lista.insert(qnt, num)
                break
            qnt += 1

print('\033[1;97m=' * 50)
print('\033[1;35mOs números em ordem crescente fica:\033[1;97m', end=' ')
for c in range(0, len(lista)):
    if c == len(lista) - 1:
        print(f'{lista[c]}.')
    else:
        print(lista[c], end=', ')
print('\033[1;97m=' * 50)