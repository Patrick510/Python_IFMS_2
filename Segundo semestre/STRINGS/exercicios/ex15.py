# Dadas duas strings, elas possuem a mesma sequência de vogais, desconsiderando outros caracteres? Por exemplo, litoral, e picotar possuem a mesma sequência de vogais "ioa".

s1 = input()
s2 = input()

def extrair_vogais(s):
  vogais = "aeiouAEIOU"
  return " ".join([letra for letra in s if letra in vogais])

if extrair_vogais(s1) == extrair_vogais(s2):
  print("Sim")