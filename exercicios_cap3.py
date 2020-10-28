# Escreva um programa que leia um número inteiro do teclado e diga se esse número é positivo ou negativo. 
"""
n = int(input('Digite um número: '))
if n < 0:
    print(n, 'é negativo!')
else:
    print(n, 'é positivo!')
"""

# Escreva um programa que leia um número inteiro do teclado e diga se esse número é par ou ímpar. Para saber se um número é par, deve-se verificar se o resto de sua divisão por 2 é igual a zero. Para calcular o resto da divisão de um número por outro deve-se utilizar o operador %. Por exemplo: ao escrever a expressão em negrito a seguir e supondo que A e B tenham conteúdo inteiro. R = A % B, então, R é o resto da divisão de A por B
"""
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(n, 'é par!')
else:
    print(n, 'é ímpar!')
"""

# Escreva um programa que leia dois números quaisquer e mostre na tela qual é o menor e qual é o maior.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(n1, 'é maior que', n2)
elif n2 > n1:
    print(n2, 'é maior que', n1)
else:
    print(n1, 'e', n2, 'são números iguais')
"""

# Escreva um programa que leia três números reais e informe se eles constituem os lados de um triângulo. Em caso afirmativo, informe se o triângulo é equilátero, isósceles ou escaleno. Para que três números formem um triângulo, a soma dos dois lados menores deve ser maior que o lado maior. Uma boa solução para esse problema envolve o uso dos operadores and e or.
"""
l1 = int(input('Digite um tamanho de lado de um triângulo: '))
l2 = int(input('Digite outro tamanho de lado de um triângulo: '))
l3 = int(input('Digite mais um tamanho de lado de um triângulo: '))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2):
    if (l1 == l2) and (l2 == l3):
        print('Esse é um triângulo equilátero!')
    elif (l1 == l2) or (l2 == l3) or (l3 == l1):
        print('Esse é um triângulo isóceles!')
    else:
        print('Esse é um triângulo escaleno!')
else:
    print('Esse não é um triângulo!')
"""

# Escreva um programa que leia o nome de um lutador e seu peso. Em seguida, informe a categoria a que pertence o lutador, conforme o Quadro 3.9 (note que o quadro foi criado para efeito deste exercício e não condiz com qualquer categoria de luta). A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir: Nome fornecido: Pepe Jordão Peso fornecido: 73.4 Frase a ser exibida: O lutador Pepe Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro
"""
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
categoria = ''

if peso < 65:
    categoria = 'Pena'
elif peso >= 65 and peso < 72:
    categoria = 'Leve'
elif peso >= 72 and peso < 79:
    categoria = 'Ligeiro'
elif peso >= 79 and peso < 86:
    categoria = 'Meio-médio'
elif peso >= 86 and peso < 93:
    categoria = 'Médio'
elif peso >= 93 and peso < 100:
    categoria = 'Meio-pesado'
else:
    categoria = 'Pesado'

print('Nome fornecido: ', nome)
print('Peso fornecido: ', peso)
print('O lutador', nome, 'pesa', peso, 'kg e se enquadra na categoria', categoria,'.')
"""

# Escreva um programa que leia o valor hora que um profissional ganha na empresa onde trabalha. Leia também as quantidades de horas normais e horas extras trabalhadas em um mês. Calcule o valor a ser recebido pelo profissional nesse mês, sabendo que nas horas extras o pagamento é dobrado.

valor_hora = float(input('Digite o valor da hora de trabalho: '))
hora = int(input('Digite a quantidade de horas trabalhadas: '))
hora_extra = int(input('Digite a quantidade se horas extras, se teve: '))

salario = (valor_hora * hora) + ((valor_hora * 2) * hora_extra)

print('Você irá receber de salário a quantia de R$ {:.2f}'.format(salario))
