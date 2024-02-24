from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Dicionario:
  word: str
  definition: str

add_dict = defaultdict(list)
word_order = []

def set(word, definition):
  add_dict[word].append(Dicionario(word,definition))
  if word not in word_order:
    word_order.append(word)

def get(word):
  return [entry.definition for entry in add_dict[word]]

def get_order_word(word):
  if word in word_order:
    return word_order.index(word)+1
  else:
    return None

def get_all_words():
  return [(entry.word, entry.definition) for entries in add_dict.values() for entry in entries]

set("Oi",("Saudação","Comprimento"))
set("Não",("Negar","Oposição"))
set("Sim",("Concordar","Afirmar"))
print(get("Oi"))
print(get_order_word("Oi"))
print(get_all_words())
