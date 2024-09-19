from random import shuffle

print('Esse programa embaralha uma lista de nomes. Digite-os a seguir:')

n1 = str(input('1º: '))
n2 = str(input('2º: '))
n3 = str(input('3º: '))
n4 = str(input('4º: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print(lista)
