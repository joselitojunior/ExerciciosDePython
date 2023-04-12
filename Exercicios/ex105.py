def notas(* n, sit=False):
    '''
    -> Função para análise de notas e a situação de alunos.
    :param n: notas
    :param sit: (opcional) | True ou False
    :return: dicionário com a análise das notas.
    '''
    dicionario = dict()
    dicionario['quantidade'] = len(n)
    for p, nota in enumerate(n):
        if p == 0:
            maior = nota
            menor = nota
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    media = sum(n) / len(n)
    dicionario['media'] = media
    if sit:
        if media >= 7:
            dicionario['situação'] = 'BOA'
        elif media < 5:
            dicionario['situação'] = 'RUIM'
        else:
            dicionario['situação'] = 'RAZOÁVEL'
    return dicionario


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
