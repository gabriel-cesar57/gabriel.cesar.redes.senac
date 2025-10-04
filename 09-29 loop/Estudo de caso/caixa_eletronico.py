# Você foi contratado para programar o sistema de saque de um caixa eletrônico. O sistema deve funcionar enquanto o cliente não escolher sair e enquanto houver saldo suficiente na conta.

saldo = 1000
while True:
    print("\nBem-vindo ao banco tabajara:")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == '1':
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    
    elif opcao == '2':
        valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
        if valor_saque > saldo:
            print("Saldo insuficiente para este saque.")
        else:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")
    
    elif opcao == '3':
        valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        print(f"Novo saldo: R$ {saldo:.2f}")
    
    elif opcao == '4':
        print("Obrigado por usar o caixa eletrônico. Até nunca!")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")