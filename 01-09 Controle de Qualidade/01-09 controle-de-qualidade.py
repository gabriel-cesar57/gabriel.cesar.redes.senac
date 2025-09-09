#Desafio Proposto aos Alunos
#Construir o sistema de entrada de dados usando input().
#Criar uma estrutura de armazenamento adequada (listas e dicionários).
#Implementar uma função que compare os valores com os limites e registre os erros.
#Ao final, exibir um relatório resumido destacando os lotes e linhas que apresentaram problemas.

# Brix: entre 10,5 e 11,2 °Bx
# pH: entre 2,3 e 2,6
# Nível: entre 195 e 205 mL


entrada = input("Digite os dados do lote (Brix, pH, Nível) separados por vírgula: ")

brix, ph, nivel = map(float, entrada.split(','))
lote = {"Brix": brix, "pH": ph, "Nível": nivel}
erros = []


def verificar_limites(lote):
    erros = []
    if not (10.5 <= lote["Brix"] <= 11.2):
        erros.append("Brix fora do limite")
    if not (2.3 <= lote["pH"] <= 2.6):
        erros.append("pH fora do limite")
    if not (195 <= lote["Nível"] <= 205):
        erros.append("Nível fora do limite")
    return erros


erros = verificar_limites(lote)


print("\nRelatório do Lote:")
print(f"Brix: {lote['Brix']} °Bx")
print(f"pH: {lote['pH']}")
print(f"Nível: {lote['Nível']} mL")
if erros:
    print("Erros encontrados:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("Todos os parâmetros dentro dos limites.")

