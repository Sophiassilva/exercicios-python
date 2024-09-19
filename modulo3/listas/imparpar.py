numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    continua = input('Deseja continuar? [S/N]: ').upper().strip()
    if continua[0] == 'N':
        break
numeros.sort()
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'''A lista de números geradas foi: {numeros}
Os números pares são: {pares}
Os números ímpares são: {impares}''')
