n, m = map(int, input().split())

jack_cds = []
jill_cds = []

for num in range(n):
    jack_cds.append(input())
for num in range(m):
    jill_cds.append(input())

jack = set(jack_cds)
jill = set(jill_cds)

ambos = jack.intersection(jill)

print(len(ambos))