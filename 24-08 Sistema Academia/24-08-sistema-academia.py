# Sistema de alunos de uma academia

# Crie o sistema de cadastro inicial (como acima).
#
#Implemente as funções para calcular médias, exibir dados e listar alunos ativos.
#
#Teste a inserção de novos alunos e execute as funções para verificar o correto uso dos tipos de dados (int, float, str, bool, list, dict).
#
#Adapte para permitir remoção ou alteração de dados de alunos.




# Lista de alunos (cada aluno é um dicionário)
alunos = [
    {"nome": "Gabriel", "idade": 21, "altura": 1.80, "ativo": True,  "avaliacoes": [9.0, 9.0, 8.2]},
    {"nome": "Mago Negro", "idade": 999, "altura": 1.83, "ativo": False, "avaliacoes": [2.0, 2.5, 6.0]},
    {"nome": "Luana", "idade": 22, "altura": 1.65, "ativo": True,  "avaliacoes": [6.0, 5.5, 9.2]},
    {"nome": "Ben-10", "idade": 10, "altura": 10, "ativo": True,  "avaliacoes": [10.0, 10.0, 10.0]},
]

# Função para calcular a média das avaliações
def calcular_media(avaliacoes):
    return sum(avaliacoes) / len(avaliacoes) if avaliacoes else 0.0

# Exibir dados dos alunos
def exibir_alunos(alunos):
    for a in alunos:
        print(f"Nome: {a['nome']}")
        print(f"Idade: {a['idade']}")
        print(f"Altura: {a['altura']}")
        print(f"Ativo: {a['ativo']}")
        print(f"Média avaliações: {calcular_media(a['avaliacoes']):.2f}")
        print("-" * 20)

# Listar apenas alunos ativos
def listar_ativos(alunos):
    return [a for a in alunos if a["ativo"]]

# Função para cadastrar novo aluno
def cadastrar(alunos, nome, idade, altura, ativo, avaliacoes):
    alunos.append({"nome": nome, "idade": idade, "altura": altura, "ativo": ativo, "avaliacoes": avaliacoes})


print("1) Cadastrar aluno")
print("2) Exibir todos os alunos")
print("3) Listar alunos ativos")
print("4) Sair")

input_usuario = input("Escolha uma opção: ")

while input_usuario != "4":
    if input_usuario == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura (em metros): "))
        ativo = input("Ativo (s/n): ").lower() == 's'
        avaliacoes = list(map(float, input("Avaliações (separadas por vírgula): ").split(',')))
        cadastrar(alunos, nome, idade, altura, ativo, avaliacoes)
        print(f"Aluno {nome} cadastrado com sucesso!")
    elif input_usuario == "2":
        print("Todos os alunos:")
        exibir_alunos(alunos)
    elif input_usuario == "3":
        print("Alunos ativos:")
        exibir_alunos(listar_ativos(alunos))
    else:
        print("Opção inválida. Tente novamente.")

    print("\n1) Cadastrar aluno")
    print("2) Exibir todos os alunos")
    print("3) Listar alunos ativos")
    print("4) Sair")

    input_usuario = input("Escolha uma opção: ")
