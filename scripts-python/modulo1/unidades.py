num = int(input('Digite um número de 0 a 9999: '))

u = int(num%10)
num = num/10
d = int(num%10)
num = num/10
c = int(num%10)
num = num/10
m = int(num%10)

print(f"""Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}""")
