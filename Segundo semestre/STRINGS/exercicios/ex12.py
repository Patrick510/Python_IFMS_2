# Receber uma string s, um índice i e outra string r. Adicionar a string r no índice i da string s. Retornar a string resultante.

s = str(input())
i = int(input())
r = str(input())

new_s = s[:i] + r + s[i:]
print(new_s)