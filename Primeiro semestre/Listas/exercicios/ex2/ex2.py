"""Ler um número n, seguido por uma sequência de n números. Escrever os números, sem duplicatas, ordenadamente."""

numeros = set()
entry = int(input(":"))

for entries in range(entry):
  num = int(input(":"))
  numeros.add(num)

numeros_ordenados = sorted(numeros)
print(numeros_ordenados)