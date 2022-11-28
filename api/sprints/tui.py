from ..utils import safe_int_input, clear_screen, console
from ..turmas.tui import search_and_select_turma
from .repository import get_all_sprints_from_group, create_sprint, get_opened_sprint_from_group, update_sprints


def summary_sprint(sprint):
    name = sprint["name"]
    id = sprint["id"]
    status = sprint["status"]
    return f"{name} #{id} ({status})"


def show_sprints_from_group(group):
    sprints = get_all_sprints_from_group(group)
    console.print("\n [green]Sprints[/green]")
    console.print()
    for sprint in sprints:
        print(f"\n    - {summary_sprint(sprint)}")


def has_group_opened_sprint(group):
    opened_sprints = get_opened_sprint_from_group(group)
    return opened_sprints is not None


def open_sprint_for_group(group):
    if has_group_opened_sprint(group):
        console.print("\n [bold red]Já existe uma sprint aberta.[/bold red]")
        console.print()
        return
    sprint_name = console.input('\n [purple]Qual o nome da sprint?[/purple] ')
    create_sprint(group, sprint_name)


def close_sprint_from_group(group):
    if not has_group_opened_sprint(group):
        console.print("\n [bold red]Não existe sprint aberta.[/bold red]")
        console.print()
        return
    sprint = get_opened_sprint_from_group(group)
    print(summary_sprint(sprint))
    answer = console.input("\n [yellow]Tem certeza que deseja fechar essa sprint ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if answer != "S" and answer != "s":
        return
    sprint["status"] = "fechada"
    update_sprints()


def select_sprint_from_group(group, closed=False):
    sprints = get_all_sprints_from_group(group)
    if not closed:
        valid_sprints = sprints
    if closed:
        valid_sprints = []
        for sprint in sprints:
            if sprint['status'] == 'fechada':
                valid_sprints.append(sprint)

    if len(valid_sprints) == 0:
        console.print("\n [bold red]Nenhuma sprint encontrada.[/bold red]")
        console.print()
        return None

    for index, sprint in enumerate(valid_sprints):
        print(f"{index+1} - {summary_sprint(sprint)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(sprints):
            return valid_sprints[option - 1]
        console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
        console.print()

def reopen_sprint_from_group(group):
    if has_group_opened_sprint(group):
        console.print("\n [bold red]Já existe uma sprint aberta.[/bold red]")
        console.print()
        return
    sprint = select_sprint_from_group(group)

    if sprint is None:
        return

    print(summary_sprint(sprint))
    answer = console.input("\n Tem certeza que deseja reabrir essa sprint ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if answer != "S" and answer != "s":
        return
    sprint["status"] = "aberta"
    update_sprints()


def admin_and_LG_sprints_menu(turma=None):
    clear_screen()
    if turma is None:
        console.print("\n [green]Selecione a Turma[/green]")
        console.print()
        turma = search_and_select_turma()

    if turma is None:
        console.print("\n [bold red]Nenhuma turma encontrada.[/bold red]")
        console.print()
        return

    while True:
        console.rule("\n [bold blue]Menu Sprints (Administrador)[/bold blue]")
        console.print(f"\n [green]Turma:[/green] {turma['name']}\n")
        console.print("[blue]1 -[/blue] [yellow]Listar[/yellow]")
        console.print("[blue]2 -[/blue] [yellow]Abrir Nova[/yellow]")
        console.print("[blue]3 -[/blue] [yellow]Fechar[/yellow]")
        console.print("[blue]4 -[/blue] [yellow]Reabrir[/yellow]")
        console.print("[blue]5 -[/blue] [yellow]Voltar[/yellow]")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 6:
                clear_screen()
                break
            console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            show_sprints_from_group(turma)
        elif option == 2:
            open_sprint_for_group(turma)
        elif option == 3:
            close_sprint_from_group(turma)
        elif option == 4:
            reopen_sprint_from_group(turma)
        else:
            return
