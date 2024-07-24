"""Ler dois arquivos de texto diferentes. Escrever as palavras presentes em pelo menos um dos arquivos, sem duplicatas."""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    return set(palavras)

def verificar_arquivo(arquivo1, arquivo2):
  palavras_arquivo1 = ler_arquivo(arquivo1)
  palavras_arquivo2 = ler_arquivo(arquivo2)
  palavras_presentes = palavras_arquivo1.union(palavras_arquivo2)
  return palavras_presentes

arquivos = []

for indice in range(2):
  arquivo = f"{str(input(f'Nome {indice+1}° arquivo:'))}.txt"
  arquivos.append(arquivo)

palavras_presentes = set()

palavras = verificar_arquivo(arquivos[0], arquivos[1])

print(palavras)