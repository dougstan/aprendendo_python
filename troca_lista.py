# Exercício: Criar uma função para Troca de valores em listas, trocando o primeiro e o último item. A função não deve retornar nada.

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

def trocaPU(ingredientes):
    ingredientes[0], ingredientes[-1] = ingredientes[-1], ingredientes[0]
    #print(ingredientes)

trocaPU(ingredientes)