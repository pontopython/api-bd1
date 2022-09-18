from .login import get_logged_user, login_user, logout_user, show_profile
from .teams import create_team_interactively, find_and_show_team, list_all_teams
from .users import (
    create_user_interactively,
    find_and_show_user,
    list_all_users,
    save_user_to_file,
)


def main_menu():
    print("Bem vindo ao menu principal")
    print("1 - Listar todos os usuários")
    print("2 - Meu Perfil")
    print("3 - Criar novo usuário")
    print("4 - Procurar usuário")
    print("5 - Criar Time")
    print("6 - Listar Times")
    print("7 - Buscar Time")
    print("97 - Deslogar apenas")
    print("98 - Sair apenas")
    print("99 - Deslogar e sair")

    option = int(input("Opção: "))
    if option == 1:
        list_all_users()
    elif option == 2:
        show_profile()
    elif option == 3:
        user = create_user_interactively()
        save_user_to_file(user)
    elif option == 4:
        find_and_show_user()
    elif option == 5:
        create_team_interactively()
    elif option == 6:
        list_all_teams()
    elif option == 7:
        find_and_show_team()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
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
