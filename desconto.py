valor = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto: '))
valorfinal = (desconto/100)*valor
valorfinal = valor - valorfinal 
print(f'O preço final do produto é R${valorfinal:.2f}.')
