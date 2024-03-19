"""Um pangrama é uma frase em que são usadas todas as letras do alfabeto de determinada língua. Exemplo de pangrama em inglês: The quick brown fox jumps over the lazy dog. Exemplo de pangrama em português, desconsiderando as letras de origem saxônica: Blitz prende ex-vesgo com cheque fajuto.

Ler um número n, seguido por n frases, uma em cada linha. Para cada frase, escrever "S" ou "N" caso seja pangrama inglês ou não (desconsidera acentos).

elif alfabeto_portugues.issubset(frase_limpa.replace("ç","c").replace("á","a").replace("ã","a")):
"""

entry = int(input())
alfabeto = set("abcdefghijklmnopqrstuvwxyz")
alfabeto_portugues = set("abcdefghijlmnopqrstuvxz")

for entries in range(entry):
  frase = input().lower()
  frase_limpa = ''.join(filter(str.isalpha, frase))
  if alfabeto.issubset(frase_limpa):
    print("S")
  elif alfabeto_portugues.issubset(frase_limpa):
    print("S")
  else:
    print("N")


