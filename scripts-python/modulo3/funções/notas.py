def notas(*num, sit=False):
    """
    --- Função para analisar notas de um aluno
    :param num: n notas do aluno
    :param sit: mostrar situação do aluno no boletim
    :return: dicionário com o boletim do aluno
    """
    boletim = {'total': len(num), 
               'maior': max(num), 
               'menor': min(num), 
               'média': sum(num)/len(num)}
    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'APROVADO'
        elif 5 <= boletim['média'] < 7:
            boletim['situação'] = 'RECUPERAÇÃO'
        else:
            boletim['situação'] = 'REPROVADO'
    return boletim


boletim = notas(10, 5, 10, sit=True)
print(boletim)