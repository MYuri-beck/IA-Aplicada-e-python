import random

# 1 - Selecionar valor aleatório de uma lista
list1 = [7, 6,4,3,2,1]
print(random.choice(list1))

# 2- Gerar um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)

# 3 - Seleciona o caractere aleatório de uma string
name = "Curso python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
#random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Olá mundo"
print(random.sample(s, 2))

# 5 - Programa de sorteio
done = False

while not done:
    print("O que você deseja fazer ?")
    print("1. Adivinhar o número")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print("=============== Adivinhe um número de 1 a 10: ===============")
        number = int(input("Digite um numero"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns você acertou")
        else:
            print(f"Tente novamente, o número sorteado foi {result}")
    elif choice == 2:
        done = True
    else:
        print("Opção inválida, Escolha a opção 1 ou 2")