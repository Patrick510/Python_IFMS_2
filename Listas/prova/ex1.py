"""Ler uma sequência de números, que se encerra com um número repetido. Escrever os números ordenadamente."""

numeros = set()

while True:
  try:
    entry = int(input(""))
    if entry in numeros:
      print(numeros)
      break
    numeros.add(entry)
  except Exception:
    print("Valor inválido")