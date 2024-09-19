#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele 
# ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
import datetime

ano = int(input('Digite seu ano de nascimento: '))

date = datetime.date.today()
anoatual = int(date.strftime("%Y"))
##anoatual = date.today().year
idade = anoatual - ano

if idade == 18:
    print('Você está na idade para se alistar.')
elif idade < 18:
    print(f'Você não tem idade para se alistar. Ainda faltam {18-idade} anos. Aliste-se em {ano+18}.')
else:
    print(f'Você está com seu alistamento {idade-18} anos atrasado. Você devia ter se alistado em {ano+18}.')
