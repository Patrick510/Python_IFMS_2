"""Um heterograma é uma palavra ou frase em que nenhuma letra do alfabeto ocorre mais de uma vez.
Ler um número n, seguido por n frases, uma em cada linha. Para cada frase, escrever "S" ou "N" caso seja heterograma ou não.
"""
def is_heterograma(frase):
  letras = set()
  for letra in frase:
    if letra.isalpha():
      if letra.lower() in letras:
        return False
      letras.add(letra.lower())
  return True

entry = int(input(""))

for entries in range(entry):
  frase = input("").lower()
  
  if is_heterograma(frase):
    print("S")
  else:
    print("N")
