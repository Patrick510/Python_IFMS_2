# 1 - Receber uma string. Retorná-la de trás para frente.
def ex1():  
  s = input()
  print(s[::-1])

# 2 - Dada uma string, ela é composta apenas por dígitos?
def ex2():
  s = input()
  print(s.isdigit())

# 3 - Dada uma frase, quantas letras ela possui?
def ex3():
  frase = input()
  print(len(frase.replace(" ","")))

# 4 - Dada uma frase, quais são as iniciais de cada palavra?
def ex4():
  frase = input()
  for letra in frase.split():
    print(letra[:1])

# 5 - Receber uma string s e dois caracteres x e y. Substituir as ocorrências de x por y na string s. Retornar a string resultante.
def ex5():
  s = input()
  x,y = input().split()
  print(s.replace(x,y))

# 6 - Receber uma frase. Retorná-la na notação CamelCase.
def ex6():
  frase = input()
  camel_case = frase.title().replace(" ","")
  camel_case = camel_case[:1].lower() + camel_case[1:]
  print(camel_case)

# 7 - Receber duas strings. Concatenar a segunda na primeira apenas se a primeira não terminar com a segunda string. Retornar a string resultante.
def ex7():
  s1 = str(input())
  s2 = str(input())
  
  if not s1.endswith(s2):
    s2 = s1+s2
    print(s2)

# 8 - Receber uma frase e retornar sua maior palavra.
def ex8():
  frase = input()
  maior = ""

  for palavra in frase.split():
    if len(palavra) > len(maior):
      maior = palavra

  print(maior)

# 9 - Receber uma string s e dois índices i e j. Remover os caracteres entre i fechado e j aberto. Retornar a string resultante. Exemplo de entrada/saída: "abcdefghij" 4 8/abcdij".
def ex9():
  s = input()
  i,j = map(int, input().split())
  
  print(s[:i]+s[j:])

# 10 - Receber duas strings. Remover cada caractere na segunda string da primeira string. Exemplo de entrada/saída: "The quick brown fox jumps over the lazy dog." "aeiou"/"Th qck brwn fx jmps vr th lzy dg."
def ex10():
  s1 = str(input())
  s2 = str(input())
  for letra in s2:
    if letra in s1:
      s1 = s1.replace(letra, "")
  print(s1)

# 11 - Receber uma string s e quatro índices i, j, k e l. Trocar as substring [i,j) e [k,l). Retornar a string resultante. Exemplo de entrada/saída: abcdefghijklmnopqrstuvwxyz 3 6 10 16/abcklmnopghijdefqrstuvwxyz.
def ex11():
  s = input()
  i,j,k,l = map(int, input().split())
  sub1 = s[i:j]
  sub2 = s[k:l]
  
  new_s = s[:i] + sub2 + s[j:k] + sub1 + s[l:]
  print(new_s)

# 12 - Receber uma string s, um índice i e outra string r. Adicionar a string r no índice i da string s. Retornar a string resultante.
def ex12():
  s = str(input())
  i = int(input())
  r = str(input())
  new_s = s[:i] + r + s[i:]

  print(new_s)

# 13 - Receber uma string e retornar outra string formada pelos dois primeiros e dois últimos caracteres da string lida. Exemplos de entrada/saída: abcdef/abef, abcd/abcd, abc/abc, ab/ab, a/a.
def ex13():
  s = input()
  if len(s) < 4:
    print(s)
  else:
    print(s[:2]+s[-2:])

# 14 - Receber uma string e retorná-la com as palavras invertidas. Exemplos de entrada/saída: "uma frase"/"frase uma", "programar é muito legal"/"legal muito é programar".
def ex14():
  s = input()
  s = s.split()
  new_s = " ".join(s[::-1])
  print(new_s)

# 15 - Dadas duas strings, elas possuem a mesma sequência de vogais, desconsiderando outros caracteres? Por exemplo, litoral, e picotar possuem a mesma sequência de vogais "ioa".
def ex15():
  s1 = str(input())
  s2 = str(input())

  def extrair_vogal(texto):
    vogais = "aeiouAEIOU"
    return ' '.join([letra for letra in texto if letra in vogais])

  if extrair_vogal(s1) == extrair_vogal(s2):
    print("Sim")

# 16 - Dadas duas strings, quantas vezes uma está contida na outra? Exemplo, "ANA" ocorre 4 vezes em "ANA E MARIANA GOSTAM DE BANANA"
def ex16():
  s1 = input()
  s2 = input()
  
  def contando_ocorrencias(sub, s):
    count = start = 0
    while True:
      start = s.find(sub, start)
      if start == -1:
        return count
      count += 1
      start += 1
  print(contando_ocorrencias(s1,s2))

ex16()

# 17 - Um palíndromo é uma sequência de caracteres que se lê da mesma forma que de trás para frente, como ARARA, REVIVER ou OGALOAMAOLAGO. Dada uma string, ela é palíndroma?.
def ex17():
  pass

# 1 - A Cifra de César é uma das técnicas de criptografia mais simples e conhecidas. Ela consiste em substituir cada letra de um texto pela n-ésima letra do alfabeto após ela, sendo n um número inteiro, chamado de chave de encriptação. Por exemplo, para n=5, o texto "Rex" se torna "Wjc". Dada a chave e o texto, qual o texto encriptado?