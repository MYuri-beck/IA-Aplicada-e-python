import pprint

filmsDict = {
    "inception": {
        "yearRelease": 2010,
        "imbRating" : 8.8,
        "genre" : ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar" : {
        "yearRelease": 2014,
        "imbRating" : 8.6,
        "genre" : ["Sci-fi", "Drama"]
    },
    "the dark knight" : {
        "yearRelease": 2008,
        "imbRating" : 9.0,
        "genre" : ["Action", "Drama", "Crime"]
    }        
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - buscar uma informação dentro de um dicionario aninhado
print(filmsDict["interstellar"]["genre"])

# 2 - adicionar novo item
filmsDict["inception"]["director"] = "Crhistopher Nolan"
print(filmsDict["inception"])

# 3 - excluir um dicionario
del filmsDict["the dark knight"]
pp.pprint(filmsDict)