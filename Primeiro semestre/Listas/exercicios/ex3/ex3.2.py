"""Ler duas frases, uma em cada linha. Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase. Escrever em outra linha as palavras da primeira frase que oorrem na segunda frase.
"""

frases = []
palavras_ocorrem = []
palavras_nao_ocorrem = []

for indice in range(2):
  entry = str(input(f"Frase {indice+1}:"))
  frases.append(entry.split())

for palavra in frases[0]:
  if palavra in frases[1]:
    palavras_ocorrem.append(palavra)
  else:
    palavras_nao_ocorrem.append(palavra)

print(f"Palavra(s) da primeira frase que não ocorrem na segunda frase: {palavras_nao_ocorrem}")
print(f"Palavras(s) da primeira frase que ocorrem na segunda frase: {palavras_ocorrem}")