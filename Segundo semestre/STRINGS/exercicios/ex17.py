# Um palíndromo é uma sequência de caracteres que se lê da mesma forma que de trás para frente, como ARARA, REVIVER ou OGALOAMAOLAGO. Dada uma string, ela é palíndroma?.

s = input()

if s == s[::-1]:
  print("Sim")