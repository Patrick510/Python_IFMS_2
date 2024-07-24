"""(25% pontos) Implemente a função contida: Recebe duas strings. Retorna True ou False dependendo 
se a primeira string possui todos os caracteres da segunda string ou não. Deve ser usada a classe set.
Por exemplo, para o seguinte código,
print(contida("abcedario","abcd"))
print(contida("abcedario","abcdef"))
A saída deve ser:
True
False
"""
def contida(palavra,caracter):
  caracter = set(caracter)
  if caracter.issubset(palavra):
    return True
  else:
    return False

print(contida("abcedario","abcd"))
print(contida("abcedario","abcdef"))
