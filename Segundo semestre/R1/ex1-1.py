def ler_arquivos(caminho1, caminho2):
  with open(caminho1, "r") as arquivo1:
    conteudo1 = arquivo1.read()
    palavras1 = conteudo1.split()
  
  with open(caminho2, "r") as arquivo2:
    conteudo2 = arquivo2.read()
    palavras2 = conteudo2.split()

  if len(palavras1) > len(palavras2):
    print("Arquivo 1 tem maior número de palavras")
  else:
    print("Arquivo 2 tem maior número de páginas")

arquivo1 = input()
arquivo2 = input()

ler_arquivos(arquivo1, arquivo2)