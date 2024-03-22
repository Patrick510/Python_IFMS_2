"""Lista proibida. Ler um número n, seguido por n palavras "proibidas". Depois, ler um número m, seguido por m frases, uma em cada linha. Para cada frase, escrever "PERMITIDO" ou "CENSURADO" caso haja palavras proibidas ou não."""

def verificar_censura(proibidas, frase):
    palavras_frase = set(frase.split())
    print(palavras_frase)
    if palavras_frase.intersection(proibidas):
        return "CENSURADO"
    else:
        return "PERMITIDO"


proibida = "hoje"
frase = "hoje fui na feira"

print(verificar_censura(proibida.lower().split(), frase.lower()))