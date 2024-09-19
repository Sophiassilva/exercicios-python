print('Digite quatro números a seguir: ')
números = ( int(input('1º: ')),
           int(input('2º: ')), 
           int(input('3º: ')), 
           int(input('4º: ')))
par = 0
for c in range(0, 4):
    if números[c] % 2 == 0:
        par += 1
print(f'''O número 9 apareceu {números.count(9)} vezes
Foram digitados {par} números pares''')
if 3 in números:
    print(f'O valor 3 apareceu na posição {números.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
