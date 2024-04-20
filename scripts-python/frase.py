import platform

implem = platform.python_implementation()
print(f"{implem}")

frase = 'Olá tudo bem?'
print(frase.find('?'), frase.count('o', 0, 7), frase.find('s'), 'Curso' in frase, 
      frase.replace('tudo', 'todos'), frase.split(), '-'.join(frase), len(frase))
