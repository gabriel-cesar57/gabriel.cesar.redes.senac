# pedra, papel, tesoura

import random

escolhas = ['pedra', 'papel', 'tesoura']
computador = random.choice(escolhas)

jogador = input("Escolha pedra, papel ou tesoura: ").lower()


while jogador not in escolhas:
    jogador = input("Escolha inválida. Escolha pedra, papel ou tesoura: ").lower()
print(f"Computador escolheu: {computador}")


if jogador == computador:
    print("Empate!")

elif (jogador == 'pedra' and computador == 'tesoura') or \
     (jogador == 'papel' and computador == 'pedra') or \
     (jogador == 'tesoura' and computador == 'papel'):
    print("Você ganhou!")

else:
    print("Computador ganhou!")
