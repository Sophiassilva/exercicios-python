from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
print(f'Para o ângulo de {ang},')
ang = radians(ang)
print(f'o cosseno é {cos(ang):.2f}, o seno é {sin(ang):.2f} e a tangente é {tan(ang):.2f}')
