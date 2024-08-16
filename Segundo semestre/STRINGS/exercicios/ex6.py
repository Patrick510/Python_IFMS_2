# Receber uma frase. Retorná-la na notação CamelCase.

frase = "hoje eu comi pao com ovo"
camel_case = frase.title().replace(" ","")
camel_case = camel_case[:1].lower() + camel_case[1:]

print(camel_case)