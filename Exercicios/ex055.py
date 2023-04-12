maiorp = 0
menorp = 0

for pessoas in range(1,6):
    peso = float(str(input(f'\033[1;97mDigite o {pessoas}º peso: \033[m')).lower().replace('kg', ''))
    if pessoas == 1:
        maiorp = peso
        menorp = peso
    if peso > maiorp:
        maiorp = peso
    elif peso < menorp:
        menorp = peso

print(f'\n\033[1;32mO maior peso é {maiorp}.\033[m\n\033[1;36mO menor peso é {menorp}.\033[m')