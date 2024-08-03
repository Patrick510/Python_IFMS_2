def ler_arquivos(caminho1,caminho2):
    with open(caminho1, "r") as arquivo1:
        conteudo = list(arquivo1.readlines())
        palavras = []
        for palavra in conteudo:
            for indice in palavra:
                if(indice != " " and indice != "\n"):
                    palavras.append(indice)
        
    with open(caminho2, "r") as arquivo2:
        conteudo2 = list(arquivo2.readlines())
        palavras2 = []
        for palavra in conteudo2:
            for indice in palavra:
                if(indice != " " and indice != "\n"):
                    palavras2.append(indice)

    if len(palavras) > len(palavras2):
        print("Arquivo 1 tem maior número de palavras")
    else:
        print("Arquivo 2 tem maior número de palavras")

arquivo1 = input()
arquivo2 = input()

ler_arquivos(arquivo1, arquivo2)