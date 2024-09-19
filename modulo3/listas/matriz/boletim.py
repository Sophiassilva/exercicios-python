boletim = list()
num = 0
while True:
    aluno = [str(input('Nome: ')), float(input('1ª nota: ')), float(input('2ª nota: '))]
    media = (aluno[1] + aluno[2])/2
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    resp = input('Deseja adicionar mais um aluno?[S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
print('-='*20)
print(f'{'N°':<3} {'Nome':<12} {'Média':<8}')
print('-'*25)
for i, a in enumerate(boletim):
    print(f'{i:<3} {a[0]:<12} {a[3]:<8.1f}')
print('-'*25)
while True:
    num = int(input('Mostrar notas de qual aluno? (Digite 999 caso deseje sair): '))
    if num == 999:
        break
    elif num < len(boletim):
        print(f'As notas do aluno {boletim[num][0]} são: {boletim[num][1:3]}.')
        print('-'*25)
    else:
        print('Aluno não encontrado. Tente novamente!')
print('Até logo!')