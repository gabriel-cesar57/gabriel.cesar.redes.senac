# While, for

#contador = 1
#while contador <= 10:
#    print(contador)
#    contador += 1  




# 2.1 A Missão Criar um sistema para controlar uma máquina de café que funciona até os grãos acabarem ou até que o cliente peça para parar.

graos = 10
while graos > 0:
    print("Fazendo café...")
    graos -= 1
    print(f"Grãos restantes: {graos}")
    if graos == 0:
        print("Acabaram os grãos de café!")
        break
    parar = input("Deseja parar? (s/n): ")
    if parar.lower() == 's':
        print("Parando a máquina de café.")
        break