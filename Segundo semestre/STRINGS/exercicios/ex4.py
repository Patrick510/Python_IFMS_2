# Dada uma frase, quais são as iniciais de cada palavra?

frase = "hoje comi pao com ovo"

for palavra in frase.split():
  print(palavra[:1])