from datetime import date
anoatual = date.today().year
ctps = {'nome': str(input('Nome: ')),
        'idade': (anoatual - int(input('Ano de nascimento: '))),
        'ctps': int(input('Nº da Carteira de Trabalho (0 se não tem): '))}
if ctps['ctps'] != 0:
    ctps['contratação'] = int(input('Ano de contratação: '))
    ctps['salário'] = float(input('Salário: '))
print('-='*25)
for k, v in ctps.items():
    print(f' -{k} é {v}')
print('-='*25)