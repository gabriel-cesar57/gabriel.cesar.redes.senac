############### calculadora


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))


print('Operações')
print('1: Adição')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')

operacao = input('Escolha uma operação: ')

if (operacao == '1'):
    print('Resultado: ')
    print(num1 + num2)

elif (operacao == '2'):
    print('Resultado: ')
    print(num1 - num2)

elif (operacao == '3'):
    print('Resultado: ')
    print (num1 * num2)

elif (operacao == '4'):
    if (num2 != 0):
        print('Resultado: ')
        print(num1 / num2)
    else:
        print('Erro, náo é possível dividir por zero :P')

else:
    print('Erro, números invalidos')