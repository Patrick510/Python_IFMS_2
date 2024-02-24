from collections import defaultdict
from dataclasses import dataclass
from datetime import date

@dataclass
class Empresa:
  code: str
  date: date
  closing_price: float

add_dict = defaultdict(list)

def add(code,date,closing_price):
  add_dict[code].append(Empresa(code,date,closing_price))

def get_prices(code):
  return [(entry.date, entry.closing_price) for entry in add_dict[code]]

def get_all_stocks():
  return [(entry.code) for entries in add_dict.values() for entry in entries]

def average_price(code):
  return sum([entry.closing_price for entry in add_dict[code]])/ len(get_prices(code))

def recent_prices(code, date):
  return [entry.closing_price for entry in add_dict.get(code,[]) if entry.date == date]

add("Google",date(2024,9,6), 250.00)
add("Google",date(2022,3,5), 150.00)
add("Google",date(2023,1,3), 550.00)
add("Google",date(2019,7,1), 850.00)
add("Samsung",date(2022,7,1), 850.00)
add("Samsung",date(2020,7,1), 850.00)

print(get_prices("Google"))

print(get_all_stocks())

print(average_price("Google"))

print(recent_prices("Google",date(2020,7,1)))

