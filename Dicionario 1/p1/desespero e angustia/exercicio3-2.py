from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass
class Eleicao:
  chapa: int
  candidato: str
  voto: int

add_dict = defaultdict(list)

def set(chapa, candidato, voto):
  add_dict[chapa].append(Eleicao(chapa, candidato, voto))

def get(chapa):
  return [(entry.candidato, entry.chapa) for entry in add_dict[chapa]]

def get_all_votos():
  return [(entry.candidato, entry.voto) for entries in add_dict.values() for entry in entries] 

def get_all_votos_bonito():
  for entries in add_dict.values():
    for entry in entries:
      print(f"Candidato: {entry.candidato} | Votos: {entry.voto}")

def cadastra_voto(chapa):
    updated_entries = [entry for candidato in add_dict.values() for entry in candidato if entry.chapa == chapa]

    for entry in updated_entries:
        entry.voto += 1
    print("Voto cadastrado")

def verificar_empate(contagem_votos):
  mais_votado = contagem_votos[0]
  
  candidatos_em_empate = [entry for entry in add_dict[mais_votado[0]] if entry.voto == mais_votado[1]]
  
  vencedor_empate = min(candidatos_em_empate, key=lambda entry: (entry.voto, entry.candidato))
  print(f"EMPATE!! O DESEMPATE SERA FEITO POR ORDEM ALFABETICA \n O vencedor foi: {vencedor_empate.candidato}")

def verificar_segundo_turno(candidato_segundo_turno):
  for candidato in candidato_segundo_turno:
    print(candidato)
  print("SEGUNDO TURNO")

def calcular_voto():
  votos = get_all_votos()
  total_votos = len(votos)
  
  if not total_votos:
    print("Não há votos")
    return
  
  contagem_votos = Counter(votos).most_common(2)
  
  if len(contagem_votos) == 1:
    candidato, qtd_votos = contagem_votos[0]
    porcent_mais_votado = qtd_votos / total_votos
    
    if porcent_mais_votado > 0.5:
      print(f"O candidato |{candidato}| ganhou com |{qtd_votos}| votos")
    else:
      print("Não houve vencedor")
  elif len(contagem_votos) > 2:
    mais_votado, segundo_mais_votado = contagem_votos[0]
    porcent_mais_votado = mais_votado[1] / total_votos
    
    if porcent_mais_votado > 0.5:
      print(f"O candidato |{mais_votado[0]}| ganhou com |{segundo_mais_votado[1]}| votos")
    else:
      candidatos_segundo_turno = (mais_votado[0], segundo_mais_votado[0])
      verificar_segundo_turno(candidatos_segundo_turno)
  else:
    verificar_empate(contagem_votos)

# try:
entry = int(input(":"))
  
for num in range(entry):
  chapa = input(":")
  nome = input(":")
  set(chapa,nome,0)

while True:
  voto = int(input("[-1]Sair :"))

  if voto == -1 or voto < 0:
    calcular_voto()
    get_all_votos_bonito()
    break

  cadastra_voto(voto)
  get_all_votos_bonito()
# except (ValueError, TypeError):
#   print("Valores inválidos ou Digitou algo que não é um número!")

