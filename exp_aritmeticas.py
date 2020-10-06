# 1) R = (A + B) / 2

# 2) X = (-B + RAIZ(B^2 - 4AC)) / 2A

# 3) E = (3A + 2B) / (A + B)

# 4) Z = 7.6A - B ^ 1.7

# 5) D = RAIZ((X1-X2)^2 + (Y1-Y2)^2)

# Valores: A = 4, B = 5, C = 1 e na última expressão: X1 = 1, Y1 = 1, X2 = 4 e Y2 = 5

A = 4
B = 5
C = 1

R = (A + B) / 2
print(R)

from math import sqrt
X = (-B + sqrt((B**2) - (4 * A * C))) / (2 * A)
print(X)

E = (3*A + 2*B) / (A + B)
print(E)

Z = 7.6*A - B**1.7
print(Z)

X1 = 1
X2 = 4
Y1 = 1
Y2 = 5
D = sqrt(((X1-X2)**2) + ((Y1-Y2)**2))
print(D)