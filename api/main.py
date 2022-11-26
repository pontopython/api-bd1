from .teams.tui import admin_and_LG_teams_menu
from .turmas.tui import admin_turmas_menu, menu_list_turmas
from .users.tui import admin_users_menu, LG_users_menu
from .sprints.tui import admin_and_LG_sprints_menu
from .evaluations.tui import admin_evaluations_menu, common_user_evaluations_menu, LG_user_evaluations_menu, FC_user_evaluations_menu
from .session.current import get_session, logout
from .session.tui import login, summary_session, my_profile_menu
from .utils import safe_int_input

def admin_menu():
    session = get_session()
    print("\nBem vindo ao menu principal (Administrador)")
    print(f"Sessão atual: {summary_session(session)}")
    print("""
    1 - Usuários
    2 - Turmas
    3 - Times
    4 - Sprints
    5 - Avaliações
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = safe_int_input("Opção: ")
    if option == 1:
        admin_users_menu()
    elif option == 2:
        admin_turmas_menu()
    elif option == 3:
        admin_and_LG_teams_menu()
    elif option == 4:
        admin_and_LG_sprints_menu()
    elif option == 5:
        admin_evaluations_menu()
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        print("Opção inválida.\n")

def group_leader_menu():
    session = get_session()
    print("\nBem vindo ao menu principal (Líder de Grupo)")
    print(f"Sessão atual: {summary_session(session)}")
    print("""
    1 - Meu Perfil
    2 - Minhas Turmas
    3 - Usuários
    4 - Times
    5 - Sprints
    6 - Avaliações
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = safe_int_input("Opção: ")
    if option == 1:
        my_profile_menu()
    elif option == 2:
        menu_list_turmas(session["user"])
    elif option == 3:
        LG_users_menu()
    elif option == 4:
        admin_and_LG_teams_menu()
    elif option == 5:
        admin_and_LG_sprints_menu()
    elif option == 6:
        LG_user_evaluations_menu(session["user"])
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        print("Opção inválida.\n")

def common_user_menu():
    session = get_session()
    print("\nBem vindo ao menu principal")
    print(f"Sessão atual: {summary_session(session)}")
    print("""
    1 - Meu Perfil
    2 - Minhas Turmas
    3 - Avaliações
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = safe_int_input("Opção: ")
    if option == 1:
        my_profile_menu()
    elif option == 2:
        menu_list_turmas(session["user"])
    elif option == 3:
        common_user_evaluations_menu(session["team"], session["user"])
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        print("Opção inválida.\n")

def fake_client_menu():
    session = get_session()
    print("\nBem vindo ao menu principal (Fake Client)")
    print(f"Sessão atual: {summary_session(session)}")
    print("""
    1 - Meu Perfil
    2 - Minhas Turmas
    3 - Avaliações
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = safe_int_input("Opção: ")
    if option == 1:
        my_profile_menu()
    elif option == 2:
        menu_list_turmas(session["user"])
    elif option == 3:
        FC_user_evaluations_menu(session["user"])
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        print("Opção inválida.\n")


def program_loop():
    while True:
        session = get_session()
        if session["user"] is None:
            login()
        else:
            if session["user"]["type"] == "ADMIN":
                admin_menu()
            elif (
                session["user"]["type"] == "INSTR"
                and session["turma"] is not None
                and session["turma"]["group_leader"]["id"] == session["user"]["id"]
            ):
                group_leader_menu()
            elif (
                session["user"]["type"] == "INSTR"
                and session["turma"] is not None
                and session["turma"]["fake_client"]["id"] == session["user"]["id"]
            ):
                fake_client_menu()
            else:
                common_user_menu()
