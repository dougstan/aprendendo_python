# Leia 2 valores inteiros (A e B). Após o programa deve mostrar "São múltiplos" ou "Não são múltiplos", indicando se os valores lidos são múltiplos entre si.

'''A = int(input("Digite o 1o número: "))
A = int(input("Digite o 2o número: "))'''

A, B = map(int, input("Digite 2 números: ").split()) # MAP (tipo_variavel, leitura_no_disp_entrada) e SPLIT para quebrar a leitura do dispositivo de entrada, separando os valores

if A % B == 0 or B % A == 0:
    print(A ,"e", B, "são múltiplos")
else:
    print(A ,"e", B, "não são múltiplos")