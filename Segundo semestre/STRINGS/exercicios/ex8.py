# Receber uma frase e retornar sua maior palavra.

frase = "hoje eu comi pao com ovo também"

maior_palavra = ""

for palavra in frase.split():
  if len(palavra)> len(maior_palavra):
    maior_palavra = palavra

print(maior_palavra)
print(max(frase.split(), key=len))