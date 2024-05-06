# Fix opcao 1 e 4

import os

usuarios = {"admin": ["123", "adm"], "melissa": ["123456", "usr"]}

# Menu
def menu():
    print("Digite 1 para Login")
    print("Digite 2 para Listar")
    print("Digite 3 para Alterar minha senha")
    print("Digite 4 para Alterar senha de um usuario")
    print("Digite 5 para Adicionar")
    print("Digite 6 para Excluir")
    print("Digite 7 para Buscar")
    print("Digite 8 para Sair")
    opcao = int(input("Entre com a opção: "))

    if opcao == 1:
        login()
    elif opcao == 2:
        lista()
    elif opcao == 3:
        alterar_minha_senha()
    elif opcao == 4:
        alterar_outros()
    elif opcao == 5:
        adicionar()
    elif opcao == 6:
        remover()
    elif opcao == 7:
        buscar()
    elif opcao == 8:
        quit()
    else:
        print("Opção Inválida!")

# Listar
def lista():
    os.system ("cls")
    for chave, dados in usuarios.items():
        print(f"Nome ......... {chave}")
        print(f"Senha ........ {dados[0]}")
        print(f"Nível ........ {dados[1]}")
    input("Continuar...")

# Adicionar
def adicionar():
    os.system ("cls")
    nome = input("Entre com o nome: ")
    senha = input("Entre com a senha: ")
    nivel = input("Entre com o nível: ")
    usuarios[nome] = [senha, nivel]
    input("Continuar...")

# Alterar a senha
def alterar_minha_senha():
    os.system ("cls")
    alterar = input("Entre com o nome: ")
    if alterar in usuarios:
        usuarios[alterar][0] = input("Entre com a nova senha: ")
    else:
        print("Usuário não encontrado!")
    input("Continuar...")

# Remover
def remover():
    os.system ("cls")
    remover = input("Entre com o nome: ")
    if remover in usuarios:
        del usuarios[remover]
    else:
        print("Usuário não encontrado!")
    input("Continuar...")

# Buscar
def buscar():
    os.system ("cls")
    busca = input("Entre com o nome: ")
    if busca in usuarios:
        print(f"Nome ......... {busca}")
        print(f"Senha ........ {usuarios[busca][0]}")
        print(f"Nível ........ {usuarios[busca][1]}")
    else:
        print("Usuário não encontrado!")
    input("Continuar...")

# Main function
def main():
    while True:
        os.system ("cls")
        menu()

if __name__ == "__main__":
    main()
