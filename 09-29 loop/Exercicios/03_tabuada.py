# Peça um número ao usuário e mostre a tabuada de 1 a 10 usando for.

num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
