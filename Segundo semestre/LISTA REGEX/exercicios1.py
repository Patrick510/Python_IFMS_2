import re

# 1 - Na língua portuguesa, palavras no plural terminam com “s”. Receber uma string e retornar uma lista com as palavras que terminam com “s”.

def ex1(string):
  pattern = r'\b[\w\'`]+s\b'
  return re.findall(pattern, string)

# print(ex1("Os gatos e cachorros estão felizes."))

# 2 - Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.