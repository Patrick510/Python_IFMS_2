def ler_arquivo(caminho, valores):
    with open(caminho, "r+") as arquivo:
        conteudo = arquivo.read()
        valor_total = 0

        for letra in list(conteudo):
            if letra != " " and letra != "\n":
                if letra in valores:
                    valor_total += valores[letra]
    return valor_total

k = int(input("Número de letras e valores: "))
arquivos = []
valores = {}

for count in range(k):
    letra, valor = map(str, input("Letra e valor (separados por espaço): ").split())
    valores[letra] = int(valor) / 100 

m = int(input("Número de arquivos: "))

for count in range(m):
    arquivo = input("Nome do arquivo: ")
    arquivos.append(arquivo)

print(ler_arquivo(arquivos[0], valores))
