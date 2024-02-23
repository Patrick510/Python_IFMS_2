from collections import defaultdict, Counter
from dataclasses import dataclass
import os

@dataclass
class Eleicao:
  candidato: str
  chapa: int
  voto: int

add_dict = defaultdict(list)

def set(candidato,chapa, voto):
  add_dict[candidato].append(Eleicao(candidato, chapa, voto))

def get():
  return [(entry.candidato, entry.voto) for candidato in add_dict.values() for entry in candidato]

def get_candidato(candidato):
  return [(entry.candidato, entry.chapa, entry.voto) for entry in add_dict[candidato]]

def get_all_candidatos():
  candidato = [(entry.candidato, entry.chapa) for candidato in add_dict.values() for entry in candidato]
  return candidato

def cadastrar_voto(chapa):
    updated_entries = [entry for candidato in add_dict.values() for entry in candidato if entry.chapa == chapa]

    for entry in updated_entries:
        entry.voto += 1
    print("Voto cadastrado")

def verificar_empate(mais_votado):
  candidatos_em_empate = [candidato for candidato, eleicoes in add_dict.items() if any(entry.voto ==mais_votado for entry in eleicoes)]
  vencedor_empate = min(candidatos_em_empate)
  print(f"Empate! O candidato vencedor por ordem alfabética é {vencedor_empate}.")

def realizar_segundo_turno(candidatos_em_segundo_turno):
  print("SEGUNDO TURNO!")
  print("Candidatos no segundo turno:")
  for candidato in candidatos_em_segundo_turno:
    print(candidato)

def calcular_votos():
  votos = get()
  total_votos = len(votos)

  if total_votos == 0:
    print("Não houve votos ainda.")
    return

  mais_votado, segundo_mais_votado = Counter(votos).most_common(2)

  percentual_mais_votado = mais_votado[1] / total_votos

  if percentual_mais_votado >= 0.5:
    vencedor = mais_votado[0]
    print(f"O candidato {vencedor} teve mais de 50% dos votos.")
  elif percentual_mais_votado < 0.5:
    candidatos_em_segundo_turno = [mais_votado[0], segundo_mais_votado[0]]
    realizar_segundo_turno(candidatos_em_segundo_turno)
  else:
    verificar_empate(mais_votado)

set("Fulano", 14, 0)
set("Beltrano", 20, 0)
set("Cicrano", 42, 0)

cadastrar_voto(3)
cadastrar_voto(14)
cadastrar_voto(42)
cadastrar_voto(20)
cadastrar_voto(5)
cadastrar_voto(20)
cadastrar_voto(14)
cadastrar_voto(0)
cadastrar_voto(42)
cadastrar_voto(20)

votos = list(get())
candidato1 = get_candidato("Fulano")
print(candidato1)

print("")
print(votos)

calcular_votos()
print(votos)

# entry = "S"
# while entry == "S":
#   print("Nome / Chapa")
#   print(get_all_candidatos())
  
#   print("\n Qual seu voto? \n")
#   cadastrar_voto(input(":"))

#   entry = input("\n Terminou? [S]Sim [N]Não \n:").upper()
#   os.system("cls")

#   if entry == "N":
#     calcular_votos()
#     break
#   else:
#     calcular_votos()