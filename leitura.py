# Função que separa cada palavra e a coloca em uma lista, além de mostrar a quantidade de palavras que há em um arquivo.
def palavras(nomearq):
    infile = open('D:\\Douglas\\Documents\\repositorios\\aprendendo_python\\exemplo.txt', 'r')
    conteudo = infile.read()
    infile.close()

    listaPalavras = conteudo.split()
    print(listaPalavras)
    return len(listaPalavras)

print(palavras('exemplo.txt'))