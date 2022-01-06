"""
Calculadora
Autor: Douglas
Função: Fazer contas (Soma, Subtração, Multiplicação e Divisão)
"""
print("-----CALCULADORA v1.0-----")

sair = False

while sair == False:

	num1 = int(input("Digite o 1º número: "))
	op = input("Digite o operador (+, -, * ou /): ")
	num2 = int(input("Digite o 2º número: "))
	
	# + = Soma
	if op == "+":
		operacao = num1 + num2

	# - = Subtração
	if op == "-":
		operacao = num1 - num2

	# * = Multiplicação
	if op == "*":
		operacao = num1 * num2

	# / = Divisão
	if op == "/":
		operacao = num1 / num2

	print("Resultado =", operacao)
	
	teste = input("Deseja Sair? (s/n): ")
	if teste == "s":
		sair = True
