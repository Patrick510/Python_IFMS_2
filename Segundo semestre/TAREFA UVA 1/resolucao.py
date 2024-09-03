import sys

def palingrama(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    odd_chars = [char for char, count in freq.items() if count % 2 != 0]
    to_add = ''.join(sorted(odd_chars))
    
    return to_add

input = sys.stdin.read()
data = input.strip().split('\n')

results = []

for line in data:
  if line == "#":
    break
  results.append(palingrama(line))
  results.append("\n")
  
  for result in results:
    print(result)