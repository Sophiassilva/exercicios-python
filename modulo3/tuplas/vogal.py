nomes = ('Sophia', 'Arthur', 'Yan', 'Liz', 'Letícia', 'Fillipe', 'Carlos')

for nome in nomes:
    print(f'\nAs vogais no nome {nome} são ', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
