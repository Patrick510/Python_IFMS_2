#Exemplo de entrada Exemplo de saída
#happy purple frog/eating bugs in the marshes/get indigestion
#computer programs/the bugs try to eat my code/i will not let them
#a e i o u/this is seven syllables/a e i o u y
#e/o/i
#SAIDA
#Y
#2
#3

import re

def conta_silabas(linha):
    return len(re.findall(r'[aeiouy]+', linha))

def verifica_haiku(haiku):
    linhas = haiku.split('/')
    contagem_silabas = [conta_silabas(linha) for linha in linhas]
    contagem_correta = [5, 7, 5]
    for i in range(3):
        if contagem_silabas[i] != contagem_correta[i]:
            return str(i+1)
    return "Y"

haiku = []

while True:
    inp = input()
    if inp == "e/o/i":
        break
    haiku.append(inp)

for i in haiku:
    print(verifica_haiku(i))