dados = list()
pessoa = list()
maiorp = menorp = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(dados) == 0:
        maiorp = menorp = pessoa[1]
    else: 
        if pessoa[1] > maiorp:
            maiorp = pessoa[1]
        if pessoa[1] < menorp:
            menorp = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    continua = input('Deseja adicionar mais alguém à lista? [S/N]: ').strip().upper()
    if continua[0] == 'N':
        break
print(f'Foram cadastradas {len(dados)} pessoas no total.')
print(f'O maior peso registrado foi de {maiorp:.2f}kg. As pesoas com esse peso são: ', end='')
for p in dados:
    if p[1] == maiorp:
        print(f'{p[0]}...', end ='')
print()
print(f'O menor peso registrado foi de {menorp:.2f}kg. As pesoas com esse peso são: ', end='')
for p in dados:
    if p[1] == menorp:
        print(f'{p[0]}...', end ='')