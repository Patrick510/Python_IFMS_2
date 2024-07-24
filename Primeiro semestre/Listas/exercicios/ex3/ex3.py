"""Ler duas frases, uma em cada linha. Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase. Escrever em outra linha as palavras da primeira frase que oorrem na segunda frase.
"""

frase1 = "Hoje fui na feira"
frase2 = "Hoje não vou na feira"

palavras_frase1 = set(frase1.split())
palavras_frase2 = set(frase2.split())

palavras_ocorrem = []
palavras_nao_ocorrem = []

for palavra in palavras_frase1:
  if palavra in palavras_frase2:
    palavras_ocorrem.append(palavra)
  else:
    palavras_nao_ocorrem.append(palavra)

print(frase1)
print(frase2)

print(f"Palavras da primeira frase que não ocorrem na segunda frase: {palavras_nao_ocorrem}")
print(f"Palavras da primeira frase que oorrem na segunda frase: {palavras_ocorrem}")