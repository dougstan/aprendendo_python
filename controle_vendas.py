"""
Um vendedor ambulante vendeu os produtos indicados na tabela a seguir. Informe quanto ele faturou com cada produto e quanto ele faturou no total.

Produto            |  Quantidade vendida  |  Valor unitário R$
--------------------------------------------------------------------
Boneco Malandrinho |  17                  |  18,50
Spinner Pequeno    |  36                  |  12,00
Cubo Mágico        |  7                   |  5,90

Todos os dados devem ser lidos do teclado, sendo que o nome do produto é string, a quantidade vendida é um número inteiro e o valor unitário é um número real.
"""

print('Controle de vendas')
prod1 = input('Digite o primeiro produto: ')
qtde1 = int(input('Quantidade vendida: '))
valor1 = float(input('Valor do produto: '))
prod2 = input('Digite o segundo produto: ')
qtde2 = int(input('Quantidade vendida: '))
valor2 = float(input('Valor do produto: '))
prod3 = input('Digite o terceiro produto: ')
qtde3 = int(input('Quantidade vendida: '))
valor3 = float(input('Valor do produto: '))

vendas_prod1 = qtde1 * valor1
vendas_prod2 = qtde2 * valor2
vendas_prod3 = qtde3 * valor3
vendas = vendas_prod1 + vendas_prod2 + vendas_prod3

print('Quantidade do item {0}: {1} - Valor: R$ {2:.2f}'.format(prod1, qtde1, vendas_prod1))
print('Quantidade do item {0}: {1} - Valor: R$ {2:.2f}'.format(prod2, qtde2, vendas_prod2))
print('Quantidade do item {0}: {1} - Valor: R$ {2:.2f}'.format(prod3, qtde3, vendas_prod3))
print('Total das vendas: R$ {:.2f}'.format(vendas))