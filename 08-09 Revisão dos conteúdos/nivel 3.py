# # armazenar nome, idade e cidade e exibir

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')

usuario = {
    "nome" : nome,
     "idade" : idade,
     "cidade" : cidade
}

print(f'O seu nome é: {usuario["nome"]}, e você tem {usuario["idade"]} anos !')


# solicite nome do produto, preço, quantidade e crie um dicionario

nome_produto = input('Qual o nome do produto? ')
preco = float(input('Qual o preço do produto? '))
estoque = int(input('Quantos produtos em estoque? '))

produtos = {
    'nome' : nome_produto,
    'preço' : preco,
    'estoque' : estoque
}

print(produtos)


# nome do livro, autor, ano de publicação e armazenar
nome_livro = input('Qual o nome do livro? ')
autor = input('Qual o autor do livro? ')
ano_publicacao = int(input('Qual o ano de publicação? '))

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