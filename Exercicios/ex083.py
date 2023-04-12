lista = []

print('\033[1;97m=' * 52)
e = str(input('\033[1;97mDigite a expressão: \033[m'))
for c in e:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if '(' in lista:
            lista.pop()
        else:
            lista.append(c)

if '(' not in e and ')' not in e:
    print('\033[1;97mNão há \033[31mnenhum\033[97m parêntese.')
elif len(lista) == 0:
    print('\033[1;97mOs \033[34mparênteses\033[97m na expressão estão em ordem \033[32mcorreta\033[97m!')
else:
    print('\033[1;97mOs \033[34mparênteses\033[97m na expressão estão em ordem \033[31mincorreta\033[97m!')
print('\033[1;97m=' * 52)
