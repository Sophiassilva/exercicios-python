# le um numero inteiro e converte: 1 para binario,, 2 para octal, 3 para hexa
num = int(input('Digite o número a ser convertido: '))
base = int(input('''Escolha qual base será convertido:
                 1 - Binário
                 2 - Octal
                 3 - Hexadecimal'''))

print(f'O número {num} na base ', end = '')
if base == 1:
    print(f'binária é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'octal é igual a {oct(num)[2:]}')
else:
    print(f'hexadecimal é igual a {hex(num)[2:]}')
    