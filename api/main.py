from .teams.tui import admin_teams_menu
from .turmas.tui import admin_turmas_menu
from .users.tui import admin_users_menu
from .sprints.tui import admin_sprints_menu
from .evaluations.tui import admin_evaluations_menu, common_user_evaluations_menu
from .session.current import get_session, logout
from .session.tui import login, summary_session, my_profile_menu
from .utils import safe_int_input

def admin_menu():
    session = get_session()
    print("\nBem vindo ao menu principal")
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
        admin_teams_menu()
    elif option == 4:
        admin_sprints_menu()
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


def common_user_menu():
    session = get_session()
    print("\nBem vindo ao menu principal")
    print(f"Sessão atual: {summary_session(session)}")
    print("""                 
    1 - Meu Perfil   
    2 - Minhas Turmas
    3 - Meu Time
    4 - Avaliações                     
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = safe_int_input("Opção: ")
    if option == 1:
        my_profile_menu()
    elif option == 2:
        admin_turmas_menu() # trocar
    elif option == 3:
        admin_teams_menu() # trocar
    elif option == 4:
        admin_sprints_menu() # trocar
    elif option == 5:
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


def program_loop():
    while True:
        session = get_session()
        if session["user"] is None:
            login()
        else:
            if session["user"]["type"] == "ADMIN":
                admin_menu()
            else:
                common_user_menu()