from collections import defaultdict

# Criando um defaultdict onde o valor padrão é 0
doces_por_pessoa = defaultdict(int)

# Adicionando doces
doces_por_pessoa['Alice'] += 5  # Alice trouxe 5 doces
doces_por_pessoa['Bob'] += 3    # Bob trouxe 3 doces

print(f"Doces da Alice {doces_por_pessoa['Alice']}")  # Saída: 5
print(doces_por_pessoa['Bob'])    # Saída: 3
print(doces_por_pessoa['Charlie'])  # Saída: 0 (Charlie não trouxe doces, mas o defaultdict atribuiu o valor padrão 0 automaticamente)
print(doces_por_pessoa)