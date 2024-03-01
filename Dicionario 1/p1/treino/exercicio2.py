from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Dicionario:
  word: str
  definition: str

add_dict = defaultdict(list)
word_order = []

def set(word,definition):
  add_dict[word].append(Dicionario(word, definition))
  if word not in word_order:
    word_order.append(word)

def get(word):
  word_ = [entry.definition for entry in add_dict.setdefault(word, [])] 
  if not word_:
        return f"{word} não encontrada"
  return word_

def get_word_order(word):
  if word in word_order:
    return word_order.index(word) + 1
  else:
    return None

def get_all_words():
  return [(word, index+1) for index, word in enumerate(word_order)]

set("Olá", ("Saudação", "Comprimento Verbal"))

print(get("Olá"))
print(get("Python"))

set("Python", ("Linguagem de Programação", "Oirentada á Objetos"))

print(get_all_words())

print(f"Palavra {get('Olá')} foi a {get_word_order('Olá')}ª ser adicionada")