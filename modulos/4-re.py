import re

text = "Udemy - uma plataforma com muitos cursos"
# 1- Índice inicial e final de palacras
# O r significa uma row string (string bruta)
match = re.search(r'muitos cursos', text)
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

# 2- Buscando o índice que possui o ponto
site = 'https://udemy.com'
macth = re.search(r'\.', site)
print(macth)

# 3- Buscando uma lista de caracteres em uma frase
pattern =  "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4- Verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa está suja', "O dia está lindo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# 5- Verificando o final de uma string
rule_end = r'!$'
phrase2 = "Odia está lindo!"
match = re.search(rule_end, phrase2)
print(match)