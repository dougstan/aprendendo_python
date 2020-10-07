"""
A média harmônica amortizada é definida como: 𝐻=𝑁/(∑1𝑛𝑖+𝑋𝑁𝑖=1−𝑋) onde N é o número de notas a serem usadas na média, ni é a i-ésimanota, e X é o fator de amortização. Implemente uma função em Python que calcule a média de 3 notas de um aluno digitadas no teclado, com fator de amortização igual a 4. Em seguida, informe se o aluno passou (média >= 5) ou não (média < 5)
"""

n1 = float(input('Informe a 1a nota: '))
n2 = float(input('Informe a 2a nota: '))
n3 = float(input('Informe a 3a nota: '))

def calc_media(n1, n2, n3):
    media = (3 / ((1 / (n1 + 4))+(1 / (n2 + 4))+(1 / (n3 + 4)))) - 4
    return media # Para o valor ser utilizado depois

media = calc_media(n1, n2, n3) # Função acionada e salva na variável media

print('Média: {:.1f}'.format(media))
if media >= 5:
    print('Aluno Aprovado!!!')
else:
    print('Aluno Reprovado!!!')

# Comentário: deu mais trabalho ver e passar a formula da média harmônica, e depois tive que lembrar que era pra criar uma função e usar return nela para poder utilizar o valor.