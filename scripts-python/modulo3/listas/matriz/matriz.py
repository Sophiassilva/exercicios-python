matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição: [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somatc += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-='*25)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-='*25)
print(f'''A soma de todos os valores pares digitados foi {somapar},
A soma dos valores da terceira coluna foi {somatc},
O maior valor da segunda linha é {maior}.''')
