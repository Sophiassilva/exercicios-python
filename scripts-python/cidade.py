nome = input('Digite o nome da cidade: ')
nome = (nome.upper()).strip()
nome = nome.split()

print(f'O nome da cidade começa com "Santo"? {"SANTO" == nome[0]}')
