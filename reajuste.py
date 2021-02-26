'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
------------------------------------------------
|       Salário       | Percentual de Reajuste |
------------------------------------------------
|      0-400,00       |          15%           |
|    400,01-800,00    |          12%           |
|   800,01-1200,00    |          10%           |
|  1200,01 - 2000,00  |           7%           |
|   Acima de 2000,00  |           4%           |
------------------------------------------------

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
'''

salario = float(input("Qual é o seu salário? "))

if salario <= 400:
    r = 15
    a = salario * (r / 100)
elif salario > 400 and salario <= 800: # Outra forma de escrever: elif: 400.01 <= salario < 800:
    r = 12
    a = salario * (r / 100)
elif salario > 800 and salario <= 1200:
    r = 10
    a = salario * (r / 100)
elif salario > 1200 and salario <= 2000:
    r = 7
    a = salario * (r / 100)
else:
    r = 4
    a = salario * (r / 100)
    
novoSalario = salario + a

print("O seu novo salário é de", "%.2f"%novoSalario, "com o valor do reajuste de", "%.2f"%a, "e a porcentagem de aumento de", r, "%")
