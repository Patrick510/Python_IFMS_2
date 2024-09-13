import re

def iscpf(string):
  pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
  return re.findall(pattern, string)

# cpf = "Meu cpf é 123.456.789-10."
# print(iscpf(cpf))

def isemail(string):
  pattern = r'\b(\w*)@([a-zA-Z0-9.-]+\.\w*)\b'
  verify = re.findall(pattern, string)
  return verify != []

# email = "example.email@test.com"
# email2 = 'example.error@.com'
# print(isemail(email))
# print(isemail(email2))

def isphone(string):
  pattern = r'\(\d{2}\)\s\d{4}\s\d{4}'
  return re.findall(pattern, string)

# phone = "Meu telefone é (11) 1234 5678."
# print(isphone(phone))

def iswordfive(string):
  pattern = r'\b\w{6,}\b'
  cleaned_string = re.sub(r'\s+', ' ', string).strip()
  
  return re.findall(pattern, cleaned_string)

# texto = "A rápida raposa marrom pula sobre o cachorro preguiçoso."
# print(iswordfive(texto))

# Exercício 4: Validar Códigos Postais
# Descrição: Receber uma string e verificar se ela é um código postal válido no formato XXXXX-XXX, onde X é um dígito. O código postal deve ser exatamente 8 dígitos, com um hífen no meio.

def codepostal(string):
  pattern = r'\b\d{5}-\d{3}\b'
  return re.findall(pattern, string) != []

# postal = "O código postal é 12345-678."
# print(codepostal(postal))

# Exercício 5: Extrair Data no Formato DD/MM/AAAA
# Descrição: Receber uma string e extrair todas as datas no formato DD/MM/AAAA. Considere que o dia deve estar entre 01 e 31, o mês entre 01 e 12 e o ano pode ser qualquer ano de quatro dígitos.

def dateformat(string):
  pattern = r'\b\d{2}/\d{2}/\d{4}\b'
  return re.findall(pattern, string)

texto = "Hoje é 01/01/2021 e amanhã será 02/01/2021."
print(dateformat(texto))