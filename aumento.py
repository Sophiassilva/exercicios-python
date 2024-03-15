salario = float(input('Digite o valor do seu salário: '))
aumento = float(input('Digite o valor do aumento: '))
salariofinal = (aumento/100)*salario
salariofinal = salariofinal + salario
print(f'O novo valor do seu salário é R${salariofinal:.2f}.')
