def ler_arquivo(caminho, valores):
  with open(caminho, "r") as arquivo:
    conteudo = arquivo.read()
    valor_total = 0

    for letra in list(conteudo):
        if letra in valores:
          valor_total += valores[letra]
    return round(valor_total, 2)

k = int(input())
arquivos = []
valores = {}

for count in range(k):
  letra, valor = map(str ,input().split())
  valores[letra] = float(valor)/100 

m = int(input())

for count in range(m):
  arquivo = input()
  arquivos.append(arquivo)

for arquivo in arquivos:
    print(f"R$ {ler_arquivo(arquivo, valores)}")

