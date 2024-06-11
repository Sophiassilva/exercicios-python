def hipotenusa(oposto, adjacente):
    res = (oposto ** 2 + adjacente ** 2) ** 0.5
    return res
 
num1 = float(input('Digite o comprimento do cateto oposto: '))
num2 = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O resultado é {hipotenusa(num1, num2):.2f}')
