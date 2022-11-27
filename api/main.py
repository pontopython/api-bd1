from rich import print
from rich.panel import Panel

from .teams.tui import admin_and_LG_teams_menu
from .turmas.tui import admin_turmas_menu, menu_list_turmas
from .users.tui import admin_users_menu, LG_users_menu
from .sprints.tui import admin_and_LG_sprints_menu
from .evaluations.tui import admin_evaluations_menu, common_user_evaluations_menu, LG_user_evaluations_menu, FC_user_evaluations_menu
from .session.current import get_session, logout
from .session.tui import login, summary_session, my_profile_menu
<<<<<<< HEAD
from .utils import safe_int_input, clear_screen

import os

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
=======
from .utils import safe_int_input, console

def admin_menu():
    session = get_session()
    console.rule("\n [blue]Bem vindo ao menu principal (Administrador)[/blue]")
    console.print(f"\n [green]Sessão atual:[/green] {summary_session(session)}")
    console.print("""
    [blue]1 -[/blue] Usuários
    [blue]2 -[/blue] Turmas
    [blue]3 -[/blue] Times
    [blue]4 -[/blue] Sprints
    [blue]5 -[/blue] Avaliações
    [blue]97 -[/blue] Deslogar apenas
    [blue]98 -[/blue] Sair apenas
    [blue]99 -[/blue] Deslogar e sair
>>>>>>> f0064dce9847383db81c3d6b28dbbcb0f19fd854
    """
    )
    console.print()

    option = safe_int_input("Opção: ")
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
    console.rule("\n [blue]Bem vindo ao menu principal (Líder de Grupo)[/blue]")
    console.print(f"\n [green]Sessão atual: [/green]{summary_session(session)}")
    console.print("""
    [blue]1 -[/blue] Meu Perfil
    [blue]2 -[/blue] Minhas Turmas
    [blue]3 -[/blue] Usuários
    [blue]4 -[/blue] Times
    [blue]5 -[/blue] Sprints
    [blue]6 -[/blue] Avaliações
    [blue]97 -[/blue] Deslogar apenas
    [blue]98 -[/blue] Sair apenas
    [blue]99 -[/blue] Deslogar e sair
    """
    )
    console.print()

    option = safe_int_input("Opção: ")
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
    console.rule("\n [blue]Bem vindo ao menu principal[/blue]")
    console.print(f"\n [green]Sessão atual:[/green] {summary_session(session)}")
    console.print("""
    [blue]1 -[/blue] Meu Perfil
    [blue]2 -[/blue] Minhas Turmas
    [blue]3 -[/blue] Avaliações
    [blue]97 -[/blue] Deslogar apenas
    [blue]98 -[/blue] Sair apenas
    [blue]99 -[/blue] Deslogar e sair
    """
    )
    console.print()    

    option = safe_int_input("Opção: ")
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
<<<<<<< HEAD
        print("Opção inválida.\n")
        
=======
        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
        console.print()
>>>>>>> f0064dce9847383db81c3d6b28dbbcb0f19fd854

def fake_client_menu():
    session = get_session()
    console.rule("\n [blue]Bem vindo ao menu principal (Fake Client)[blue]")
    console.print(f"\n [green]Sessão atual: [/green]{summary_session(session)}")
    console.print("""
    [blue]1 -[/blue] Meu Perfil
    [blue]2 -[/blue] Minhas Turmas
    [blue]3 -[/blue] Avaliações
    [blue]97 -[/blue] Deslogar apenas
    [blue]98 -[/blue] Sair apenas
    [blue]99 -[/blue] Deslogar e sair
    """
    )
    console.print()

    option = safe_int_input("Opção: ")
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
    while True:
        session = get_session()
        clear_screen()
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
