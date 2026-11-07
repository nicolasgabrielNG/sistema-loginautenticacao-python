usuarios = {"Nick": "12345"}  # usuário: senha


def mostrar_boas_vindas():
    print("Sistema de Autenticação")
    print("Seja bem-vindo!")


def cadastrar():
    usuario = input("Escolha um usuário: ")

    if usuario in usuarios:
        print("Esse usuário já existe.")
        return

    senha = input("Escolha uma senha: ")

    if len(senha) < 5:
        print("A senha precisa ter pelo menos 5 caracteres.")
        return

    usuarios[usuario] = senha
    print("Cadastro realizado com sucesso!")


def realizar_login():
    tentativas = 3

    while tentativas > 0:
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        if usuarios.get(usuario) == senha:
            print(f"Login realizado com sucesso! Olá, {usuario}!")
            return usuario

        tentativas -= 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

    print("Acesso bloqueado.")
    return None


def menu():
    mostrar_boas_vindas()

    while True:
        print("\n===== SISTEMA DE AUTENTICAÇÃO =====")
        print("1 - Fazer login")
        print("2 - Cadastrar usuário")
        print("3 - Alterar senha")
        print("4 - Excluir usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            realizar_login()

        elif opcao == "2":
            cadastrar()

        elif opcao == "3":
            print("Funcionalidade em desenvolvimento.")

        elif opcao == "4":
            print("Funcionalidade em desenvolvimento.")

        elif opcao == "5":
            print("Até logo!")
            break

        else:
            print("Opção inválida.")
menu ()