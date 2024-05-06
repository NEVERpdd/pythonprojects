class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password, users):
        super().__init__(username, password)
        self.users = users

    def add_user(self, username, password):
        self.users[username] = password

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado.")

    def change_password(self, username, new_password):
        if username in self.users:
            self.users[username] = new_password
            print("Senha alterada com sucesso!")
        else:
            print("Usuário não encontrado.")

def login(users):
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    if username in users and users[username] == password:
        print("Login bem-sucedido!")
        return username
    else:
        print("Nome de usuário ou senha incorretos.")
        return None

def create_user(users):
    username = input("Digite um nome de usuário: ")
    password = input("Digite uma senha: ")
    users[username] = password
    print("Usuário criado com sucesso!")

def main():
    users = {"admin": "admin"}
    admin = Admin("admin", "admin", users)

    while True:
        print("\n=== MENU ===")
        print("1. Login")
        print("2. Criar usuário")
        choice = input("Escolha uma opção (ou 'q' para sair): ")

        if choice == "1":
            username = login(users)
            if username == "admin":
                while True:
                    print("\n=== MENU DO ADMIN ===")
                    print("1. Alterar senha de usuário")
                    print("2. Adicionar usuário")
                    print("3. Remover usuário")
                    print("4. Listar usuários")
                    print("5. Voltar ao menu principal")
                    admin_choice = input("Escolha uma opção: ")

                    if admin_choice == "1":
                        username = input("Digite o nome de usuário para alterar a senha: ")
                        new_password = input("Digite a nova senha: ")
                        admin.change_password(username, new_password)

                    elif admin_choice == "2":
                        create_user(users)

                    elif admin_choice == "3":
                        username = input("Digite o nome de usuário para remover: ")
                        admin.remove_user(username)

                    elif admin_choice == "4":
                        print(users)

                    elif admin_choice == "5":
                        break
                    else:
                        print("Opção inválida.")

            elif username:
                pass

        elif choice == "2":
            create_user(users)

        elif choice.lower() == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
