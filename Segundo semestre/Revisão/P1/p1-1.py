# 1) adicionar_livro: recebe uma tupla com os dados do livro como argumento e o insere na lista.
# 2) excluir_livro: recebe o título e o nome do autor como argumentos e exclui da lista o livro 
# correspondente.
# 3) consultar_livros_por_autor: recebe o nome de um autor como argumento e retorna uma lista 
# contendo os títulos dos livros desse autor. Se o autor não tiver nenhum livro na biblioteca, a função deve 
# retornar uma lista vazia.
# 4) livros_publicados_no_ano: recebe um ano como argumento e retorna uma lista contendo os títulos 
# dos livros publicados nesse ano.
# 5) calcular_media_paginas: calcula e retorna a média do número de páginas de todos os livros na 
# biblioteca.
# 6) livros_maiores_que: recebe um número de páginas como argumento e retorna uma lista de tuplas 
# composta pelo título e o número de páginas dos livros que têm mais páginas que o argumento.

from dataclasses import dataclass

@dataclass
class Book:
  title:str
  author:str
  year:int
  number_pages:int

library = []

def add_book(title, author, year, number_pages):
  global library
  library.append(Book(title,author,year,number_pages))

def delete_book(title, author):
  return [books for books in library if books.title != title or books.author != author]

def find_books_author(author):
  return [books for books in library if books.author == author]  

def books_publish_year(year):
  return [books.title for books in library if books.year == year]

def average_number_pages():
  pages = sum([books.number_pages for books in library])
  return pages/len(library)

def books_better_then(number_page):
  return [(books.title, books.number_pages) for books in library if books.number_pages > number_page]

add_book("Python for Beginners", "John Smith", 2020, 300)
add_book("Data Science Essentials", "Jane Doe", 2019, 450)
add_book("Artificial Intelligence in Practice", "Alice Williams", 2020, 300)
add_book("Literary Classics", "Jane Doe", 2017, 500)

print(find_books_author("Jane Doe"))
print(books_publish_year(2020))
print(average_number_pages())
print(books_better_then(300))

# biblioteca = [
#     ("Python for Beginners", "John Smith", 2020, 300),
#     ("Data Science Essentials", "Jane Doe", 2019, 450),
#     ("History of Science", "Robert Johnson", 2018, 250),
#     ("Artificial Intelligence in Practice", "Alice Williams", 2021, 380),
#     ("Literary Classics", "David Brown", 2017, 500)
# ]