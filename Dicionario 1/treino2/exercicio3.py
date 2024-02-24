from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass
class Eleicao:
  candidato: str
  chapa: int
  voto: int

add_dict = defaultdict(list)
total_votos = 0

def set_candidato(candidato,chapa,voto):
  add_dict[candidato].append(Eleicao(candidato,chapa,voto))

def get(candidato):
  return [(entry.candidato, entry.voto) for entry in add_dict[candidato]]

def get_all_votos():
  return [(entry.candidato, entry.voto) for entries in add_dict.values() for entry in entries]

def get_all_candidatos():
  return [(entry.candidato, entry.chapa, entry.voto) for entries in add_dict.values() for entry in entries]

def cadastrar_voto(chapa):
  global total_votos
  for entries in add_dict.values():
    for entry in entries:
      if entry.chapa == chapa:
        entry.voto += 1
        total_votos += 1
      else:
        total_votos += 1

def verificar_empate(candidatos_empate):
  vencedor_empate = min(candidatos_empate)
  print(f"{vencedor_empate} ganhou")

def verificar_segundo_turno(candidato_segundo_tunro):
  for candidato in candidato_segundo_tunro:
    print(candidato)
  print("SEGUNDO TURNO")

def calcular_voto():
  global total_votos
  votos = get_all_votos()
  
  if total_votos == 0:
    print("Nenhum voto foi cadastrado")

  contagem_votos = Counter({candidato: voto for candidato, voto in votos}).most_common(2)
  
  if len(contagem_votos) == 1:
    candidato, qtd_votos = contagem_votos[0]
    percent_votos = qtd_votos / total_votos
    
    if percent_votos > 0.5:
      print(f"{candidato} Ganhou")
    else:
      print(f"{candidato} Perdeu")
  elif len(contagem_votos) > 1:
    mais_votado, qtd_votos1 = contagem_votos[0]
    segundo_mais_votado, qtd_votos2 = contagem_votos[1]
    percent_votos = qtd_votos1 / total_votos

    print(contagem_votos)

    if qtd_votos1 == qtd_votos2:
      candidatos_empate = (mais_votado,segundo_mais_votado)
      verificar_empate(candidatos_empate)
    elif percent_votos > 0.5:
      print(f"{mais_votado} Ganhou")
    else:
        candidatos_segundo_turno = (mais_votado, segundo_mais_votado)
        verificar_segundo_turno(candidatos_segundo_turno)

set_candidato("Fulano", 14, 0)
set_candidato("Beltrano", 42, 0)
set_candidato("Siclano", 20, 0)

cadastrar_voto(5)
cadastrar_voto(20)
cadastrar_voto(14)
cadastrar_voto(0)
cadastrar_voto(42)
cadastrar_voto(20)

calcular_voto()

# print(get("Fulano"))
# print(get_all_candidatos())
