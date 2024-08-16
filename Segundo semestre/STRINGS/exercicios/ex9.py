# Receber uma string s e dois índices i e j. Remover os caracteres entre i fechado e j aberto. Retornar a string resultante. Exemplo de entrada/saída: "abcdefghij" 4 8/abcdij".

string = str(input())
i,j = map(int,input().split())

print(string[:i]+string[j:])