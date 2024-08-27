def maior(*num):
    maior = i = 0
    for n in num:
        if i == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        i += 1
    print(f'Dos valores {num}, o maior deles é {maior}')


maior(0, 9, -13, 200)