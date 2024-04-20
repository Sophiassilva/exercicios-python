frase = input('Digite uma frase: ')
frase = (frase.strip()).lower()

print(f'Essa frase tem {frase.count('a')} letras A, o primeiro é na posição {frase.find('a')+1} e o último na posição {frase.rfind('a')+1}')