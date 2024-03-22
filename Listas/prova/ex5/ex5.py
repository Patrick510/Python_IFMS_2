"""Ler dois arquivos de texto diferentes. Escrever as palavras presentes em pelo menos um dos arquivos, sem duplicatas."""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    return set(palavras)

def verifica_palavras(arquivo1,arquivo2):
  return arquivo1.union(arquivo2)

arquivos = []

for entries in range(2):
  entry = input()
  arquivos.append(ler_arquivo(entry))

palavras_presentes = verifica_palavras(arquivos[0], arquivos[1])

for palavra in palavras_presentes:
  print(palavra)