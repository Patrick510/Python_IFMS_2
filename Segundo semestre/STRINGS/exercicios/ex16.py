# Dadas duas strings, quantas vezes uma está contida na outra? Exemplo, "ANA" ocorre 4 vezes em "ANA E MARIANA GOSTAM DE BANANA"

s1 = input()
s2 = input()

print(s2.count(s1))

def count_occurrences(sub, s):
    count = start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            return count
        count += 1
        start += 1

print(count_occurrences(s1, s2))