# IF e ELSE

# idade = int(input("Digite sua idade: "))

# if idade > 30:
#     print("tá com o pé na cova....")
# else:
#     print("Tá com a vida ganha eim")




# nome = input("Digite seu nome: ").upper()

# if nome == "AFONSO":
#     print("presente professor")
# else:
#     print("sai daqui krl")



# a = 1
# b = 1

# if a == 1 and b == 1:
#     print("True")
# else:
#     print("False")


# conectcar = True
# velocidade = 40

# if conectcar and velocidade <= 40:
#     print("A cancela abriu!!")
# else:
#     print("Vc bateu e morreu....")



# moeda = input("Cara ou Coroa? ").upper()

# if moeda == "CARA":
#      print("deu coroa")
# else:
#      print("deu cara")


# a = 1
# b = 0

# if a != b:
#     print("True")
# else:
#     print("False")

conta1 = int(input("Conta 1 tem assinatura? 0: Não / 1: Sim "))
conta2 = int(input("Conta 2 tem assinatura? 0: Não / 1: Sim "))

if conta1 != conta2 or conta1 == 0:
    print("Saque negado")
else:
    print("Saque liberado")
