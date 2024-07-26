# 1) (25% pontos) Implemente a função combinar_listas: Recebe duas listas. Combina os elementos das 
# duas listas em uma lista de tuplas, onde cada tupla conterá os próximos itens de cada lista. Retorna a lista 
# de tuplas. Caso as listas sejam de tamanhos diferentes, levantar uma exceção. Deve ser usada a função zip.

def combinar_listas(nomes,idades):
  return list(zip(nomes,idades))

nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
lista_combinada = combinar_listas(nomes, idades)
# print(lista_combinada)

# 2) (25% pontos) Implemente a função contida: Recebe duas strings. Retorna True ou False dependendo 
# se a primeira string possui todos os caracteres da segunda string ou não. Deve ser usada a classe set.

def contida(palavra, letras):
  caracter = set(letras)
  if caracter.issubset(palavra):
    return True
  else:
    return False

# print(contida("abcedario","abcd"))
# print(contida("abcedario","abcdef"))

# 3) (50% pontos) Desenvolva um programa que realize as seguintes tarefas:
# 1. Lê o caminho para um arquivo de texto.
# 2. Abre o arquivo especificado e escreve seu conteúdo na tela, enumerando cada linha.
# 3. Lê o número da linha a ser removida do arquivo.
# 4. Remove a linha selecionada do arquivo.
# 5. Salva o arquivo atualizado, agora sem a linha removida.

# Dicas:
# ➢ Utilize a função open para abrir o arquivo.
# ➢ Utilize o método readlines para ler todas as linhas do arquivo.
# ➢ Ao exibir as linhas enumeradas, você pode utilizar um contador para acompanhar o número da linha.
# ➢ Para remover a linha selecionada, você pode utilizar a indexação de lista para acessar as linhas e, em 
# seguida, reescrever o arquivo com as linhas restantes.

def ler_arquivo(caminho):
  with open(caminho, "r+") as arquivo:
    arquivo_lido = arquivo.readlines()
    for numero_linhas, linhas in enumerate(arquivo_lido, start=1):
      print(f"{numero_linhas}: {linhas}")
    linha_remover = int(input())
    arquivo_lido.remove(arquivo_lido[linha_remover - 1])
    
    arquivo.seek(0)
    arquivo.truncate()
    arquivo.writelines(arquivo_lido)

caminho = input()
ler_arquivo(caminho)