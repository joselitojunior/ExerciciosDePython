cidade = str(input('\033[1;35mQual o nome da sua cidade?\033[m '))
print(cidade.strip())
cidade = cidade.lower().replace('-',' ').split()
print(cidade[0] == 'santo')
