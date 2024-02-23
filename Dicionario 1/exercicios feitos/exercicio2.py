from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Dicionario:
  word: str
  definition: str

add_dict = defaultdict(list) 
word_order = []

def set(word,definition):
  add_dict[word].append(Dicionario(word,definition))
  if word not in word_order:
    word_order.append(word)

def get(word):
  return [(entry.word, entry.definition) for entry in add_dict[word]]

def get_word_order(word):
  if word in word_order:
    return word_order.index(word) + 1
  else:
    return None

def get_all_words():
  return word_order

set("Oi", ("Saudacao","Comprimento verbal"))
set("Adeus", ("Despedida","Saindo"))

palavra1 = get("Oi")
print(palavra1)

order = get_word_order("Adeus")
print(f"Ordem da palavra Adeus: {order}")

todas_as_palavras = get_all_words()
print(f"Todas as palavras no dicionario: {todas_as_palavras}")