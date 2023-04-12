while True:
    n = int(input('\033[1;97mTabuada de:\033[m '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[1;35m{n} \033[1;97mx {c}: {n * c}\033[m')
    print('-' * 30)
print('\n\033[1;32mPrograma finalizado.\033[m')