#Rafael Rodrigues - RM 555794
#Lucas Takemoto - RM556804

# Questão 1:
def cadastrar_livro(livros):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    livros.append({"Título": titulo, "Autor": autor, "Ano": ano})
    print("Livro cadastrado com sucesso!")

# Questão 2:
def listar_livros(livros):
    print("Listagem de Livros:")
    for livro in livros:
        print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")

# Questão 3:
def buscar_livros_por_autor(livros, autor):
    print(f"Livros do autor {autor}:")
    for livro in livros:
        if livro['Autor'] == autor:
            print(f"Título: {livro['Título']}, Ano: {livro['Ano']}")

# Questão 4:
def menu():
    livros = []
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livros por autor")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            autor = input("Digite o nome do autor: ")
            buscar_livros_por_autor(livros, autor)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Questão 5:
menu()

# Questão 6: a) for i in lista: