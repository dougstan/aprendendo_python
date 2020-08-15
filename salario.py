#Programa que lê o nome de um vendedor, o seu salário e o total de vendas no mês (em dinheiro). Informa o total que ele recebe no mês, com mais 15% de desconto de comissão nas vendas.

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário mensal: "))
vendas = float(input("Digite o total de vendas: "))

salario_final = salario + vendas*0.15
salario_final = str("%.2f"%salario_final)

print("Total = ", salario_final)