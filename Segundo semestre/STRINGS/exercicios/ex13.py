# Receber uma string e retornar outra string formada pelos dois primeiros e dois últimos caracteres da string lida. Exemplos de entrada/saída: abcdef/abef, abcd/abcd, abc/abc, ab/ab, a/a.

s = str(input())

new_s = s[:2] + s[-2:]
print(new_s)
