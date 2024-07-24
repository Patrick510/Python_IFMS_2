"""Ler dois arquivos de texto diferentes. Escrever as palavras presentes em ambos os arquivos, sem duplicatas.
"""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    return set(palavras)

def verifica_comum(palavras1, palavras2):
  palavras_em_comum = set()
  for palavra in palavras1:
    if palavra in palavras2:
      palavras_em_comum.add(palavra)
  return palavras_em_comum

def palavras_em_comum(arquivo1, arquivo2):
  palavras_arquivo1 = ler_arquivo(arquivo1)
  palavras_arquivo2 = ler_arquivo(arquivo2)
  palavras_comuns = verifica_comum(palavras_arquivo1, palavras_arquivo2)
  return palavras_comuns

arquivos = []

for entry in range(2):
  arquivo = f"./{input(f'Digite o nome do {entry+1}° arquivo: ')}.txt"
  arquivos.append(arquivo)

palavras_comuns = palavras_em_comum(arquivos[0], arquivos[1])

print("Palavras comuns aos dois arquivos:")
for palavra in palavras_comuns:
    print(palavra)