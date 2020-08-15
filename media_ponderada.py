#Entrada
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))

#Processamento
media = (a * 2 + b * 3 + c * 5) / 10
media = str("%.1f"%media) #Para exibir a média com uma casa decimal

#Saída
print("A média é de: ", media)