nome = input('Digite seu nome completo: ')
nome = (nome.strip()).split()

print(f"""Nome: {nome[0]}
Último nome: {nome[len(nome)-1]}""")