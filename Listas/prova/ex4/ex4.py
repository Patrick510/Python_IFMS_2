"""Ler dois arquivos de texto diferentes. Escrever as palavras presentes em ambos os arquivos, sem duplicatas.
"""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    return set(palavras)

def palavras_em_comum(arquivo1, arquivo2):
  return arquivo1.intersection(arquivo2)

arquivos = []

for entries in range(2):
  entry = input()
  arquivos.append(ler_arquivo(entry))

palavras_comuns = palavras_em_comum(arquivos[0], arquivos[1])

for palavra in palavras_comuns:
    print(palavra)