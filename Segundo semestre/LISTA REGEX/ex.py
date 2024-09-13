import re

# 1 - Na língua portuguesa, palavras no plural terminam com “s”. Receber uma string e retornar uma lista com as palavras que terminam com “s”.

def ex1(string):
    pattern = r'\b\w+s\b'
    return re.findall(pattern, string)

#print(ex1("Os gatos e cachorros estão felizes."))

# 2 - Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.

def ex2(string):
    pattern = r'\b\w*(\w)\1\w*\b'
    words = set(match.group(0) for match in re.finditer(pattern, string))
    return words

#print(ex2("Os gatos e cachorros estão correndo felizes"))

# 3 - Receber uma string com várias linhas e retornar uma lista com todas as datas no formato dd/mm/aaaa.

def ex3(string):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, string)

#print(ex3("Hoje é 01/01/2021 e amanhã será 02/01/2021."))

# 4 - Receber uma string e retornar True caso seja um horário no formato “HH:MM” válido, ou False caso contrário. Usar apenas uma expressão regular que faça a validação completa.

def ex4(string):
    pattern = r'\b(0[0-9]|1[1-2]):[0-5][0-9]\b'
    return re.findall(pattern, string) != []

print(ex4("O horário é 12:00."))