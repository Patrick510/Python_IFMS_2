# Primeiros Exercícios

### API de Preços de Ações
Crie uma API que mantém uma lista dos preços de fechamento de várias ações ao longo dos dias. Utilize dicionários, em que as chaves representam o código da ação e os valores são listas de tuplas contendo a data e o preço de fechamento. Implemente os seguintes métodos:

```add(code, date, closing_price)```: adiciona informações de preço de fechamento para uma ação específica em uma determinada data. Certifique-se de lidar com casos em que a ação ainda não possui uma entrada no dicionário, usando defaultdict.

```get_prices(code)```: Retorna a lista de tuplas contendo a data e o preço de fechamento para uma ação específica.

```get_all_stocks()```: Retorna uma lista com todos os códigos de ações presentes no dicionário.

```average_price(code)```: Retorna a média dos preços de fechamento de uma ação específica.

```recent_prices(code, date)```: Retorna uma lista com os preços de fechamento de uma ação específica a partir da data date.

#

###  Dicionário de definição de palavras
Melhore a solução proposta para o problema do dicionário de palavras definido anteriormente. Crie uma API com os seguintes métodos:

```set(word, definition)```: Adiciona ou modifica a definição de uma palavra.

```get(word)```: Retorna a definição de uma palavra. Se a palavra não existir no dicionário, retorna uma mensagem indicando que a palavra não foi encontrada.

```get_word_order(word)```: Retorna a ordem em que uma palavra foi adicionada/modificada no dicionário. A ordem deve ser um número inteiro representando a posição da palavra na sequência de adições/modificações.

```get_all_words()```: Retorna uma lista com todas as palavras presentes no dicionário, na ordem em que foram adicionadas/modificadas.

#

### Sistema de eleições
Crie um programa para gerenciar uma eleição. Primeiramente, será necessário cadastrar os candidatos e associá-los às suas respectivas chapas. Em seguida, o programa deverá ler a lista de votos, onde cada voto é representado pelo número da chapa do candidato votado.

Primeiramente o programa lê a quantidade de candidatos, seguida pelo número da chapa e o nome (única palavra, sem espaços) de cada candidato. Depois o programa lê a quantidade de votos, seguida pelos números das chapas votadas. Caso haja algum número sem chapa cadastrada, considerar como voto nulo. Por fim, o programa deve exibir os dois candidatos mais votados, e a mensagem "SEM SEGUNDO TURNO" ou "COM SEGUNDO TURNO", caso o primeiro candidato tenha conseguido mais de 50% dos votos ou não. Caso haja empate, o critério de desempate é a ordem alfabética. A entrada e saída de dados deve obedecer ao seguinte padrão de exemplo:


### Anotações

```
def get_votos(candidato):
  votos = sum(entry.voto for entry in add_dict[candidato])
  return votos
```

```
  total_votos = len(votos)  # Obtém o total de votos
  votos_candidato = Counter(votos).get(candidato_vencedor, 0)  # Obtém os votos do candidato vencedor

  if total_votos > 0 and (votos_candidato / total_votos) > 0.5:
    print(f"O candidato {candidato_vencedor} teve mais de 50% dos votos.")
  else:
    print(f"O candidato {candidato_vencedor} não teve mais de 50% dos votos.")
```


Aviso de função muito extensa:

```

def calcular_votos():
  votos = get_all_votos()
  total_votos = len(votos) 
  
  if total_votos > 0:
    mais_votado = Counter(votos).most_common(1)[0][0]
    contagem_mais_votado = Counter(votos)[mais_votado]

    # Verifica se houve empate
    empate = contagem_mais_votado > 1

    if not empate:
      for candidato, eleicoes in add_dict.items():
        for entry in eleicoes:
          if entry.voto == mais_votado:
            print(f"O candidato {candidato} teve mais de 50% dos votos.")
          return
    else:
      # Empate, determina o vencedor por ordem alfabética
      candidatos_em_empate = [candidato for candidato, eleicoes in add_dict.items() if any(entry.voto == mais_votado for entry in eleicoes)]
      vencedor_empate = min(candidatos_em_empate)  # Obtém o candidato vencedor por ordem alfabética
      print(f"Empate! O candidato vencedor por ordem alfabética é {vencedor_empate}.")
```