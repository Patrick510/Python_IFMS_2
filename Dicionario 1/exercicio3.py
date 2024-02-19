from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Eleicao:
  candidato: str
  chapa: int
  voto: int

add_dict = defaultdict(list)

def set(candidato,chapa, voto):
  add_dict[candidato].append(Eleicao(candidato, chapa, voto))

def get(candidato):
  return [(entry.candidato, entry.chapa, entry.voto) for entry in add_dict[candidato]]

def cadastrar_voto(chapa):
  if chapa is not None:
    for candidato, eleicoes in add_dict.items():
      for entry in eleicoes:
        if entry.chapa == chapa:
          entry.voto += 1
          print("Voto cadastrado")
          return
  else:
    print("Chapa não encontrada")

def calcular_votos():
  pass

set("Fulano", 14, 0)
set("Sicrano", 42 ,0)
set("Beltrano", 20 ,0)

print("Nome/ Chapa/ Qtd Votos")
candidato1 = get("Fulano")
print(candidato1)

cadastrar_voto(14)
cadastrar_voto(0)

candidato1 = get("Fulano")
print(candidato1)