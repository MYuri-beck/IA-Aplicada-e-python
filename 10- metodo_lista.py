filmsList = ["Inception" , "The ShawShank Redemption",
             "The Dark Kgniht", "Pulp Fiction", "Interstellar"]

# 1 - tamanho da lista
print(len(filmsList))

# 2 - recuperar um indice da lista pelo seu nome
print(filmsList.index("Interstellar"))

# 3 - adicionar item no final da lista
filmsList.append("The lord of the Rings")
print(filmsList)

# 4- ordenação da lista
filmsList.sort()
print(filmsList)

# 5 - copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
print(filmsCopy)

# 6 - remover item da lista
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 7 - remove todos os itens da lista
filmsList.clear()
print(filmsList)