from .login import get_logged_user, login_user, logout_user


def main_menu():
    print("Bem vindo ao menu principal")
    print("1 - Listar todos os usuários")
    print("98 - Deslogar apenas")
    print("99 - Deslogar e Encerrar Programa")

    option = int(input("Opção: "))
    if option == 98:
        logout_user()
    elif option == 99:
        logout_user()
        exit()
    else:
        print("Opção inválida.")


def program_loop():
    while True:
        if get_logged_user() is None:
            login_user()
        else:
            main_menu()
