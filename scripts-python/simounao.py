from random import choice

res = ['SIM!', 'NÃO!']

quest = input('Faça uma pergunta: ')
print(f'A resposta para essa pergunta é sem dúvidas {choice(res)}')
