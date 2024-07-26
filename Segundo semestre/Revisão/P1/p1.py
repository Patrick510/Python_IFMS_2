# biblioteca = [
#   ("Python for Beginners", "John Smith", 2020, 300),
#   ("Data Science Essentials", "Jane Doe", 2019, 450),
#   ("History of Science", "Robert Johnson", 2018, 250),
#   ("Artificial Intelligence in Practice", "Alice Williams", 2021, 380),
#   ("Literary Classics", "David Brown", 2017, 500)
# ]

from dataclasses import dataclass

@dataclass
class Book:
  title: str
  autor: str
  year: int
  number_pages: int
  
library = []
  
def add_book(title, autor, year, number):
  new_book = Book(title, autor, year, number) 
  library.append(new_book)

def remove_book(title, autor):
  global library
  library = [book for book in library if book.title != title or book.autor != autor]

def search_book_autor(autor):
  return [book for book in library if book.autor == autor]

def books_published_year(year):
  return [books for books in library if books.year == year]

def average_number_pages():
  num_pages = sum(books.number_pages for books in library)
  return num_pages/len(library)

def books_more_then(number_page):
  return [books for books in library if books.number_pages == number_page]

add_book("Python for Beginners", "John Smith", 2020, 380)
add_book("Artificial Intelligence in Practice", "Alice Williams", 2020, 380)
add_book("Artificial Intelligence in Practice 2", "Alice Williams", 2021, 380)
remove_book("Python for Beginners", "John Smith")
print(search_book_autor("John Smith"))
print(books_published_year(2020))
print(average_number_pages())
print(books_more_then(380))