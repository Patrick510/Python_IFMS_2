import re

# 1 - Na língua portuguesa, palavras no plural terminam com “s”. Receber uma string e retornar uma lista com as palavras que terminam com “s”.

def ex1(string):
  pattern = r'\b[\w\'`]+s\b'
  return re.findall(pattern, string)

# texto = "Os gatos e cachorros estão felizes."
# print(ex1(texto))

# 2 - Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.

def ex2(string):
  pattern = r'\b\w*(\w)\1\w*\b'

  words_with_repeats = set(match.group(0) for match in re.finditer(pattern, string))

  return list(words_with_repeats)

# texto = "Os gatos e cachorros estão correndo estão felizes."
# print(ex2(texto))

# 3 - Receber uma string com várias linhas e retornar uma lista com todas as datas no formato dd/mm/aaaa.

def ex3(string):
  pattern = r'\b\d{2}/\d{2}/\d{4}\b'
  return re.findall(pattern, string)

# texto = "Hoje é 01/01/2021 e amanhã será 02/01/2021."
# print(ex3(texto))

# 4 - Receber uma string e retornar True caso seja um horário no formato “HH:MM” válido, ou False caso contrário. Usar apenas uma expressão regular que faça a validação completa.

def ex4(string):
  pattern = r'\b(0[0-9]|1[0-2]):[0-5][0-9]\b'
  verify = re.findall(pattern, string)
  return verify != []

# texto = "O horário é 12:00."
# print(ex4(texto))

# 5 - Receber uma string, que representa uma URL, e retornar um dicionário com as variáveis e seus valores extraídos da URL, ambas como string. Por exemplo, para a URL https://www.exemplo.com/produto?id=123&nome=produto1&categoria=eletronicos, a função deve retornar o dicionário {"id":"123", "nome":"produto1", "categoria":"eletronicos"}.

def ex5(string):
  pattern = r'(?<=\?|&)(\w+)=(\w+)'
  matches = re.findall(pattern, string)

  return {key: value for key, value in matches}

# url = "https://www.exemplo.com/produto?id=123&nome=produto1&categoria=eletronicos"
# print(ex5(url))

# Receber uma string contendo informações sobre filmes e retornar uma lista apenas com os títulos dos filmes produzidos antes de 1990. Exemplo, para a string:
# 1 The Shawshank Redemption (1994)
# 2 The Godfather (1972)
# 3 The Godfather: Part II (1974)
# 4 Pulp Fiction (1994)
# 5 The Good, the Bad and the Ugly (1966)
# 6 The Dark Knight (2008)
# 7 12 Angry Men (1957)
# 8 Schindler's List (1993)
# 9 The Lord of the Rings: The Return of the King (2003)
# 10 Fight Club (1999)
# Retornar a seguinte lista:

# ['The Godfather', 'The Godfather: Part II', 'The Good, the Bad and the Ugly', '12 Angry Men']

def ex6(string):
  pattern = r'(\d+)\s(.*?)(?:\s\((\d{4})\))'
  matches = re.findall(pattern, string)
  return [title for _, title, year in matches if int(year) < 1990]

# filmes = "1 The Shawshank Redemption (1994) 2 The Godfather (1972) 3 The Godfather: Part II (1974) 4 Pulp Fiction (1994) 5 The Good, the Bad and the Ugly (1966) 6 The Dark Knight (2008) 7 12 Angry Men (1957) 8 Schindler's List (1993) 9 The Lord of the Rings: The Return of the King (2003) 10 Fight Club (1999)"

# print(ex6(filmes))

# 7 - Receber uma string e retornar outra string deixando apenas dois dígitos após a casa decimal de cada número com ponto flutuante. Exemplo, para a string:
# 1 Euro = 1.351299 US Dollar
# British Pound = 1.614873 US Dollar
# Australian Dollar = 0.916063 US Dollar
# Retornar a string:

# 1 Euro = 1.35 US Dollar
# British Pound = 1.61 US Dollar
# Australian Dollar = 0.91 US Dollar

def ex7(string):
  pattern = r'(\d{1}\.\d{2})\d*'
  return re.sub(pattern, r'\1', string)

# moedas = "1 Euro = 1.351299 US Dollar British Pound = 1.614873 US Dollar Australian Dollar = 0.916063 US Dollar"
# print(ex7(moedas))

# 8 - Receber uma lista de strings representando URLs e retornar uma lista apenas com os hostnames das URLs de protocolo HTTPS. Exemplo, para a lista:
# ['https://www.google.com?q=regexp', 'http://example.com', 'https://pedrosiqueira.github.io/ifmsjs/alg/']
# Retornar a lista:

# ['google.com', 'pedrosiqueira.github.io']

def ex8(string):
  pattern = r'https://(?:www\.)?([^/?#]+)'
  matches = []
  for url in string:
    match = re.search(pattern, url)
    if match:
      matches.append(match.group(1))
  return matches

# urls = ['https://www.google.com?q=regexp', 'http://example.com', 'https://pedrosiqueira.github.io/ifmsjs/alg/']
# print(ex8(urls))

# 9 - Receber uma string de várias linhas com o tempo entre parênteses no final da linha e retornar uma string com o tempo no início da linha, sem parênteses. Exemplo, para a string:
# Cartola - Corra e Olhe o Céu (0:00)
# Chico Buarque - Construção (3:25)
# Elis Regina & Adoniran Barbosa - Tiro ao álvaro (9:47)
# Cartola - Corra e Olhe o Céu (13:12)
# Retornar a string:

# 0:00 Cartola - Corra e Olhe o Céu
# 3:25 Chico Buarque - Construção
# 9:47 Elis Regina & Adoniran Barbosa - Tiro ao álvaro
# 13:12 Cartola - Corra e Olhe o Céu

def ex9(string):
  pattern = r'(.+?)\s\((\d+:\d+)\)'
  return re.sub(pattern, r'\2 \1', string)

# musicas = "Cartola - Corra e Olhe o Céu (0:00) Chico Buarque - Construção (3:25) Elis Regina & Adoniran Barbosa - Tiro ao álvaro (9:47) Cartola - Corra e Olhe o Céu (13:12)"
# print(ex9(musicas))

# 10 - Python f-strings começam com f antes das aspas, e variáveis dentro da string ficam entre chaves. Javascript template strings são similares, mas não começam com f, as aspas são trocadas por acentos graves, e antes das chaves há um cifrão. Receber uma string que contenha uma f-string do Python (não esquecer de escapar os devidos caracteres), e retornar a string no formato template string do Javascript. Exemplo, para a seguinte string:
# f"{msg}, {nome}!"
# Retornar a string:

# `${msg}, ${nome}!`

def ex10(string):
  pattern = r'f"(.+?)"'
  return re.sub(pattern, r'`${\1}`', string)

fstring = 'f"{msg}, {nome}!"'
print(ex10(fstring))