# Ex1: 
primeiroNome = input("Dgitite o nome: ")
segundoNome = input("Digite o sobrenome: ")

nomeFormatado = f"{segundoNome} {primeiroNome}"
print(nomeFormatado)

# Ex2: 
texto = "Python é muito interessante"
palavras = texto.split()
textInvertido = " ".join(palavras[::-1])
print(textInvertido)

# Ex3:
texto1 = "arara"
texto2 = "python"

text1_format = texto1.lower().replace(" ","")
text2_format = texto2.lower().replace(" ","")

palindromo1 = text1_format == texto1[::-1]
palindromo2 = text2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)