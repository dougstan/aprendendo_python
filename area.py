''' Escreva um programa que leia 3 valores com ponto flutuante de dupla precisão: A, B, e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura;
b) a área do círculo de raio C (pi = 3.14159);
c) a área do trapézio que tem A e B por bases e C por altura;
d) a área do quadrado que tem lado B;
e) a área do retângulo que tem lados A e B.
'''
#a = float(input("Digite valor A: "))
#b = float(input("Digite valor B: "))
#c = float(input("Digite valor C: "))
a, b, c = map(float, input("Digite A, B e C: ").split())

from math import pi
tri_ret = a * c / 2 # Base = A e Altura = C
circ = pi * c ** 2 # Raio = C
trap = (c * (a + b)) / 2 # C = Altura; A e B = tamanho bases menor e maior
quad = b ** 2 # Lado = B
ret = a * b # Lados: A e B

print("Valores digitados -> A:", a, " B:", b, " C:", c)
print("Área do triângulo retângulo:", str("%.2f"%tri_ret))
print("Área do círculo:", str("%.2f"%circ))
print("Área do trapézio:", str("%.2f"%trap))
print("Área do quadrado:", str("%.2f"%quad))
print("Área do retângulo:", str("%.2f"%ret))