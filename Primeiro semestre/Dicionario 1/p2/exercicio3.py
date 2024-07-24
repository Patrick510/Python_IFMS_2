# Crie um programa para gerenciar uma eleição. Primeiramente, será necessário cadastrar os candidatos e associá-los às suas respectivas chapas. Em seguida, o programa deverá ler a lista de votos, onde cada voto é representado pelo número da chapa do candidato votado.

# Primeiramente o programa lê a quantidade de candidatos, seguida pelo número da chapa e o nome (única palavra, sem espaços) de cada candidato. Depois o programa lê a quantidade de votos, seguida pelos números das chapas votadas. Caso haja algum número sem chapa cadastrada, considerar como voto nulo. Por fim, o programa deve exibir os dois candidatos mais votados, e a mensagem "SEM SEGUNDO TURNO" ou "COM SEGUNDO TURNO", caso o primeiro candidato tenha conseguido mais de 50% dos votos ou não. Caso haja empate, o critério de desempate é a ordem alfabética. A entrada e saída de dados deve obedecer ao seguinte padrão de exemplo:

from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass
class Eleicao:
  chapa: int
  candidato: str
  voto = int(0)

total_votos = 0
candidato_bd = defaultdict(list)

def addcandidato(chapa, candidato):
  candidato_bd[chapa] = Eleicao(chapa, candidato)

def getcandidato(chapa):
  return f"Chapa: {candidato_bd[chapa].chapa} | Candidato:{candidato_bd[chapa].candidato}"

def cadastravoto(chapa):
  global total_votos
  if chapa in candidato_bd: 
    candidato_bd[chapa].voto += 1
    total_votos += 1
  else:
    total_votos += 1
    #print("Chapa não encontrada")

def getcandidatos():
  candidatos = [(entry.candidato, entry.chapa, entry.voto) for entry in candidato_bd.values()]
  for candidato in candidatos:
    print(f"Candidato: {candidato[0]} | Chapa: {candidato[1]} | Voto: {candidato[2]}")

def validaempate(candidatos):
  vencedor = min(candidatos)
  return vencedor[0]

def validasegundoturno(candidatos):
  for candidato in candidatos:
    print(candidato)
  print("SEGUNDO TURNO")

def _getvotos():
  return [(entry.candidato,entry.voto) for entry in candidato_bd.values()]

def calcula_voto():
  global total_votos
  votos = _getvotos()
  
  if votos == 0:
    print("Não houve votos")
  else:
    classificacao = Counter({candidato:voto for candidato,voto in votos}).most_common(3)
    
    if len(classificacao) == 1:
      print(classificacao)
      mais_votado, votos = classificacao[0]
      porcentagem = mais_votado[1] / total_votos

      if porcentagem > 0.5:
        print(f"{mais_votado[0]} ganhou")
      else:
        print(f"{mais_votado[0]} perdeu")
    elif len(classificacao) > 1:
      primeiro, votosprimeiro = classificacao[0]
      segundo, votossegundo = classificacao[1]
      terceiro, votosterceiro = classificacao[2]
      porcentagem_ = votosprimeiro / total_votos

      if votosprimeiro == votossegundo:
        candidatos = (primeiro,segundo)
        validaempate(candidatos)
      elif porcentagem_ > 0.5:
        print(f"O {primeiro} ganhou de {segundo}")
      else:
        if votossegundo == votosterceiro:
          valida = ((segundo,votossegundo),(terceiro,votosterceiro))
          vencedor_empate = validaempate(valida)

          candidatossegundo = (primeiro, vencedor_empate)
          validasegundoturno(candidatossegundo)  
    else:
      print("cabo")

addcandidato(14,"Fulano")
addcandidato(42,"Beltrano")
addcandidato(20,"Sicrano")

cadastravoto(5)
cadastravoto(20)
cadastravoto(14)
cadastravoto(0)
cadastravoto(42)
cadastravoto(20)

getcandidatos()
print()
calcula_voto()