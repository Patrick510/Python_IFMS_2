from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int
    numero_paginas: int

livro_bd = defaultdict(list)

def adicionar_livro(titulo, autor, ano, numero_paginas):
    livro_bd[titulo] = Livro(titulo, autor, ano, numero_paginas)
    
def excluir_livro(titulo, autor):
    if titulo in livro_bd: 
        for entry in livro_bd[titulo]:
            if entry.autor == autor:
                livro_bd[titulo].remove(titulo)

def consultar_livros_por_autor(autor):
    return [entry.titulo for entry in livro_bd.values() if entry.autor == autor]

def livros_publicados_no_ano(ano):
    return [entry.titulo for entry in livro_bd.values() if entry.ano >= ano]

def calcular_media_paginas():
    total_paginas = sum([entry.numero_paginas for entries in livro_bd.values() for entry in entries])
    total_livros = sum(len(entry) for entry in livro_bd.values())
    return total_paginas / total_livros

def livros_maiores_que(numero_paginas):
    livros_maior_que = []
    for entries in livro_bd.values():
        for entry in entries:
            if entry.numero_paginas > numero_paginas:
                livros_maior_que.append(entry.titulo, entry.numero_paginas)
        return livros_maior_que
    
def getLivro(titulo):
    return livro_bd.get(titulo, None)

adicionar_livro("History of Science", "Robert Johnson", 2018, 250)
adicionar_livro("Python for Begginers", "John Smith", 2018, 300)

print(consultar_livros_por_autor("John Smith"))
print(livros_publicados_no_ano(2018))
excluir_livro("Python for Begginers", "John Smith")
#print(calcular_media_paginas())
#print(livros_maiores_que())