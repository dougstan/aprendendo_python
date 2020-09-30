'''
Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de 4 letras nessa lista Python
'''
# O que fiz antes de ver
'''
print('Olá')
nome = input("Digite um nome: ")#.split(' ')
for n in nome:
    if len(nome) == 4:
        print(n)
'''
# Depois de corrigido
'''
Seu código para validar as palavras com 4 letras e exibi-las está correto, o problema é que você está executando uma vez apenas o código, ou seja, armazena 1 nome, exibe (ou não) e termina o programa com sucesso.

Se você quiser que ele continue pedindo e printando os nomes tem que colocar um laço. Por exemplo, o while, assim, enquanto a condição for verdadeira o processo continua.

Tentei entender seu problema e fiz algumas alterações: Criei uma lista para armazenar todos os nomes, coloquei o while para continuar pedindo novos nomes enquanto não receber um input vazio e coloquei o print no final, após escapar do laço.

Ahh, e na lista só são adicionados os nomes com exatos 4 caracteres.
'''
ListaNome = []
nome = input('Digite um nome: ')

while nome != '':
    if len(nome) == 4:
        ListaNome.append(nome)
    nome = input('Digite um nome: ')
    
for x in range(len(ListaNome)):
    print(ListaNome[x])