nome = str(input('Digite seu nome completo:')).strip().lower().title().split()
print('\033[1;34mMuito prazer em te conhecer!\033[m')
print('Seu primeiro nome é \033[0;32m{}\033[m.'.format(nome[0]))
print('Seu último nome é \033[0;32m{}\033[m.'.format(nome[len(nome)-1]))
