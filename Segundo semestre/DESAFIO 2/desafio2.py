palavras_ignoradas = set()
titulos = []

while True:
  palavra = input()
  if palavra == "::":    
    while True:
      titulo = input()
      if titulo.strip() == "":
        break
      titulos.append(titulo.strip().lower().split())
    break
  palavras_ignoradas.add(palavra.lower())

kwic_index = []

for titulo in titulos:
  palavras = titulo
  for i, palavra in enumerate(palavras):
    if palavra not in palavras_ignoradas:
      palavras_kwic = palavras[:]
      palavras_kwic[i] = palavra.upper()
      kwic_index.append(" ".join(palavras_kwic))

for linha in sorted(kwic_index):
  print(linha)