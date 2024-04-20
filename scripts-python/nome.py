nome = input('Digite seu nome completo: ')

print(f"""Maiúsculo: {nome.upper()}
Minúsculo: {nome.lower()}
Espaços ocupados: {len(nome)}
Qtd. de letras 1º nome: {len((nome.split())[0])}
Total de letras: {len(nome) - nome.count(' ')}""")
