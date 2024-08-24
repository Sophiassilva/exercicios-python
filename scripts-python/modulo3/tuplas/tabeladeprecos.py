lista = ('212 Heroes Feminino', 500.00, 'Scandal Feminino', 490.00, 'Eudora Rosé', 220.00 ,
          'Una Blush', 200.00, 'Grace Midnight', 160.00)
print('-'*35)
print(f'{"Perfumes":^35}')
print('-'*35)

for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<25}', end='')
    print(f'R$ {lista[i+1]:.2f}')
print('-'*35)