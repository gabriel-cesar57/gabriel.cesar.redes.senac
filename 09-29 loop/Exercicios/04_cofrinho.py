#O Cofrinho Inteligente: peça ao usuário depósitos até que ele digite 0. Ao final, mostre o total acumulado
total = 0
while True:
    deposito = float(input("Digite o valor a ser depositado (ou 0 para sair): "))
    if deposito == 0:
        break
    total += deposito
print(f"Total acumulado no cofrinho: R$ {total:.2f}")
