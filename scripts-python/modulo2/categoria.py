#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Para atletas com {idade} anos de idade, a categoria é ', end = '')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JÚNIOR.')
elif idade <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')
    