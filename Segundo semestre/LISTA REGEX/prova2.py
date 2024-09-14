import re

# Define a expressão regular para verificar a frase exata
pattern = re.compile(r'^tom hates jerry , jimmy hates tom$')

# Função para processar cada linha
def process_line(line):
    # Verifica se a linha corresponde exatamente ao padrão
    if pattern.match(line):
        return "YES I WILL"
    else:
        return "NO I WON'T"

# Ler a entrada do usuário até uma linha vazia
while True:
    try:
        line = input().strip()  # Remove espaços em branco ao redor
        if line == '':
            break
        print(process_line(line))
    except EOFError:
        break
