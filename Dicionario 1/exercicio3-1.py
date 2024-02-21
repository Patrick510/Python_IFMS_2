from collections import Counter
import os

add_dict = {}

def set(candidato, chapa, votos=0):
  if candidato not in add_dict:
    add_dict[candidato] = [{"candidato":candidato,"chapa":chapa,"votos":votos}]
  else:
    add_dict[candidato].append({"candidato":candidato,"chapa":chapa,"votos":votos})

def cadastrar_voto(chapa):
  chapa_encontrada = False
  for indice, candidato in add_dict.items():
    for entry in candidato:
      if entry["chapa"] == chapa:
        entry["votos"] += 1
        print("Voto cadastrado")
        chapa_encontrada = True
        return
  if not chapa_encontrada:
    print("Chapa não encontrada")

def get_all_votos():
  votos = [(entry["candidato"], entry["votos"]) for candidato in add_dict.values() for entry in candidato]
  return votos

def get_all_candidatos():
  candidatos = [(entry["candidato"], entry["chapa"]) for candidato in add_dict.values() for entry in candidato]
  return candidatos

def get_all_candidatos_():
  candidatos = [(entry["candidato"], entry["chapa"], entry["votos"]) for candidato in add_dict.values() for entry in candidato]
  return candidatos

def verificar_empate(mais_votado):
  candidatos_em_empate = [candidato for candidato, eleicoes in add_dict.items() if any(entry["voto"] == mais_votado[1] for entry in eleicoes)]
  vencedor_empate = min(candidatos_em_empate)
  print(f"Empate! O candidato vencedor por ordem alfabética é {vencedor_empate}.")

def realizar_segundo_turno(candidatos_segundo_turno):
  print("SEGUNDO TURNO")
  print("Candidatos no segundo turno: \n")
  for candidato in candidatos_segundo_turno:
    print(candidato)

  for candidato in candidatos_segundo_turno:
    nome, votos = candidato
    print(f"{nome} | VOTOS: {votos}")

def calcular_votos():
  votos = list(get_all_votos())
  total_votos = len(votos)
  
  if total_votos == 0:
    print("Nenhum voto cadastrado")
    return

  contagem_votos = Counter(votos).most_common()

  if len(contagem_votos) == 1:
    candidato, votos_candidato = contagem_votos[0]
    percentual_mais_votado = votos_candidato / total_votos

    if percentual_mais_votado > 0.5:
      print(f"O candidato {candidato} teve mais que 50%")
    else:
      print("Nenhum candidato recebeu mais que 50%")
  elif len(contagem_votos) == 2:
    mais_votado, segundo_mais_votado = contagem_votos
    percentual_mais_votado = mais_votado[1] / total_votos

    if percentual_mais_votado > 0.5:
      print(f"O candidato {mais_votado[0]} teve mais que 50%")
    else:
      candidatos_em_segundo_turno = [mais_votado[0], segundo_mais_votado[0]]
      realizar_segundo_turno(candidatos_em_segundo_turno)
  else:
    verificar_empate(contagem_votos)

try:
  entry = int(input("Quantos candidatos são? \n:"))

  for qtd in range(entry):
    chapa_cand = int(input("Chapa:"))
    nome_cand = input("Nome:")
    voto = 0

    set(nome_cand, chapa_cand, voto)

  while True:
      try:
        print(get_all_candidatos())
        voto = input("(PARA SAIR DIGITE [S])\nQual seu voto\n:")
        if voto.lower() == 's':
          calcular_votos()
          break
        print(voto)
        voto = int(voto)
        cadastrar_voto(voto)
      except ValueError:
        print("Por favor, insira um número válido para o voto.")
except (TypeError, ValueError):
  print("Valor inválido, digite apenas números")