números = []
while True:
    números.append(int(input('Digite um número: ')))
    continua = input('Deseja continuar?[S/N]: ').upper().strip()
    if continua[0] == 'N':
        break
números.sort(reverse=True)
print(f'''Foram digitados {len(números)} números,
A lista em ordem decrescente é: {números},''')
if 5 in números:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
