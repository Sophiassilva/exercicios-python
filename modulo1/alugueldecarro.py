dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos km foram percorridos: '))
aluguel = 60*dias + 0.15*km
print(f'O  preço do aluguel do carro é R${aluguel:.2f}.')
