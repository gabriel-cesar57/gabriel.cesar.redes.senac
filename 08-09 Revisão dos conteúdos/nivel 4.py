#Crie um programa que coleta dados de 2 pessoas (nome e idade) e armazena cada pessoa como um dicionário em uma lista. Mostre a lista ao final.

#variaveis
nome1 = input('Digite o nome da primeira pessoa: ')
idade1 = int(input('Digite a idade da primeira pessoa: '))

nome2 = input('Digite o nome da segunda pessoa: ')
idade2 = int(input('Digite a idade da segunda pessoa: '))

#listas
pessoa1 = {
    'nome' : nome1,
    'idade' : idade1
}

pessoa2 = {
    'nome' : nome2,
    'idade' : idade2
}

#mostrar a lista
lista_pessoas = []
lista_pessoas.append(pessoa1)
lista_pessoas.append(pessoa2)
print(lista_pessoas)

