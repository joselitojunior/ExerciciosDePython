from ex111.utilidadescev import dado, moeda

p = dado.leiadinheiro('\033[1;97mDigite o preço: ')
moeda.resumo(p, 35, 22, True)
