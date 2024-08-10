# Leitura das palavras a serem ignoradas
palavras_ignoradas = set()
titulos = []

while True:
    palavra = input().strip().lower()
    if palavra == "::":
        break
    palavras_ignoradas.add(palavra)

while True:
    titulo = input().strip().lower().split()
    if titulo == "sair":
        break
    titulos.append(titulo)
# Processamento dos títulos para gerar o índice KWIC
kwic_index = []

for titulo in titulos:
    palavras = titulo.split()
    for i, palavra in enumerate(palavras):
        if palavra not in palavras_ignoradas:
            # Cria uma nova versão do título com a palavra-chave em maiúsculas
            palavras_kwic = palavras[:]
            palavras_kwic[i] = palavra.upper()
            kwic_index.append(" ".join(palavras_kwic))

# Ordenar o índice KWIC por ordem alfabética das palavras-chave
kwic_index.sort(key=lambda s: s.lower())

# Exibir o índice KWIC
for linha in kwic_index:
    print(linha)
