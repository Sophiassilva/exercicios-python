números = []
for i in range(0,5):
    números.append(int(input(f'Digite o {i+1}º número: ')))
print(f'O maior número digitado foi {max(números)}, encontrado nas seguintes posições da lista: ', end='')
for i, n in enumerate(números):
    if n == max(números):
        print(f'{i}...' , end='')
print(f'\nO menor número digitado foi {min(números)}, encontrado nas seguintes posições da lista: ', end='')
for i, n in enumerate(números):
    if n == min(números):
        print(f'{i}...' , end='')