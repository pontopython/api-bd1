from .evaluation import run_evaluation, run_mean_grades
from .login import (
    change_current_user_name,
    get_logged_user,
    login_user,
    logout_user,
    show_profile,
)
from .teams import (
    create_team_interactively,
    edit_team,
    find_and_delete_team,
    find_and_show_team,
    list_all_teams,
)
from .old_users import (
    create_user_interactively,
    edit_user,
    find_and_delete_user,
    find_and_show_user,
    find_user_interactively,
    create_users_list,
    list_all_users,
    select_user_interactively,
)
from .utils import bright_input, bright_print, cyan_print, red_print


def admin_menu():
    cyan_print("\n      Bem vindo ao menu principal\n")
    bright_print(
        """
         1 - Listar todos os usuários
         2 - Meu Perfil
         3 - Criar novo usuário
         4 - Procurar usuário
         5 - Editar usuário
         6 - Excluir usuário
         7 - Criar time
         8 - Listar times
         9 - Buscar time
        10 - Editar time
        11 - Excluir time
        12 - Avaliar membro de um time
        13 - Ver médias
        14 - Selecionar Usuário
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
        create_user_interactively()
    elif option == 4:
        find_and_show_user()
    elif option == 5:
        edit_user()
    elif option == 6:
        find_and_delete_user()
    elif option == 7:
        create_team_interactively()
    elif option == 8:
        list_all_teams()
    elif option == 9:
        find_and_show_team()
    elif option == 10:
        edit_team()
    elif option == 11:
        find_and_delete_team()
    elif option == 12:
        run_evaluation()
    elif option == 13:
        run_mean_grades()
    elif option == 14:
        find_user_interactively()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
    elif option == 99:
        logout_user()
        exit()
    else:
        red_print("     Opção inválida.\n")


def team_leader_menu():
    cyan_print("\n      Bem vindo ao menu principal\n")
    bright_print(
        """
         1 - Listar todos os usuários
         2 - Meu Perfil
         3 - Criar novo usuário
         4 - Procurar usuário
         5 - Criar time
         6 - Listar times
         7 - Buscar time
         8 - Editar time
         9 - Avaliar membro de um time
        10 - Ver médias
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
        create_user_interactively()
    elif option == 4:
        find_and_show_user()
    elif option == 5:
        create_team_interactively()
    elif option == 6:
        list_all_teams()
    elif option == 7:
        find_and_show_team()
    elif option == 8:
        edit_team()
    elif option == 9:
        run_evaluation()
    elif option == 10:
        run_mean_grades()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
    elif option == 99:
        logout_user()
        exit()
    else:
        red_print("     Opção inválida.\n")


def fake_client_menu():
    cyan_print("\n      Bem vindo ao menu principal\n")
    bright_print(
        """
         1 - Meu Perfil
         2 - Listar times
         3 - Buscar time
         4 - Avaliar membro de um time
         5 - Ver médias
        97 - Deslogar apenas
        98 - Sair apenas
        99 - Deslogar e sair
        """
    )

    option = int(input("     Opção: "))
    if option == 1:
        show_profile()
    elif option == 2:
        list_all_teams()
    elif option == 3:
        find_and_show_team()
    elif option == 4:
        run_evaluation()
    elif option == 5:
        run_mean_grades()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
    elif option == 99:
        logout_user()
        exit()
    else:
        red_print("     Opção inválida.\n")


def user_menu():
    cyan_print("\n      Bem vindo ao menu principal\n")
    bright_print(
        """
         1 - Meu Perfil
         2 - Editar meu perfil
         3 - Listar times
         4 - Buscar time
         5 - Avaliar membro de um time
         6 - Ver médias
        97 - Deslogar apenas
        98 - Sair apenas
        99 - Deslogar e sair
        """
    )

    option = int(input("     Opção: "))
    if option == 1:
        show_profile()
    elif option == 2:
        change_current_user_name()
    elif option == 3:
        list_all_teams()
    elif option == 4:
        find_and_show_team()
    elif option == 5:
        run_evaluation()
    elif option == 6:
        run_mean_grades()
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
        current_user = get_logged_user()
        if current_user is None:
            login_user()
        else:
            admin_menu()
