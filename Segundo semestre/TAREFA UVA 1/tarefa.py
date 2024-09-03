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

test_cases = [
    "ddc",
    "aaab",
    "a",
    "ab",
    "abc",
    "aabbcc"
]

for case in test_cases:
    result = palingrama(case)
    print(f"Para a string '{case}', o que deve ser adicionado é '{result}'")
