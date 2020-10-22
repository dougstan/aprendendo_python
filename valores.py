# Programa que totaliza um conjunto de valores

# Escreva um programa que leia um número inteiro N e, em seguida, gere N números aleatórios no intervalo [1, 50] e totalize-os. Para gerar números aleatórios, use a função randint, disponível na biblioteca random.

from random import randint

N = int(input('Digite N: '))
total = 0 # Cria objeto Total zerado
i = 1

while i <= N:
    x = randint(1, 50) # Gera um valor para x
    print('Valor {} gerado = {}'.format(i, x)) # Exibe x na tela
    total = total + x # Acumula x em total
    i += 1

print('\nSoma dos valores gerados = {}'.format(total))