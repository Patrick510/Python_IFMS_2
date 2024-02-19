from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Pessoa:
  nome: str
  sobrenome: str


add_nome = defaultdict(list)

nome1 = Pessoa('Patrick', 'Dias')

print(nome1)