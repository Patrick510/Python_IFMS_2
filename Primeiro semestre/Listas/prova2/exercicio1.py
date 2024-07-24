"""1) (25% pontos) Implemente a função combinar_listas: Recebe duas listas. Combina os elementos das 
duas listas em uma lista de tuplas, onde cada tupla conterá os próximos itens de cada lista. Retorna a lista 
de tuplas. Caso as listas sejam de tamanhos diferentes, levantar uma exceção. Deve ser usada a função zip.
Por exemplo, para o seguinte código,

nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
lista_combinada = combinar_listas(nomes, idades)
print(lista_combinada)
A saída deve ser:
[('Ana', 25), ('João', 30), ('Maria', 28)]
"""

def combinar_listas(nomes, idades):
  listas = ()
  qtd = len(nomes)
  tudo = set()
  try:
    if len(nomes) == len(idades):
      for _ in range(qtd):
        listas += (nomes[_], idades[_])
        tudo = [listas]
      return tudo
  except Exception:
    print("Listas de tamanhos diferentes")

nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
lista_combinada = combinar_listas(nomes, idades)
print(lista_combinada)