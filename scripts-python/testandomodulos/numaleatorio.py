import random
num1, num2 = map(int, input('Digite um intervalo de números, de forma crescente: ').split())
print(random.randint(num1, num2))
