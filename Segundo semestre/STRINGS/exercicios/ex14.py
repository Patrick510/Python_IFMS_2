# Receber uma string e retorná-la com as palavras invertidas. Exemplos de entrada/saída: "uma frase"/"frase uma", "programar é muito legal"/"legal muito é programar".

s = input()
new_s = ' '.join(s.split()[::-1])
print(new_s)