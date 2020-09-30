'''nome = []
print('Olá')
nome.append(input('Digite um nome: '))

for n in nome:
    if len(n) == 4:
        print(n)
'''


ListaNome = []
nome = input('Digite um nome: ')

while nome != '':
    if len(nome) == 4:
        ListaNome.append(nome)
    nome = input('Digite um nome: ')
    
for x in range(len(ListaNome)):
    print(ListaNome[x])