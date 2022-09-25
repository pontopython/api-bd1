from .login import get_logged_user, login_user, logout_user, show_profile
from .teams import create_team_interactively, find_and_show_team, list_all_teams
from .utils import bright_input, bright_print, cyan_print, red_print
from .users import (
    create_user_interactively,
    find_and_show_user,
    list_all_users,
    save_user_to_file,
    find_and_delete_user
)


def main_menu():
    cyan_print("\n      Bem vindo ao menu principal\n")
    bright_print(
        """
        1 - Listar todos os usuários
        2 - Meu Perfil
        3 - Criar novo usuário
        4 - Procurar usuário
        5 - Editar usuário
        6 - Excluir usuário
        7 - Criar Time
        8 - Listar Times
        9 - Buscar Time
        97 - Deslogar apenas
        98 - Sair apenas
        99 - Deslogar e sair
        """
    )

    option = int(input("     Opção: "))
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
        print("Editar")
    elif option == 6:
        find_and_delete_user()
    elif option == 7:
        create_team_interactively()
    elif option == 8:
        list_all_teams()
    elif option == 9:
        find_and_show_team()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
    elif option == 99:
        logout_user()
        exit()
    else:
        red_print("     Opção inválida.\n")


def program_loop():
    while True:
        if get_logged_user() is None:
            login_user()
        else:
            main_menu()
