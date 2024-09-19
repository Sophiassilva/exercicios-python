partidas = [] 
jogador = {'nome': str(input('Nome do jogador: ')),
           'partidas': int(input('Qtd de partidas jogadas: '))}
totgols = 0
for i in range(0, jogador['partidas']):
    partidas.append(int(input(f'Quantos gols na partida {i+1}?: ')))
    totgols += partidas[i]
jogador['gols'] = partidas
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*25)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for i in range(0, jogador['partidas']):
    print(f'Na partida {i+1}, ele fez {jogador['gols'][i]} gols.')
print(f'Foi um total de {totgols} gols.')