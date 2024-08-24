seriea = ('Botafogo', 46, 'Fortaleza CE', 45,'Flamengo', 41, 'Palmeiras', 41, 'Bahia', 38)

print('Aqui está a situação dos 5 primeiros colocados na série A do Brasileirão em 19/08/2024')
num = 1

while True:
    for i in range (0, 10, 2):
        print(f'O time {seriea[i]} está na {num}ª posição, com {seriea[i+1]} pontos.')
        num += 1
    break
