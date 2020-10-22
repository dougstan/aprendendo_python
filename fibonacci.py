# Programa que gera a sequência de Fibonacci
# Escreva um programa que leia um número inteiro N e, em seguida, mostre na tela os N primeiros termos da sequência de Fibonacci. Faça o programa de modo que N seja no mínimo 2.

print('Sequência de Fibonacci:')
N = 0

while N < 2:
    try:
        N = int(input('Digite N > 1: '))
        if N < 2:
            print('Digite N >= 2')
    except:
        print('O dado deve ser um número inteiro!')

A = 0
B = 1
print('0, 1, ', end='') # Exibe os 2 primeiros termos
i = 0

while i < N-2: # O laço tem que exibir N - 2 termos, pois os dois primeiros já foram exibidos fora do laço
    C = A + B
    print('{}, '.format(C), end='') # o end suprime a mudança de linha
    A = B                           # na exibição da tela
    B = C
    i += 1

print('\nFim do programa!')
