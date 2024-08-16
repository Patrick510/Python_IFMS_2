# Receber duas strings. Remover cada caractere na segunda string da primeira string. Exemplo de entrada/saída: "The quick brown fox jumps over the lazy dog." "aeiou"/"Th qck brwn fx jmps vr th lzy dg."

string1 = str(input())
string2 = str(input())

for palavra in string1:
  if palavra in string2:
    string1 = string1.replace(palavra,"")

print(string1)