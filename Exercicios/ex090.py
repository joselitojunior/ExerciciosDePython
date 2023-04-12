aluno = dict()

print('\033[1;97m'+'=' * 50)

while True:
    aluno['nome'] = str(input('\033[1;33mNome\033[97m do aluno: ')).strip().lower().title()
    if aluno['nome'].isalpha():
        break
    else:
        del aluno['nome']
while True:
    aluno['media'] = str(input(f'\033[1;35mMédia\033[97m de {aluno["nome"]}: ')).replace(' ', '').replace(',', '.', 1)
    aluno2 = aluno['media']
    if '.' in aluno['media']:
        aluno2 = aluno['media'].replace('.', '', 1)
    if aluno2.isnumeric():
        aluno['media'] = float(aluno['media'])
        break
    else:
        del aluno['media']
aluno['situação'] = '\033[1;32mAprovado' if aluno['media'] >= 7 else '\033[1;31mReprovado'

print('\033[1;97m'+'=' * 50)

print(f'\033[1;97mAluno: \033[33m{aluno["nome"]}')
print(f'\033[1;97mMédia: \033[35m{aluno["media"]}')
print(f'\033[1;97mSituação: {aluno["situação"]}')

print('\033[1;97m'+'=' * 50)
