nome = input('Digite seu nome completo: ')
nome = ((nome.upper()).strip()).split()

print(f'Tem Silva no nome? {'SILVA' in nome}')
