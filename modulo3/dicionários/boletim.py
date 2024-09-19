boletim = dict()
aluno = list()
while True:
    boletim['nome'] = input('Nome: ')
    boletim['média'] = float(input('Média: '))
    if boletim['média'] >= 7:
        boletim['resultado'] = 'APROVADO' 
    else:
        boletim['resultado'] = 'REPROVADO'
    aluno.append(boletim.copy())
    boletim.clear()
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
for a in aluno:
    print('-='*15)
    for k, v in a.items():
        print(f'{k} é {v}')
