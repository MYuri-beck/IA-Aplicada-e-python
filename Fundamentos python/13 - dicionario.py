filmIception = {
    "title" : "Inception",  
    "yearRelease": 2010,
    "imbRating" : 8.8,
    "genre" : ["Sci-fi", "Action", "Thriller"]
}
print(filmIception)
print(len(filmIception))
print(type(filmIception))

# 1 - recuperar um elemento do dicionario
print(filmIception["genre"])
print(filmIception.get("genre"))

# 2 - buscar apenas as chaves do dicionario
print(filmIception.keys())

# 3 - buscar apenas os valores do dicionario
print(filmIception.values())

# 4 - bhuscar itens do dicionario com chave e valor
print(filmIception.items())

# 5 - adicionar itens ao dicionario
filmIception["diretor"] = "Crhistopher Nolan"
print(filmIception)

# 6 - artualizar itens no dicionario
filmIception.update({"imdbRating": 8.7})
print(filmIception)

# 7 - remover item do dicionario
filmIception.pop("director")