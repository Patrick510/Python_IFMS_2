# Receber uma string s e quatro índices i, j, k e l. Trocar as substring [i,j) e [k,l). Retornar a string resultante. Exemplo de entrada/saída: abcdefghijklmnopqrstuvwxyz 3 6 10 16/abcklmnopghijdefqrstuvwxyz.

s = str(input())
i,j,k,l = map(int,input().split())
sub1 = s[i:j]
sub2 = s[k:l]

new_s = s[:i] + sub2 + s[j:k] + sub1 + s[l:]
print(new_s)