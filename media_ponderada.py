# Leia 3 valores, no caso variáveis A, B e C, que são as três notas de um aluno. Em seguida, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que a nota pode ir de 0 a 10, sempre com uma casa decimal.

#Entrada
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))

#Processamento
media = (a * 2 + b * 3 + c * 5) / 10
media = str("%.1f"%media) #Para exibir a média com uma casa decimal

#Saída
print("A média é de:", media)