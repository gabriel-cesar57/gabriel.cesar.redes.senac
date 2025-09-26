# Validador de senhas

senha = input("Digite uma senha: ")

if len(senha) < 8:
    print("Senha muito curta, digite no minimo 8 caracteres.")
else:
    print("Senha válida.")

    