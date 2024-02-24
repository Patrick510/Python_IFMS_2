from collections import defaultdict
from dataclasses import dataclass
from datetime import date

@dataclass
class Acoes:
  code: str
  data: date
  closing_price: float

add_dict = defaultdict(list)

def add(code,date,closing_price):
  add_dict[code].append(Acoes(code,date,closing_price))

def get_prices(code):
  return [(entry.data, entry.closing_price) for entry in add_dict[code]]

def get_all_stocks():
  return [(entry.code, entry.data, entry.closing_price) for entries in add_dict.values() for entry in entries]

def average_prices(code):
  media = sum([entry.closing_price for entry in add_dict[code]])/len(get_prices(code))
  return media

def recent_prices(code,date):
  return [entry.closing_price for entry in add_dict.get(code,[]) if entry.data > date]

add("Google", date(2020,8,4), 130.0)
add("Google", date(2018,9,4), 150.0)
add("Google", date(2016,4,4), 189.0)
add("Netflix", date(2019,7,3), 180.0)

# print(get_prices("Google"))
print(get_all_stocks())
mediaGoogle = average_prices("Google")
print(f"{mediaGoogle:.2f}")
print(recent_prices("Google",date(2016,4,4)))
