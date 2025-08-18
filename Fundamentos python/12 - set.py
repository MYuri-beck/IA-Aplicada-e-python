filmSet = {"Inception" , "The ShawShank Redemption",
             "The Dark Kgniht", "Pulp Fiction", "Interstellar"}

# 1 - buscar tamanho do set
print(len(filmSet))

# 2 - true e 1 são considerados os mesmo valor
exempleSet = {"Inception", True, 1 ,8.7}
print(exempleSet)

# 3 - adicionar tem de outro set
filmSet.update(exempleSet)
print(filmSet)

# 4 - remover item de um set
filmSet.remove(True)
filmSet.remove(8.7)
print(filmSet)
