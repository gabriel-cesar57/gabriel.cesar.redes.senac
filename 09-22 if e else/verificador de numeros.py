#   Verificador se é par ou impar

try:
    numero = int(input("Digite um numero: "))
except ValueError:
    print("Erro, digite um número válido.")
    exit()

if numero % 2 == 0:
    print("O numero é par")

else:
    print("O numero é impar")

