import stdiomask
from rich.markdown import Markdown

from ..utils import safe_int_input, clear_screen, console
from ..users.prompt import prompt_user_email
from ..users.repository import get_user_by_email
from ..users.tui import detail_user, edit_user
from ..turmas.tui import select_turma_from_user
from ..teams.repository import get_team_from_turma_and_student

from .current import get_session, update_session

def summary_session(session):
    user_name = session["user"]["name"]

    if session["turma"] is None:
        turma_name = "-"
    else:
        turma_name = session["turma"]["name"]

    if session["team"] is None:
        team_name = "-"
    else:
        team_name = session["team"]["name"]

    return f"{user_name} (Turma: {turma_name}, Time: {team_name})"


def login():
    console.rule("[bold underline blue]Sistema de Avaliação 360º[/bold underline blue]")

    email = prompt_user_email()
    user = get_user_by_email(email)
    if user is None:
        console.print(":x: [bold red]Usuário não encontrado[/bold red] :x:", justify="center")
        console.print()
        return

    console.print(f":lock: Senha: ", end="")
    password = stdiomask.getpass(prompt="", mask="*")
    if password != user["password"]:
        console.print(":x: [bold red]Credenciais inválidas[/bold red] :x:", justify="center")
        console.print()
        return

    turma = select_turma_from_user(user)

    if turma is None:
        team = None
    else:
        team = get_team_from_turma_and_student(turma, user)

    session = get_session()
    session["user"] = user
    session["turma"] = turma
    session["team"] = team

    update_session()


def my_profile_menu():
    session = get_session()
    while True:
        console.print("[bold blue]Meu Perfil[/bold blue]", justify="center")
        console.print("\n[blue]1 -[/blue] [yellow]Visualizar[/yellow]")
        console.print("[blue]2 -[/blue] [yellow]Editar[/yellow]")
        console.print("[blue]3 -[/blue] [yellow]Voltar[/yellow]")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 3:
                clear_screen()
                break
            console.print(":x: [bold red]Opção inválida[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            detail_user(session["user"])
        elif option == 2:
            edit_user(session["user"])
        else:
            return
