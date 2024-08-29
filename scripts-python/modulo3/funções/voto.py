from datetime import date

def voto(idade):
    s = str
    if idade >= 18 and idade <= 65:
        s = 'OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        s = 'OPCIONAL'
    else: 
        s = 'NEGADO'
    return s


ano = int(input('Em qual ano você nasceu?: '))
idade = date.today().year - ano
print(f'Por ter {idade} anos de idade, o seu voto é {voto(idade)}.')
