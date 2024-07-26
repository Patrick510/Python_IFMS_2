list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8]
list1[0] = "PC"
# print(list1)
# print()

set1 = set(["Computer", "Printer", "TV","Camera", 89, 30.8])
# print(set1)
# print()

dict1 = {
  1:["Computer", "Printer", "TV","Camera", 89, 30.8],
  2:["Computer2", "Printer2", "TV2","Camera2", 892, 30.82],
  3:["Nothing"]
}
dict1[1][3] = "None"
dict1[1].remove("None")
del dict1[3]

tuple1 = [
  ("Computer", "Printer", "TV", "Camera", 89, 30.8),
  ("Computer2", "Printer2", "TV2","Camera2", 892, 30.82),
  ("Nothing")
]

#Retirando apenas o elemento "TV da tupla"
new_tuple1 = tuple(item for item in tuple1[0] if item != "TV")

new_tuple1 = [new_tuple1, tuple1[1], tuple1[2]]

#Retirando uma lista inteira
new_tuple1 = tuple(item for item in tuple1 if item != tuple1[0])

#Remover qualquer tupla que contenha "Nothing"
new_tuple1 = tuple(item for item in tuple1 if "Nothing" not in item)

tuple2 = [
  ("Computer", "Printer", "TV", "Camera", 89, 30.8),
  ("Computer2", "Printer2", "TV2","Camera2", 892, 30.82),
  ("Nothing")
]

new_tuple2 = tuple(item for item in tuple1[0] if item != "TV")
tuple2 = [new_tuple2, tuple2[1], tuple2[2]]
print("Após remover 'TV' da primeira sub-tupla")
print(tuple2)

print()

tuple2 = [item for item in tuple2 if item != tuple2[0]]
print("Após remover a primeira sub-tupla inteira")
print(tuple2)
print()

tuple2 = [item for item in tuple2 if "Nothing" not in item]
print("Após remover qualquer sub-tupla que contenha 'Nothing'")
print(tuple2)


new_list = ["NewItem1", "NewItem2", "NewItem3"]
tuple2.append(new_list)
print("Após adicionar a lista como nova sub-tupla")
print(tuple2)


def ler_documento(caminho):
  with open(caminho, "r") as arquivo:
    return arquivo.read()

def escrever_documento(caminho):
  with open(caminho, "w") as arquivo:
    arquivo.write("Tem coisa agora")

caminho = input()
conteudo = ler_documento(caminho)
# conteudo = escrever_documento(caminho)
# print(conteudo)


