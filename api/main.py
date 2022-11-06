from api.teams.tui import admin_teams_menu
from api.turmas.tui import admin_turmas_menu
from api.users.tui import list_instructors, list_users, admin_users_menu
from api.sprints.tui import admin_sprints_menu
from api.evaluations.tui import admin_evaluations_menu
from .session.current import get_session, logout
from .session.tui import login

def admin_menu():
    print("\nBem vindo ao menu principal")
    print("""
    1 - Listar Usuários                    
    2 - Listar Instrutores                 
    3 - Menu Usuários                   
    4 - Menu Turmas       
    5 - Menu Times
    6 - Menu Sprints
    7 - Menu Avaliações                     
    97 - Deslogar apenas
    98 - Sair apenas
    99 - Deslogar e sair
    """
    )

    option = int(input("Opção: "))
    if option == 1:
        list_users()
    elif option == 2:
        list_instructors()
    elif option == 3:
        admin_users_menu()
    elif option == 4:
        admin_turmas_menu()
    elif option == 5:
        admin_teams_menu()
    elif option == 6:
        admin_sprints_menu
    elif option == 7:
        admin_evaluations_menu
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        ("Opção inválida.\n")

def program_loop():
    while True:
        session = get_session()
        if session["user"] is None:
            login()
        else:
            admin_menu()