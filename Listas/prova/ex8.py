"""Um anagrama é uma palavra ou frase formada reorganizando as letras de outra palavra ou frase, usando todas as letras originais exatamente uma vez. Em outras palavras, as palavras ou frases são anagramas se tiverem as mesmas letras, mas em ordens diferentes. Exemplos de anagramas: "amor" e "roma"; "listen" e "silent"; "ator" e "rota".
Ler um número n seguido por n pares de palavras, e, para cada par, escrever "S" ou "N" caso sejam anagramas ou não."""

def is_anagrama(palavra1,palavra2):
    set_palavra1 = set(palavra1)
    set_palavra2 = set(palavra2)
    
    if set_palavra1.issubset(set_palavra2):
        return "S"
    else:
        return "N"

palavra1 = "amor"
palavra2 = "roma"

palavra3 = "listen"
palavra4 = "silent"

print(is_anagrama(palavra1,palavra2))
print(is_anagrama(palavra3,palavra4))
