s1 = int(input('1º segmento: '))
s2 = int(input('2º segmento: '))
s3 = int(input('3º segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Esse segmentos formam um triângulo ', end = '')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif (s1 == s2 or s2 == s3 or s1 == s3) and (s1 != s2 or s2 != s3 or s1 != s3):
        print('ISÓSCELES.')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO.')
else: 
    print('Esses segmentos não podem formar um triângulo.')