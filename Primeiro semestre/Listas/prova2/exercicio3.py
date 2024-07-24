"""(50% pontos) Desenvolva um programa que realize as seguintes tarefas:
1. Lê o caminho para um arquivo de texto.
2. Abre o arquivo especificado e escreve seu conteúdo na tela, enumerando cada linha.
3. Lê o número da linha a ser removida do arquivo.
4. Remove a linha selecionada do arquivo.
5. Salva o arquivo atualizado, agora sem a linha removida.
Dicas:
➢ Utilize a função open para abrir o arquivo.
➢ Utilize o método readlines para ler todas as linhas do arquivo.
➢ Ao exibir as linhas enumeradas, você pode utilizar um contador para acompanhar o número da linha.
➢ Para remover a linha selecionada, você pode utilizar a indexação de lista para acessar as linhas e, em 
seguida, reescrever o arquivo com as linhas restantes.
"""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    return palavras

def salva_arquivo(arquivo_editar):
  nome_arquivo = input("Digite o nome do arquivo: ")
  with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(arquivo_editar)
    print("Arquivo salvo")
    arquivo.close()

def deleta_linha(nome_arquivo, linha):
  tamanho = len(nome_arquivo)
  for qtd in range(tamanho):
    if qtd != linha:
      del(nome_arquivo[linha])
    return nome_arquivo

def recebe_palavras(arquivo):
  palavras_arquivo = ""
  for qtd in range(len(arquivo)):
    palavras_arquivo += arquivo[qtd]+" "
  return palavras_arquivo

def mostra_arquivo(arquivo):
  for qtd in range(len(arquivo)):
    print(f'{qtd} {arquivo[qtd]}')

arquivos = []

entry = input()
arquivos.append(ler_arquivo(entry))

mostra_arquivo(arquivos[0])

print("Deletando linha do arquivo")
print()
deleta_linha(arquivos[0], 2)
mostra_arquivo(arquivos[0])

print("Salvando arquivo alterado")
print()
palavras_arquivo = recebe_palavras(arquivos[0])
print(palavras_arquivo)
salva_arquivo(palavras_arquivo)
