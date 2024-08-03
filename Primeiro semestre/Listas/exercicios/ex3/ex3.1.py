frase1 = "Hoje fui na feira"
frase2 = "Hoje não vou no shopping"

palavras_frase1 = set(frase1.split())
palavras_frase2 = set(frase2.split())

print(palavras_frase1)
print(palavras_frase2)

palavras_ocorrem = palavras_frase1.intersection(palavras_frase2)
palavras_nao_ocorrem = palavras_frase1.difference(palavras_frase2)

print(f"Palavras que ocorrem em ambas as frases: {palavras_ocorrem}")
print(f"Palavras que ocorrem apenas na primeira frase: {palavras_nao_ocorrem}")
