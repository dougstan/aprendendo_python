# Fala o preço a pagar de uma compra usando um código do produto, a quantidade e o preço unitário

codigo1 , qtde1, valor1 = map(float, input("Digite as informações para produto 1: codigo, qtde, valor\n").split())
codigo2 , qtde2, valor2 = map(float, input("Digite as informações para produto 2: codigo, qtde, valor\n").split())

# o map converte para float o que foi digitado, e o split separa por cada item

valor_total = (qtde1 * valor1) + (qtde2 * valor2)

print("Valor a pagar: R$", str("%.2f"%valor_total))