movieName = "Top Gun"

movieDescription = '''Top Gun Maverick, é um filme de aviação e aventura,
muito consagrado na indústria
'''
print(movieName.upper()) #tudo maisculo
print(movieName.lower()) #tudo minusculo
print(movieName.capitalize()) #primeira letra maiscula
print(movieName.title()) #primeira letra maiscula
print(movieName.center(10, '-')) #retona a string centralizada com caracter de preenchimento
print(movieName.find("u")) # retorna indece/posição de x caractere
print(movieName.find("o")) # conta caracteres
print(movieName.replace("Top", "Matrix")) # altera elemento por outro   
print(movieDescription.split(','))