from collections import defaultdict, Counter
from dataclasses import dataclass
import os

@dataclass
class Eleicao:
    candidato: str
    chapa: int
    voto: int  # Remova o valor padrão 0

add_dict = defaultdict(list)
total_votos = 0

def set(candidato, chapa, voto):
    add_dict[candidato].append(Eleicao(candidato, chapa, voto))

def get():
    return [(entry.candidato, entry.chapa, entry.voto) for entries in add_dict.values() for entry in entries]

def get_votos():
    return [( entry.candidato, entry.voto) for entries in add_dict.values() for entry in entries]

def cadastrar_voto(chapa):
    global total_votos
    for candidato in add_dict.values():
        for entry in candidato:
            if entry.chapa == chapa:
                entry.voto += 1
                total_votos += 1
            else:
                total_votos += 1


def verificar_empate(candidatos_empate):
    vencedor_empate = min(candidatos_empate)
    print(f"EMPATE! O DESEMPATE SERA FEITO POR ORDEM ALFABETICA \nO vencedor foi {vencedor_empate}")

def verificar_segundo_turno(candidatos_turno):
    for candidatos in candidatos_turno:
        print(candidatos)
    print("SEGUNDO TURNO")

def calcular_voto():
    global total_votos
    votos = get_votos()
    
    if total_votos == 0:
        print("Não houve votos")

    contagem_votos = Counter({candidato: voto for candidato, voto in votos}).most_common(2)

    if len(contagem_votos) == 1:
        candidato, qtd_votos = contagem_votos[0]
        percent_mais_votado = qtd_votos / total_votos

        if percent_mais_votado > 0.5:
            print(f"O único candidato, {candidato} ganhou com mais de 50% dos votos")
        else:
            print(f"O único candidato, {candidato} perdeu com menos de 50% dos votos")
    elif len(contagem_votos) > 1:
        mais_votado, qtd_votos = contagem_votos[0]
        segundo_mais_votado, qtd_votos_2 = contagem_votos[1]
        percent_mais_votado = qtd_votos / total_votos

        if qtd_votos == qtd_votos_2:
            candidatos_em_empate = (mais_votado, segundo_mais_votado)
            verificar_empate(candidatos_em_empate)
        elif percent_mais_votado > 0.5:
            print(f"O candidato {mais_votado} ganhou com mais de 50% dos votos")
        else:
            candidatos_segundo_turno = (mais_votado, segundo_mais_votado)
            verificar_segundo_turno(candidatos_segundo_turno)
    else:
        print("Algo deu errado")

try:
    numero_candidatos = int(input(":"))

    for entry in range(numero_candidatos):
        chapa = int(input(":"))
        nome = str(input(":"))
        voto = 0

        set(nome, chapa, voto)
    
    while True:
        entry = input("[S] <- Sair:")
        
        if entry != "S":
            voto_chapa = int(entry)
            cadastrar_voto(voto_chapa)
        else:
            os.system("cls")
            calcular_voto()
            break

except(ValueError, TypeError):
    print("Valores inválidos")

