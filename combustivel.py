'''
Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva o algoritmo para ler o tipo de combustível abastecido:
1) Álcool
2) Gasolina
3) Diesel
4) Fim
Caso o usuário digite um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido).
O programa será encerrado quando o código informado for 4.
'''
op = "1"
alc = 0
gas = 0
die = 0

print("1) Álcool")
print("2) Gasolina")
print("3) Diesel")
print("4) Fim")

while op != "4":
    op = input("Digite a opção desejada: ")

    if op == "1":
        alc += 1
    elif op == "2":
        gas += 1
    elif op == "3":
        die += 1
    else:
        print("Opção errada! Digite a opção certa!")
    

print("Quantidade de abastecimentos:")
print("1) Álcool:", alc)
print("2) Gasolina:", gas)
print("3) Diesel:", die)
print("Muito obrigado!")

