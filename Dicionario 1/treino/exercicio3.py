from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass
class Eleicao:
  candidato: str
  chapa: int
  voto: int = 0
  total_votos = 0
    
  add_dict = defaultdict(list)

  def add_candidato(self, candidato, chapa, voto):
    self.add_dict[candidato].append(Eleicao(candidato, chapa, voto))

  def get(self):
    return [(entry.candidato, entry.chapa, entry.voto) for entries in self.add_dict.values() for entry in entries]
  
  def get_votos(self):
    return [(entry.candidato, entry.voto) for entries in self.add_dict.values() for entry in entries]
  
  def cadastrar_voto(self,chapa):
    for entries in self.add_dict.values():
      for entry in entries:
        if entry.chapa == chapa:
          self.total_votos += 1
          entry.voto += 1
          break
        else:
          self.total_votos += 1
  
  def verificar_empate(self, candidatos_empate):
    print(candidatos_empate)
    vencedor_empate = min(candidatos_empate)
    print(f"EMPATE! O RESULTADO DECIDIDO POR ORDEM ALFABETICA\n {vencedor_empate} ganhou")

  def verifica_segundo_turno(self, candidatos_segundo_turno):
    for candidato in candidatos_segundo_turno:
      print(candidato)
    print("SEGUNDO TURNO")
    
  def calcular_voto(self):
    votos = self.get_votos()
    
    print(votos)
    if self.total_votos == 0:
      print("Não houve votos")
    
    contagem_votos = Counter({entry.candidato: entry.voto for entries in self.add_dict.values() for entry in entries}).most_common(2)
    
    if len(contagem_votos) == 1:
      candidato, qtd_votos = contagem_votos[0]
      porcent_votos = qtd_votos / self.total_votos
      
      if porcent_votos > 0.5:
        print(f"O único candidato {candidato} ganhou com mais de 50% dos votos")
      else:
        print(f"O único candidato {candidato} perdeu com mais de 50% dos votos")
    elif len(contagem_votos) > 1:
      mais_votado, qtd_votos_1 = contagem_votos[0]
      segundo_mais_votado, qtd_votos_2 = contagem_votos[1]
      percent_mais_votado = qtd_votos_1 / self.total_votos
      
      if qtd_votos_1 == qtd_votos_2:
        candidatos_empate = (mais_votado,segundo_mais_votado)
        self.verificar_empate(candidatos_empate)
      elif percent_mais_votado > 0.5:
        print(f"O candidato {mais_votado} ganhou com mais de 50% dos votos")
      else:
        candidato_segundo_turno = (mais_votado, segundo_mais_votado)
        self.verifica_segundo_turno(candidato_segundo_turno)

eleicao_ = Eleicao("",0,0)

eleicao_.add_candidato("Fulano", 14, 0)
eleicao_.add_candidato("Beltrano", 42, 0)
eleicao_.add_candidato("Sicrano", 20, 0)

eleicao_.cadastrar_voto(5)
eleicao_.cadastrar_voto(20)
eleicao_.cadastrar_voto(14)
eleicao_.cadastrar_voto(0)
eleicao_.cadastrar_voto(42)
eleicao_.cadastrar_voto(20)

eleicao_.calcular_voto()

try:
  entrada = int(input(":"))
  
  eleicao_instance = Eleicao('', 0, 0)
  
  for entry in range(entrada):
    chapa = int(input(":"))
    nome = str(input(":"))
    
    eleicao_instance.add_candidato(nome,chapa,0)
  
  while True:
    voto_entry = input("[S]Sair:")
    
    if voto_entry != "S":
      voto = int(voto_entry)
      eleicao_instance.cadastrar_voto(voto)
    else:
      print(eleicao_instance.get())
      eleicao_instance.calcular_voto()
      break
  
except (ValueError,TypeError):
  print("Valores inválidos")