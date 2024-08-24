numeros = [[], []]
temp = 0
for i in range(1, 8):
    temp = int(input(f'Digite o {i}º número: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)
for i in range(0, 2):
    numeros[i].sort()
print(f'''Os números pares digitados foram: {numeros[0]}
Os ímpares foram: {numeros[1]}''')