a = 1
b = a
b = 2
print(a, b)
c = [1, 2]
d = c
d[0] = 0
print(c, d)
d = c[:]
d[0] = 1
print(c, d)