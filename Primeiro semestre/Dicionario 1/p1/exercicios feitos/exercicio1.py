from collections import defaultdict
from datetime import date
from dataclasses import dataclass

@dataclass
class Add:
    code: int  # Código
    data: date  # Data
    preco_final: float  # Preço de fechamento

add_dict = defaultdict(list)

def add(code, data, preco_final):
  add_dict[code].append(Add(code, data, preco_final))

def get_prices(code):
  return [(add.data, add.preco_final) for add in add_dict[code]]

def average_price(code):
  return sum([add.preco_final for add in add_dict[code]])/len([add.preco_final for add in add_dict[code]])

def get_all_stocks():
  return list(add_dict.keys()) 

def recent_prices(code, data):
  prices = []
  
  for add in add_dict.get(code,[]):
    if add.data > data:
      prices.append(add.preco_final)

  return prices

add(1, date(2022, 9, 1), 125.0)
add(1, date(2020, 9, 7), 130.0)
add(2, date(2021, 4, 1), 150.0)
add(3, date(2020, 7, 1), 175.0)

prices_for_code_1 = get_prices(1)
print(f"Precos e datas do codigo 1: {prices_for_code_1}")

all_stocks = get_all_stocks()
print(f"Todos os codigos: {all_stocks}")

average = average_price(1)
print(f"Media dos precos do codigo 1: {average}")

recent = recent_prices(1, date(2020,9,7))
print(recent)
