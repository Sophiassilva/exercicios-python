n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
media = (n1+n2)/2

print(f'A sua média é {media:.1f}, logo você está ', end = '')

if media < 5:
    print('REPROVADO. Tente novamente semestre que vem, não desista!')
elif media >= 5 and media <= 6.9:
    saldo = 7 - media
    print(f'de RECUPERAÇÃO, você ainda precisa de {saldo:.1f} na média para passar. Você consegue!')
else:
    print('APROVADO! Parabéns pelo seu empenho!')
