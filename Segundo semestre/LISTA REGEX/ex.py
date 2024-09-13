import re

# 1 - Na língua portuguesa, palavras no plural terminam com “s”. Receber uma string e retornar uma lista com as palavras que terminam com “s”.

#print(ex1("Os gatos e cachorros estão felizes."))

# 2 - Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.

#print(ex2("Os gatos e cachorros estão correndo felizes"))

# 3 - Receber uma string com várias linhas e retornar uma lista com todas as datas no formato dd/mm/aaaa.

#print(ex3("Hoje é 01/01/2021 e amanhã será 02/01/2021."))

# 4 - Receber uma string e retornar True caso seja um horário no formato “HH:MM” válido, ou False caso contrário. Usar apenas uma expressão regular que faça a validação completa.

#print(ex4("O horário é 12:00."))

# 5 - Receber uma string, que representa uma URL, e retornar um dicionário com as variáveis e seus valores extraídos da URL, ambas como string. Por exemplo, para a URL https://www.exemplo.com/produto?id=123&nome=produto1&categoria=eletronicos, a função deve retornar o dicionário {"id":"123", "nome":"produto1", "categoria":"eletronicos"}.

#print(ex5("https://www.exemplo.com/produto?id=123&nome=produto1&categoria=eletronicos"))

# 6 - Receber uma string contendo informações sobre filmes e retornar uma lista apenas com os títulos dos filmes produzidos antes de 1990. Exemplo, para a string:
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

#print(ex6("1 The Shawshank Redemption (1994) 2 The Godfather (1972) 3 The Godfather: Part II (1974) 4 Pulp Fiction (1994) 5 The Good, the Bad and the Ugly (1966) 6 The Dark Knight (2008) 7 12 Angry Men (1957) 8 Schindler's List (1993) 9 The Lord of the Rings: The Return of the King (2003) 10 Fight Club (1999)"))

# 7 - Receber uma string e retornar outra string deixando apenas dois dígitos após a casa decimal de cada número com ponto flutuante. Exemplo, para a string:
# 1 Euro = 1.351299 US Dollar
# British Pound = 1.614873 US Dollar
# Australian Dollar = 0.916063 US Dollar
# Retornar a string:

# 1 Euro = 1.35 US Dollar
# British Pound = 1.61 US Dollar
# Australian Dollar = 0.91 US Dollar

#print(ex7("1 Euro = 1.351299 US Dollar British Pound = 1.614873 US Dollar Australian Dollar = 0.916063 US Dollar"))

# 8 - Receber uma lista de strings representando URLs e retornar uma lista apenas com os hostnames das URLs de protocolo HTTPS. Exemplo, para a lista:
# ['https://www.google.com?q=regexp', 'http://example.com', 'https://pedrosiqueira.github.io/ifmsjs/alg/']
# Retornar a lista:

# ['google.com', 'pedrosiqueira.github.io']

#print(ex8(['https://www.google.com?q=regexp', 'http://example.com', 'https://pedrosiqueira.github.io/ifmsjs/alg/']))

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

#print(ex9("Cartola - Corra e Olhe o Céu (0:00) Chico Buarque - Construção (3:25) Elis Regina & Adoniran Barbosa - Tiro ao álvaro (9:47) Cartola - Corra e Olhe o Céu (13:12)"))

# 10 - Python f-strings começam com f antes das aspas, e variáveis dentro da string ficam entre chaves. Javascript template strings são similares, mas não começam com f, as aspas são trocadas por acentos graves, e antes das chaves há um cifrão. Receber uma string que contenha uma f-string do Python (não esquecer de escapar os devidos caracteres), e retornar a string no formato template string do Javascript. Exemplo, para a seguinte string:
# f"{msg}, {nome}!"
# Retornar a string:

# `${msg}, ${nome}!`

#print(ex10('f"{msg}, {nome}!"'))