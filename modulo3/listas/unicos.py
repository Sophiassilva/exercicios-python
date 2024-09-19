números = []
while True:
    num = int(input('Digite um número: '))
    if num in números:
        print('Esse número já foi adicionado.')
    else:
        print('Valor adicionado.')
        números.append(num)
    continua = input('Deseja continuar? [S/N]: ').lower().strip()
    if continua[0] == 'n':
        break
números.sort()
print('A lista digitada por ordem crescente é: ', end='')
for n in números:
    print(f'{n} ', end='')
