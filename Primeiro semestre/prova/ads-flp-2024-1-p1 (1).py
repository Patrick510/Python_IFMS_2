def anexo():
    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        simbolo1, _, menor_preco1, maior_preco1 = acao1
        simbolo2, _, menor_preco2, maior_preco2 = acao2

        variacao_percentual1 = calcular_variacao_percentual(menor_preco1, maior_preco1)
        variacao_percentual2 = calcular_variacao_percentual(menor_preco2, maior_preco2)

        if variacao_percentual1 > variacao_percentual2:
            return simbolo1, variacao_percentual1
        else:
            return simbolo2, variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return simbolo, atual, menor, maior

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print("Ação com a maior variação percentual:", resultado[0])
    print("Variação percentual da ação:", resultado[1])

def ex1():
    from collections import namedtuple

    Acao = namedtuple('Acao', ['simbolo', 'atual', 'menor', 'maior'])

    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        variacao_percentual1 = calcular_variacao_percentual(acao1.menor, acao1.maior)
        variacao_percentual2 = calcular_variacao_percentual(acao2.menor, acao2.maior)

        if variacao_percentual1 > variacao_percentual2:
            return acao1.simbolo, variacao_percentual1
        else:
            return acao2.simbolo, variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return Acao(simbolo=simbolo, atual=atual, menor=menor, maior=maior)

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print(f"Ação com a maior variação percentual: {resultado[0]}")
    print(f"Média do valor da ação com a maior variação percentual: {resultado[1]}")

def ex2():
    from dataclasses import make_dataclass

    # Criando a classe de dados para representar uma ação
    Acao = make_dataclass("Acao", [("simbolo", str), ("atual", float), ("menor", float), ("maior", float)])

    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        variacao_percentual1 = calcular_variacao_percentual(acao1.menor, acao1.maior)
        variacao_percentual2 = calcular_variacao_percentual(acao2.menor, acao2.maior)

        if variacao_percentual1 > variacao_percentual2:
            return acao1.simbolo, variacao_percentual1
        else:
            return acao2.simbolo, variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return Acao(simbolo=simbolo, atual=atual, menor=menor, maior=maior)

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print(f"Ação com a maior variação percentual: {resultado[0]}")
    print(f"Média do valor da ação com a maior variação percentual: {resultado[1]}")

def ex3():
    from dataclasses import dataclass

    # Decorando a classe Acao com @dataclass
    @dataclass
    class Acao:
        simbolo: str
        atual: float
        menor: float
        maior: float

    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        variacao_percentual1 = calcular_variacao_percentual(acao1.menor, acao1.maior)
        variacao_percentual2 = calcular_variacao_percentual(acao2.menor, acao2.maior)

        if variacao_percentual1 > variacao_percentual2:
            return acao1.simbolo, variacao_percentual1
        else:
            return acao2.simbolo, variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return Acao(simbolo,atual,menor,maior)

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print(f"Ação com a maior variação percentual: {resultado[0]}")
    print(f"Média do valor da ação com a maior variação percentual: {resultado[1]}")

def ex4():
    def calcular_variacao_percentual(menor, maior):
        if menor > maior:
            menor, maior = maior, menor
        return maior / menor - 1

    def obter_acao_com_maior_variacao_percentual(acao1, acao2):
        variacao_percentual1 = calcular_variacao_percentual(acao1['menor'], acao1['maior'])
        variacao_percentual2 = calcular_variacao_percentual(acao2['menor'], acao2['maior'])

        if variacao_percentual1 > variacao_percentual2:
            return acao1['simbolo'], variacao_percentual1
        else:
            return acao2['simbolo'], variacao_percentual2

    def ler_acao():
        simbolo = input("Digite o símbolo da ação: ")
        atual = float(input("Digite o preço atual da ação: "))
        menor = float(input("Digite o menor preço da ação: "))
        maior = float(input("Digite o maior preço da ação: "))
        return {'simbolo': simbolo, 'atual': atual, 'menor': menor, 'maior': maior}

    print("\n# Ação 1")
    acao1 = ler_acao()

    print("\n# Ação 2")
    acao2 = ler_acao()

    resultado = obter_acao_com_maior_variacao_percentual(acao1, acao2)

    print(f"Ação com a maior variação percentual: {resultado[0]}")
    print(f"Média do valor da ação com a maior variação percentual: {resultado[1]}")