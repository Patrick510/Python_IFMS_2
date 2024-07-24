perguntas = [
  {
    'Pergunta': 'Quanto é 2+2',
    'Opções':['1','3','4','5'],
    'Resposta':'4',
  },
  {
    'Pergunta': 'Quanto é 5 x 5',
    'Opções':['25','55','10','51'],
    'Resposta':'25'
  },
  {
    'Pergunta': 'Quanto é 10/2',
    'Opções':['4','5','2','1'],
    'Resposta':'5'
  },
]

# print(perguntas[0]['Pergunta'])
acertos = 0
for pergunta in perguntas:
  print(f'Pergunta: {pergunta["Pergunta"]}')

  for chave, opcao in enumerate(pergunta['Opções']):
    print(f'{chave+1}) {opcao}')
  entry = input(':')

  if entry == pergunta['Resposta']:
    print('Acertou')
    acertos += 1
  else:
    print('Errou')
  
print(f'Você acertou {acertos} perguntas de {len(perguntas)}')
