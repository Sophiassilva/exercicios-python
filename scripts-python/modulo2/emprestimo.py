print('Bem-vindo à sua consulta de empréstimo! Por favor, responda as seguintes perguntas para a análise:')
valorcasa = float(input('Qual o valor da casa que quer comprar?: R$'))
valorsalario = float(input('Qual o seu salário mensal?: R$'))
anos = int(input('Em quantos anos planeja financiar?: '))

# end = '' n faz nada no fim da linha

prest = valorcasa/(anos*12)
prcsalario = 0.3*valorsalario
print(f'Para financiar uma casa no valor de R${valorcasa} em {anos}, a prestação será de R${prest:.2f} por mês.')
if prest > prcsalario:
    print('Infelizmente o seu empréstimo foi NEGADO, pois a prestação ultrapassou 30 porcento do seu salário mensal.')
else:
    print('Seu empréstimo foi APROVADO! Aguarde o nosso contato para continuar.')
    