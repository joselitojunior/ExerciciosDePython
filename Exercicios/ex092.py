from datetime import date
ano = date.today().year
pessoa = {}

print('\033[1;97m=' * 50)
pessoa['nome'] = str(input('\033[1;33mNome: ')).strip().lower().title()
pessoa['idade'] = ano - int(input('\033[1;36;4mAno\033[m\033[1;36m de nascimento: '))
pessoa['carteira de trabalho'] = int(input('\033[1;35mCarteira de trabalho (0 se não tiver): '))
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratacao'] = int(input('\033[34mAno de contratação: '))
    pessoa['aposentar'] = pessoa['idade'] + 35 - (ano - pessoa['ano de contratacao'])
    salario = float(str(input('\033[1;32mSalário: R$')).replace('.', '').replace(',', '.', 1))
    pessoa['salário'] = f'R${salario:.2f}'
else:
    pessoa.pop('carteira de trabalho')
print('\033[1;97m=' * 50)
for k, v in pessoa.items():
    print(f'\033[1;97m{k.capitalize()}: {v}')
print('\033[1;97m=' * 50)
