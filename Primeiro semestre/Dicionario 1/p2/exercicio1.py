# Crie uma API que mantém uma lista dos preços de fechamento de várias ações ao longo dos dias. Utilize dicionários, em que as chaves representam o código da ação e os valores são listas de tuplas contendo a data e o preço de fechamento. Implemente os seguintes métodos:

# ```add(code, date, closing_price)```: adiciona informações de preço de fechamento para uma ação específica em uma determinada data. Certifique-se de lidar com casos em que a ação ainda não possui uma entrada no dicionário, usando defaultdict.

# ```get_prices(code)```: Retorna a lista de tuplas contendo a data e o preço de fechamento para uma ação específica.

# ```get_all_stocks()```: Retorna uma lista com todos os códigos de ações presentes no dicionário.

# ```average_price(code)```: Retorna a média dos preços de fechamento de uma ação específica.

# ```recent_prices(code, date)```: Retorna uma lista com os preços de fechamento de uma ação específica a partir da data date.

from collections import defaultdict
from dataclasses import dataclass
from datetime import date

Stock_db = defaultdict(list)

@dataclass
class NewStock:
  code: str
  date: date
  closing_price: float

def add(code: str, stock_data: NewStock):
  Stock_db[code].append(stock_data)

def get_prices(code):
  return Stock_db.get(code, None)

def get_all_stocks():
  return Stock_db.items()

def get_average_price(code):
  prices = [entry.closing_price for entry in Stock_db[code]]
  return sum(prices) / len(prices)

def recent_price(code, date):
  return list((stock.date, stock.closing_price) for stock in get_prices(code) if stock.date >= date)


new_stock1 = NewStock("Google",date(1999,8,26), 275.0)
new_stock2 = NewStock("Google",date(2010,10,20), 200.0)
new_stock3 = NewStock("Google",date(2011,10,20), 150.0)
add("Google", new_stock1)
add("Google", new_stock2)
add("Google", new_stock3)

#print(get_all_stocks())

#print(recent_price("Google",date(1999,8,26)))

print(f"{get_average_price('Google'):.2f}")