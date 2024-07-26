# set(word, definition): Adiciona ou modifica a definição de uma palavra.
# get(word): Retorna a definição de uma palavra. Se a palavra não existir no dicionário, retorna uma mensagem indicando que a palavra não foi encontrada.
# get_word_order(word): Retorna a ordem em que uma palavra foi adicionada/modificada no dicionário. A ordem deve ser um número inteiro representando a posição da palavra na sequência de adições/modificações.
# get_all_words(): Retorna uma lista com todas as palavras presentes no dicionário, na ordem em que foram adicionadas/modificadas.

from dataclasses import dataclass

@dataclass
class WordDict:
  word: str
  definition: str

dictionary = []

def set_word(word, definition):
  global dictionary
  for i, words in enumerate(dictionary):
    if words.word == word:
      dictionary[i].definition = definition
      return
  dictionary.append(WordDict(word, definition))

def get_word(word):
  result = [words.definition for words in dictionary if words.word == word]
  return  result[0] if result else "Word not found" 

def get_word_order(word):
  for index, words in enumerate(dictionary):
    if words.word == word:
      return index
  return "Word not found"

def get_all_words():
  return [(words.word, words.definition) for words in dictionary]

set_word("Ola", "Saudação")
print(get_word("Ola"))
print(get_word_order("Ola"))
print(get_all_words())


