def fatorial(num, show=False):
    f = 1
    for i in range(1, num+1):
        f *= i
        if show:
            print(f'{f}...', end='')
    print()
    print(f'O fatorial de {num} é {f}')


num = int((input('Digite um número: ')))
resp = input('Deseja ver o processo?[S/N]: ').strip().upper()
if resp == 'S': 
    fatorial(num, True)
else:
    fatorial(num)