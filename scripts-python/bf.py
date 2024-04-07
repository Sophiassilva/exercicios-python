from random import choice

print('Esse programa diz quem vai ser seu próximo namorado. Digite os nomes a seguir:')

n1 = str(input('1º: '))
n2 = str(input('2º: '))
n3 = str(input('3º: '))
n4 = str(input('4º: '))

lista = [n1, n2, n3, n4]

print(f'De acordo com o destino, será: {choice(lista)}.')
