#O Jogo da Contagem Regressiva: peça um número inicial e faça uma contagem regressiva até 0, mostrando "🚀 Lançar!" no fim.

import time
numero = int(input("Digite um número para iniciar a contagem regressiva: "))
while numero >= 0:
    print(numero)
    time.sleep(1) 
    numero -= 1
print("🚀 Lançar!")
