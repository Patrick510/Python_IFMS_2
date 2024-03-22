"""Lista permitida. Ler um número n, seguido por n palavras "permitidas". Depois, ler um número m, seguido por m frases, uma em cada linha. Para cada frase, escrever "PERMITIDO" ou "CENSURADO" caso contenha apenas palavras permitidas ou não."""

def verifica_permitido(permitido, frase):
    palvaras_frase = set(frase.split())

    if palvaras_frase.issubset(permitido):
        return "PERMITIDO"
    else:
        return "CENSURADO"

permitida = "hoje"
frase = "hoje fui na feira"

print(verifica_permitido(permitida.lower().split(), frase.lower()))