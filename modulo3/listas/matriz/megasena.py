from random import randint
jogos = list()
cartela = list()
num = 0
qtd = int(input('Quantos jogos deseja?: '))
for i in range(0, qtd):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in cartela:
            num = randint(1, 60)
        cartela.append(num)
        if j == 5:
            if cartela in jogos:
                j = 0
    cartela.sort()
    jogos.append(cartela[:])
    cartela.clear()
for l in range(0, qtd):
    print(f'{l+1}º Jogo: {jogos[l]}')
