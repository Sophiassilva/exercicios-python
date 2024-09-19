from time import sleep

def contador(i, f, p):
    print('-='*16)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1)
    if p < 0:
        p = p*(-1)
    if p == 0:
        p = 1
    if i > f:
        while i >= f:
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
            i -= p
        print('FIM!')
    else:
        while f >= i:
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
            i += p
        print('FIM!')
    print('-='*16)

contador(1, 10, 1)
contador(10, 0, 2)
contador(10, 0, -2)
contador(1, 10, 0)