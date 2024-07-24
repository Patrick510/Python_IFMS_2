"""Ler uma sequência de números, que se encerra com um número repetido. Escrever os números ordenadamente."""
numeros = []

while True:
  entry = int(input(":"))
  if entry in numeros:
    print(sorted(numeros))
    break
  else:
    numeros.append(entry)