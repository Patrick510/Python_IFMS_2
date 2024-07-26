def combinar_listas(nomes, idades):
  return list(zip(nomes, idades))

nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
lista_combinada = combinar_listas(nomes, idades)
# print(lista_combinada) # [('Ana', 25), ('João', 30), ('Maria', 28)]

# Exercicio 2
def contida(palavra, letras):
  caracter = set(letras)
  if caracter.issubset(palavra):
    return True

# print(contida("abcedario","abcd"))
# print(contida("abcedario","abcdef"))

# Exercicio 3
# 1. Lê o caminho para um arquivo de texto.
# 2. Abre o arquivo especificado e escreve seu conteúdo na tela, enumerando cada linha.
# 3. Lê o número da linha a ser removida do arquivo.
# 4. Remove a linha selecionada do arquivo.
# 5. Salva o arquivo atualizado, agora sem a linha removida.

# Tem coisa escrita no arquivo agora
# Aqui tambem tem coisa

def ler_documento(caminho):
  with open(caminho, "r+") as arquivo:
    linhas = arquivo.readlines()
    for numero_linha, linha in enumerate(linhas, start=1):
      print(f"{numero_linha}: {linha}", end="")
    
    linha_remover = int(input())
    linhas.remove(linhas[linha_remover - 1])  
    
    arquivo.seek(0)
    arquivo.truncate()
    arquivo.writelines(linhas)

caminho = input()
ler_documento(caminho)


