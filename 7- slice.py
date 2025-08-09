movieName = "Top Gun"

# string[inicio:fim] - indice começa na posição 0 / indice final - 1

# 1 - Buscar toda a string a pártit da primeira posição
print(movieName[0:])

# 2 - Busca toda string até a última posição
print(movieName[:7])

# 3 - buscar toda string da terceira até a ultima posição
print(movieName[2:])

'''
string[inicio:fim:passo] 
indice começa na posição 0 / indice final - 1
passo - determina o incremento. Por padrão e o 1
'''

# 4 - buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - buscar toda a string nos indices impares
print(movieName[1::2])

# 6 - inverter uma string de trás para frente
print(movieName[::-1])