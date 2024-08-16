# Receber duas strings. Concatenar a segunda na primeira apenas se a primeira não terminar com a segunda string. Retornar a string resultante.

string1 = str(input())
string2 = str(input())

if not string1.endswith(string2):
  string2 = string1 + string2
  print(string2)