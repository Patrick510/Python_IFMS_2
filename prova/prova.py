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
    livro_bd[titulo] = (Livro(titulo, autor, ano, numero_paginas))

def excluir_livro(titulo, autor):
    if titulo in livro_bd and livro_bd[titulo] is not None and livro_bd[titulo].autor == autor:
        del livro_bd[titulo]
    else:
        return None

def consultar_livros_por_autor(autor):
    return [entry.titulo for entry in livro_bd.values() if entry.autor == autor]

def livros_publicados_no_ano(ano):
    return [entry.titulo for entry in livro_bd.values() if entry.ano == ano]

def calcular_media_paginas():
    total_paginas = sum(entry.numero_paginas for entry in livro_bd.values() if entry is not None)
    return total_paginas / len(livro_bd)

def livros_maiores_que(numero_paginas):
    livros_maior_que = []
    for entry in livro_bd.values():
        if entry is not None and entry.numero_paginas > numero_paginas:
            livros_maior_que.append((entry.titulo, entry.numero_paginas))
    return livros_maior_que

def get_livro(titulo):
    return livro_bd.get(titulo, None)

adicionar_livro("History of Science", "Robert Johnson", 2018, 250)
adicionar_livro("Python for Begginers", "John Smith", 2018, 300)

print(consultar_livros_por_autor("John Smith"))
print(livros_publicados_no_ano(2018))
print(calcular_media_paginas())
print(livros_maiores_que(250))