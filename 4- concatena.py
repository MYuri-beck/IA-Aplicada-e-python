#Usando do Input

name = input("Figite o nome do filme: ")
yearLaunch = int(input("Digite o ano de lancamento do filme: "))
noteMovie = float(input("Digite a nota do filme: "))

print("Dados do filme")
print("=====================")

#alternativa1
print("Nome do filme", name)
print("Ano de lancamento", yearLaunch)
print("Nota do filme", noteMovie)

#alternativa 2
print("Nome do filme: ", name, "\nAno de lancamento: ", yearLaunch, "\nNota do filme: ", noteMovie)

#alternativa 3
print (f"nome do filme: {name}\n"
       f"Ano de lancaento: {yearLaunch} \n"
       f"Nota do filme: {noteMovie} \n")