from api.teams.tui import list_teams, new_team, remove_team, show_members, edit_team, show_team
from api.turmas.tui import edit_turma, list_turmas, new_turma, remove_turma, show_turma
from api.users.tui import list_instructors, list_users, admin_create_a_new_user, remove_user, show_user, edit_user
from .login import get_logged_user, login_user, logout_user

def admin_main():
    print("\nBem vindo ao menu principal")
    print("""
    1 - Listar Usuários                    
    2 - Listar Instrutores                 
    3 - Criar novo usuário                 
    4 - Procurar e Detalhar Usuário        
    5 - Editar usuário                     
    6 - Excluir usuário                    
    7 - Mostrar Membros do Time            
    8 - Criar Novo Time                    
    9 - Editar Time                        
    10 - Excluir Time                       
    11 - Listar Times                       
    12 - Procurar e Detalhar Time           
    13 - Listar Turmas                      
    14 - Detalhar Turma                     
    15 - Criar Nova Turma                   
    16 - Editar Turma                       
    17 - Excluir Turma                      
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
        admin_create_a_new_user()
    elif option == 4:
        show_user()
    elif option == 5:
        edit_user()
    elif option == 6:
        remove_user()
    elif option == 7:
        show_members()
    elif option == 8:
        new_team()
    elif option == 9:
        edit_team()
    elif option == 10:
        remove_team()
    elif option == 11:
        list_teams()
    elif option == 12:
        show_team()
    elif option == 13:
        list_turmas()
    elif option == 14:
        show_turma()
    elif option == 15:
        new_turma()
    elif option == 16:
        edit_turma()
    elif option == 17:
        remove_turma()
    elif option == 97:
        logout_user()
    elif option == 98:
        exit()
    elif option == 99:
        logout_user()
        exit()
    else:
        ("Opção inválida.\n")

def program_loop():
    while True:
        current_user = get_logged_user()
        if current_user is None:
            login_user()
        else:
            admin_main()