from rich import print
from rich.panel import Panel

from .teams.tui import admin_and_LG_teams_menu
from .turmas.tui import admin_turmas_menu, menu_list_turmas
from .users.tui import admin_users_menu, LG_users_menu
from .sprints.tui import admin_and_LG_sprints_menu
from .evaluations.tui import admin_evaluations_menu, common_user_evaluations_menu, LG_user_evaluations_menu, FC_user_evaluations_menu
from .session.current import get_session, logout
from .session.tui import login, summary_session, my_profile_menu
from .utils import safe_int_input, clear_screen, console 

def admin_menu():
    
    session = get_session()
    console.rule("\n [bold blue]Bem vindo ao menu principal (Administrador)[/bold blue]")
    console.print(f"\n [green]Sessão atual:[/green] {summary_session(session)}")
    console.print("""
    [blue] 1 -[/blue] [yellow]Usuários [/yellow]
    [blue] 2 -[/blue] [yellow]Turmas[/yellow]
    [blue] 3 -[/blue] [yellow]Times[/yellow]
    [blue] 4 -[/blue] [yellow]Sprints[/yellow]
    [blue] 5 -[/blue] [yellow]Avaliações[/yellow]
    [blue]97 -[/blue] [yellow]Deslogar apenas[/yellow]
    [blue]98 -[/blue] [yellow]Sair apenas[/yellow]
    [blue]99 -[/blue] [yellow]Deslogar e sair[/yellow]
    """
    )
    console.print()

    option = safe_int_input("\nOpção: ")
    clear_screen()
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
        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
        console.print()

def group_leader_menu():
    
    session = get_session()
    console.rule("\n [bold blue]Bem vindo ao menu principal (Líder de Grupo)[/bold blue]")
    console.print(f"\n [green]Sessão atual: [/green]{summary_session(session)}")
    console.print("""
    [blue] 1 -[/blue] [yellow]Meu Perfil[/yellow]
    [blue] 2 -[/blue] [yellow]Minhas Turmas[/yellow]
    [blue] 3 -[/blue] [yellow]Usuários[/yellow]
    [blue] 4 -[/blue] [yellow]Times[/yellow]
    [blue] 5 -[/blue] [yellow]Sprints[/yellow]
    [blue] 6 -[/blue] [yellow]Avaliações[/yellow]
    [blue]97 -[/blue] [yellow]Deslogar apenas[/yellow]
    [blue]98 -[/blue] [yellow]Sair apenas[/yellow]
    [blue]99 -[/blue] [yellow]Deslogar e sair[/yellow]
    """
    )
    console.print()

    option = safe_int_input("\nOpção: ")
    clear_screen()
    if option == 1:
        my_profile_menu()
    elif option == 2:
        menu_list_turmas(session["user"])
    elif option == 3:
        LG_users_menu()
    elif option == 4:
        admin_and_LG_teams_menu()
    elif option == 5:
        admin_and_LG_sprints_menu(session["turma"])
    elif option == 6:
        LG_user_evaluations_menu(session["turma"], session["user"])
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
        console.print()

def common_user_menu():
    
    session = get_session()
    console.rule("\n [bold blue]Bem vindo ao menu principal[/bold blue]")
    console.print(f"\n [green]Sessão atual:[/green] {summary_session(session)}")
    console.print("""
    [blue] 1 -[/blue] [yellow]Meu Perfil[/yellow]
    [blue] 2 -[/blue] [yellow]Minhas Turmas[/yellow]
    [blue] 3 -[/blue] [yellow]Avaliações[/yellow]
    [blue]97 -[/blue] [yellow]Deslogar apenas[/yellow]
    [blue]98 -[/blue] [yellow]Sair apenas[/yellow]
    [blue]99 -[/blue] [yellow]Deslogar e sair[/yellow]
    """
    )
    console.print()    

    option = safe_int_input("\nOpção: ")
    clear_screen()
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
        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
        console.print()

def fake_client_menu():
    
    session = get_session()
    console.rule("\n [bold blue]Bem vindo ao menu principal (Fake Client)[/bold blue]")
    console.print(f"\n [green]Sessão atual: [/green]{summary_session(session)}")
    console.print("""
    [blue] 1 -[/blue] [yellow]Meu Perfil[/yellow]
    [blue] 2 -[/blue] [yellow]Minhas Turmas[/yellow]
    [blue] 3 -[/blue] [yellow]Avaliações[/yellow]
    [blue]97 -[/blue] [yellow]Deslogar apenas[/yellow]
    [blue]98 -[/blue] [yellow]Sair apenas[/yellow]
    [blue]99 -[/blue] [yellow]Deslogar e sair[/yellow]
    """
    )
    console.print()

    option = safe_int_input("\nOpção: ")
    clear_screen()
    if option == 1:
        my_profile_menu()
    elif option == 2:
        menu_list_turmas(session["user"])
    elif option == 3:
        FC_user_evaluations_menu(session["turma"], session["user"])
    elif option == 97:
        logout()
    elif option == 98:
        exit()
    elif option == 99:
        logout()
        exit()
    else:
        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
        console.print()

def program_loop():
    clear_screen()
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