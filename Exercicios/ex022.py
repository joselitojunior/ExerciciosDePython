nome = str(input('Digite seu nome completo: '))
nome = nome.strip()
print('\033[1;4;33m'+nome.upper()+'\033[m')
print('\033[1;4;34m'+nome.lower()+'\033[m')
junto = nome.replace(' ', '')
print(len(junto))
dividido = nome.split()
print(len(dividido[0]))
