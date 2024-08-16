# A Cifra de César é uma das técnicas de criptografia mais simples e conhecidas. Ela consiste em substituir cada letra de um texto pela n-ésima letra do alfabeto após ela, sendo n um número inteiro, chamado de chave de encriptação. Por exemplo, para n=5, o texto "Rex" se torna "Wjc". Dada a chave e o texto, qual o texto encriptado?

alfabeto_minus = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maius = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
texto = str(input())
chave = int(input())

for letra in texto:
  if letra in alfabeto_minus:
    indice = alfabeto_minus.index(letra)
    novo_indice = (indice + chave) % 26
    print(alfabeto_minus[novo_indice], end="")
  elif letra in alfabeto_maius:
    indice = alfabeto_maius.index(letra)
    novo_indice = (indice + chave) % 26
    print(alfabeto_maius[novo_indice], end="")
  else:
    print(letra, end="")


