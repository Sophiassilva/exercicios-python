dados = list()
pessoa = dict()
media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('ERRO! Digite M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    dados.append(pessoa.copy())
    pessoa.clear()
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp not in 'SN':
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
media = media/len(dados)
print('-='*25)
print(f'A) Ao todo, temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.1f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p['nome']}...', end='')
print()
print('D)Lista de pessoas que estão com a idade acima da média: ')
for p in dados:
    if p['idade'] > media:
        print(p)
print('Encerrando...')