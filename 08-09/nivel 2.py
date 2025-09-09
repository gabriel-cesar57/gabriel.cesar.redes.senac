# # Peça ao usuario dois numeros e armazene os em variaveis, em seguida exiba a soma

# num1 = float(input('Digite o primeiro número: '))
# num2 = float(input('Digite o segundo número: '))

# print(f'A soma dos números {num1} e {num2} é: {num1+num2}')



# # armazenar nome e idade e exibir

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))

# usuario = {
#     "nome" : nome,
#     "idade" : idade
# }

# print(f'O seu nome é: {usuario["nome"]}, e você tem {usuario["idade"]} anos !')


# solicite nome do produto, preço, quantidade e crie um dicionario

# nome_produto = input('Qual o nome do produto? ')
# preco = float(input('Qual o preço do produto? '))
# estoque = int(input('Quantos produtos em estoque? '))

# produtos = {
#     'nome' : nome_produto,
#     'preço' : preco,
#     'estoque' : estoque
# }

# print(produtos)

nome_livro = input('Qual o nome do livro? ')
autor = input('Qual o autor do livro? ')
ano_publicacao = int(input('Qual o ano de publicação? '))
id = int(input('Digite o id do livro: '))

biblioteca = []

# 0
livro1 = {
    'nome do livro' : nome_livro,
    'autor' : autor,
    'ano de publicação' : ano_publicacao
}

# 1
livro2 = {
    'nome do livro' : 'Berserk',
    'autor' : "Kentarou Miura",
    'ano de publicação' : "1989"
}


biblioteca.append(livro1)
biblioteca.append(livro2)

# vai puxar só o autor do livro2 
print(biblioteca[1]['autor'])