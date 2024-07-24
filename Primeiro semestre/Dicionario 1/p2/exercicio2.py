# Melhore a solução proposta para o problema do dicionário de palavras definido anteriormente. Crie uma API com os seguintes métodos:

# ```set(word, definition)```: Adiciona ou modifica a definição de uma palavra.

# ```get(word)```: Retorna a definição de uma palavra. Se a palavra não existir no dicionário, retorna uma mensagem indicando que a palavra não foi encontrada.

# ```get_word_order(word)```: Retorna a ordem em que uma palavra foi adicionada/modificada no dicionário. A ordem deve ser um número inteiro representando a posição da palavra na sequência de adições/modificações.

# ```get_all_words()```: Retorna uma lista com todas as palavras presentes no dicionário, na ordem em que foram adicionadas/modificadas.

from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Dictionary:
  word: str
  definition: str
  order: int

word_counter = 0
dict_bd = defaultdict(list)

def set(word, definition):
    global word_counter
    word_counter += 1

    if word in dict_bd:
        dict_bd[word][0].definition = definition
        dict_bd[word][0].order = word_counter
    else:
        dict_bd[word] = [Dictionary(word, definition, word_counter)]

def get(word):
  return [entry.definition for entry in dict_bd[word]] if word in dict_bd else ["Não existe"]

def get_word_order(word):
  order = [(entry.order, entry.word) for entry in dict_bd[word]]
  return f"Order of change or Addiction:{order[0][0]} Word:{order[0][1]}"

def get_all_words():
  return dict_bd.items()

# Exemplos de uso
set("Ola", ("Saudacao", "Comprimento verbal"))
print(get("Ola"))
print(get_word_order("Ola"))

set("Adeus", ("Comprimento verbal","Saída","Despedida"))
print(get_word_order("Adeus"))

set("Ola", ("Saudacao", "Comprimento verbal", "Entrada"))
print(get_word_order("Ola"))

print(get_all_words())