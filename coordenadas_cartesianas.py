# Escreva um programa que leia do teclado as coordenadas (x1 , y1) do ponto 1 e (x2, y2) do ponto 2. Utilizando a expressão do item 8.e, determine a distância entre esses dois pontos e exiba-a na tela com três casas decimais. Teste-o com os dados da tabela a seguir.
# D = sqrt(((X1-X2)**2) + ((Y1-Y2)**2))

print('Digite as coordenadas do ponto 1: ')
x1 = float(input('Digite a coordenada X: '))
y1 = float(input('Digite a coordenada Y: '))
print('Digite as coordenadas do ponto 2: ')
x2 = float(input('Digite a coordenada X: '))
y2 = float(input('Digite a coordenada Y: '))

from math import sqrt
distancia = sqrt(((x1-x2)**2) + ((y1-y2)**2))

print('A distância entre as coordenadas é: {:.3f}'.format(distancia))