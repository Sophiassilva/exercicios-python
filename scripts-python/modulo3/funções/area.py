def area(b, h):
    r = b*h
    print(f'A área de um terreno de dimensões {b}x{h} é de {r}m²')


print(f'{'Controle de Terrenos':^25}')
print('-'*25)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)