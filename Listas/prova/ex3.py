"""Ler duas frases, uma em cada linha. Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase. Escrever em outra linha as palavras da primeira frase que oorrem na segunda frase.
"""

frase1 = "Ontem fui na feira comprar pao"
frase2 = "Hoje não fui na feira"

palavras_frase1 = set(frase1.split())
palavras_frase2 = set(frase2.split())

palavras_nao_ocorrem_frase2 = palavras_frase1.intersection(palavras_frase2)
palavras_ocorrem_frase2 = palavras_frase1.difference(palavras_frase2)

print(f'Palavras da primeira frase que não ocorrem na segunda frase: {palavras_nao_ocorrem_frase2}')
print(f'Palavras da primeira frase que ocorrem na segunda frase: {palavras_ocorrem_frase2}')