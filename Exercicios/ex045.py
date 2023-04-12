from time import sleep
import emoji
from random import choice

escolha = str(input(('\033[1;33m=\033[m' * 70+'\n\033[1;37mPedra\033[m'+emoji.emojize(':facepunch:', use_aliases=True)+
                    ', \033[1mpapel\033[m'+emoji.emojize(':hand:', use_aliases=True)+' ou '
                    '\033[1;33mtesoura'+emoji.emojize(':v:', use_aliases=True)+'\033[m? '))).strip().capitalize()
print('\033[1;33m=\033[m' * 70)

lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)

sleep(0.6)
print('\n\033[1mJO\033[m', end="")
sleep(0.5)
print(' \033[1mKEN\033[m', end="")
sleep(0.5)
print(' \033[1mPÔ\033[m !')
sleep(0.8)

if escolha == 'Pedra':
    eemoji = emoji.emojize(':facepunch:', use_aliases=True)
if escolha == 'Papel':
    eemoji = emoji.emojize(':hand:', use_aliases=True)
if escolha == 'Tesoura':
    eemoji = emoji.emojize(':v:', use_aliases=True)

if computador == 'Pedra':
    cemoji = emoji.emojize(':facepunch:', use_aliases=True)
if computador == 'Papel':
    cemoji = emoji.emojize(':hand:', use_aliases=True)
if computador == 'Tesoura':
    cemoji = emoji.emojize(':v:', use_aliases=True)

print(f'\n\033[4mVocê\033[m: {escolha}{eemoji}'
      f'\n\033[4mComputador\033[m: {computador}{cemoji}\n')

if escolha == 'Pedra' and computador == 'Pedra':
    print('\033[1;36mEMPATE!\033[m')
elif escolha == 'Pedra' and computador == 'Papel':
    print('\033[1;31mVocê perdeu...\033[m')
elif escolha == 'Pedra' and computador == 'Tesoura':
    print('\033[1;32mVOCÊ GANHOU!\033[m')

if escolha == 'Papel' and computador == 'Pedra':
    print('\033[1;32mVOCÊ GANHOU!\033[m')
elif escolha == 'Papel' and computador == 'Papel':
    print('\033[1;36mEMPATE!\033[m')
elif escolha == 'Papel' and computador == 'Tesoura':
    print('\033[1;31mVocê perdeu...\033[m')

if escolha == 'Tesoura' and computador == 'Pedra':
    print('\033[1;31mVocê perdeu...\033[m')
elif escolha == 'Tesoura' and computador == 'Papel':
    print('\033[1;32mVOCÊ GANHOU!\033[m')
elif escolha == 'Tesoura' and computador == 'Tesoura':
    print('\033[1;36mEMPATE!\033[m')
