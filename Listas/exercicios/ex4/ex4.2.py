class Arquivos:
  def __init__(self, arquivo1, arquivo2):
    self.arquivo1 = arquivo1
    self.arquivo2 = arquivo2

  def ler_arquivo(self, nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
      conteudo = arquivo.read()
      palavras = conteudo.split()
      return set(palavras)

  def palavras_em_comum(self):
    palavras_arquivo1 = self.ler_arquivo(self.arquivo1)
    palavras_arquivo2 = self.ler_arquivo(self.arquivo2)
    palavras_comuns = palavras_arquivo1.intersection(palavras_arquivo2)
    return palavras_comuns

arquivos = []

for entry in range(2):
  arquivo = f"{input(f'Digite o nome do {entry+1}° arquivo: ')}.txt"
  arquivos.append(arquivo)

arquivos_compara = Arquivos(arquivos[0], arquivos[1])

palavras_comuns = arquivos_compara.palavras_em_comum()

print("Palavras comuns aos dois arquivos:")
for palavra in palavras_comuns: 
    print(palavra)