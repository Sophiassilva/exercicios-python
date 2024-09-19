def nome(nome):
    global jogador
    if nome == '':
        jogador = '<desconhecido>'


def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol/s.')


jogador = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantos gols o jogador fez?: '))
nome(jogador)
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador, gols)