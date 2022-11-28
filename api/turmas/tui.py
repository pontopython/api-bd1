from ..utils import blue_bright_print, bright_input, red_print, safe_int_input, clear_screen, console
from .repository import delete_turma, get_turmas, get_turmas_from_user, search_turmas, create_turma, delete_turma, get_turmas_by, search_students, update_turmas
from .prompt import prompt_turma_name
from ..users.tui import search_and_select_instructor, search_and_select_common_user, list_common_users, list_instructors


def summary_turma(turma):
    name = turma["name"]
    group_leader_name = turma["group_leader"]["name"]
    fake_client_name = turma["fake_client"]["name"]
    students_count = len(turma["students"])
    return f"{name} (Líder de Grupo: {group_leader_name}, Fake Client: {fake_client_name}, {students_count} alunos)"


def summary_student(student):
    name = student["name"]
    email = student["email"]
    return f"{name} <{email}>"


def detail_turma(turma, title="Detalhes da Turma:"):
    id = turma["id"]
    name = turma["name"]
    group_leader_name = turma["group_leader"]["name"]
    group_leader_email = turma["group_leader"]["email"]
    fake_client_name = turma["fake_client"]["name"]
    fake_client_email = turma["fake_client"]["email"]
    students_count = len(turma["students"])
    students = turma["students"]
    count = 0

    clear_screen()

    print(title)
    console.print(f"\n [yellow]Id:[/yellow] {id}")
    console.print(f"[yellow]Nome:[/yellow] {name}")
    console.print(f"[yellow]Líder de Grupo:[/yellow] {group_leader_name} <{group_leader_email}>")
    console.print(f"[yellow]Fake Client:[/yellow] {fake_client_name} <{fake_client_email}>")
    console.print(f"[yellow]Total de Alunos:[/yellow] {students_count}")
    console.print()
    while count < len(students):
        aluno = students[count]
        console.print(f"\n [yellow]Aluno:[/yellow] {aluno['name']}")
        console.print()
        count += 1


def list_turmas():
    console.print("\n [purple]Turmas:[/purple]")
    console.print()
    for turma in get_turmas():
        print(f"    - {summary_turma(turma)}")


def search_and_select_turma():
    search_term = console.input("\n [green]Procurar:[/green] ")
    turmas = search_turmas(search_term)

    if len(turmas) == 0:
        console.print("\n [bold red]Nenhuma turma encontrada.[/bold red]")
        console.print()
        return None

    for index, turma in enumerate(turmas):
        console.print(f"\n[blue]{index+1}[/blue] - {summary_turma(turma)}")

    while True:
        option = safe_int_input("\nOpção: ")
        if option > 0 and option <= len(turmas):
            return turmas[option - 1]
        console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
        console.print()


def select_turma_from_user(user):
    turmas = get_turmas_from_user(user)

    if len(turmas) == 0:
        if user["type"] != "ADMIN":
            console.print("\n [red]Nenhuma turma encontrada.[/red]")
        console.print()
        return None

    if len(turmas) == 1:
        return turmas[0]

    for index, turma in enumerate(turmas):
        print(f"{index+1} - {summary_turma(turma)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(turmas):
            return turmas[option - 1]
        console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
        console.print()


def show_turma():
    turma = search_and_select_turma()
    if turma is None:
        return
    detail_turma(turma)


def new_turma():
    console.print("\n [purple]Nova Turma[/purple]")
    name = prompt_turma_name()

    console.print("\n [green]Selecione um Líder de Grupo[/green]")
    console.print()
    group_leader = search_and_select_instructor()
    while group_leader is None:
        group_leader = search_and_select_instructor()
    console.print("\n [green]Líder do Grupo selecionado[/green]")

    console.print("\n [green]Selecione um Fake Client[/green]")
    console.print()
    fake_client = search_and_select_instructor(excludes=[group_leader])
    while fake_client is None:
        fake_client = search_and_select_instructor(excludes=[group_leader])
    console.print("\n [green]Fake Client selecionado[/green]")
    console.print()

    list_common_users()
    console.print("\n [green]Selecione os estudantes:[/green]")
    console.print()
    students = [search_and_select_common_user()]
    while True:
        should_continue = console.input("\n [yellow]Deseja adicionar mais um estudante ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
        if should_continue != "s" and should_continue != "S":
            break
        new_student = search_and_select_common_user(excludes=students)
        if new_student is not None:
            students.append(new_student)

    create_turma(name, group_leader, fake_client, students)


def edit_turma():
    console.print("\n [purple]Editar Turma[/purple]")
    console.print()
    turma = search_and_select_turma()

    if turma is None:
        return

    console.print(f"\n [yellow]Nome:[/yellow] {turma['name']}")
    console.print()
    should_update = console.input("\n [yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        turma["name"] = prompt_turma_name("Novo nome: ")

    console.print(f"\n [yellow]Líder do Grupo:[/yellow] {turma['group_leader']['name']}")
    console.print()
    should_update = console.input("\n [yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        turma['group_leader'] = search_and_select_instructor(excludes=[turma['fake_client']])

    console.print(f"\n [yellow]Fake Client:[/yellow] {turma['fake_client']['name']}")
    console.print()
    should_update = console.input("\n [yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        turma['fake_client'] = search_and_select_instructor(excludes=[turma['group_leader']])

    list_members_turma(turma)
    add_student(turma)

    list_members_turma(turma)
    remove_student(turma)

    update_turmas()


def list_members_turma(turma):
    console.print("\n [purple]Estudantes: [/[purple]")
    console.print()
    for student in turma["students"]:
        print(f"    - {summary_student(student)}")


def remove_student(turma):
    while True:
        should_add = console.input("\n [yellow]Deseja remover um estudante ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
        if should_add == "S" or should_add == "s":
            console.print("\n [green]Selecione um Estudante[/green]")
            console.print()
            student_to_remove = search_and_select_common_user()
            if student_to_remove is None:
                continue
            turma["students"].remove(student_to_remove)
        else:
            break

def add_student(turma):
    while True:
        should_add = console.input("\n [yellow]Deseja adicionar mais um estudante ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
        if should_add == "S" or should_add == "s":
            console.print("\n [green]Selecione um Estudante[/green]")
            console.print()
            new_student = search_and_select_common_user(excludes=turma["students"])
            if new_student is None:
                continue
            turma["students"].append(new_student)
        else:
            break

def remove_turma():
    console.print("\n [red]Remover Turma[/red]")
    console.print()
    turma = search_and_select_turma()
    if turma is None:
        return
    delete_turma(turma)


def select_leader_group(leader_id):
    groups = get_turmas_by("group_leader", leader_id, 'id')

    if len(groups) < 1:
        console.print("\n [/bold red]Você não é líder em nenhuma turma[/bold red]")
        console.print()
        return

    console.print("\n [blue]Turmas em que você é líder:[/blue]")
    console.print()

    for index, group in enumerate(groups):
        print(f'    {index + 1}. {group["name"]}')

    input_group = int(bright_input("\nQual turma deseja selecionar? "))

    if input_group > 0 and input_group <= len(groups):
        group = groups[input_group - 1]
        return group
    else:
        console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
        console.print()
        return select_leader_group(leader_id)


def search_and_select_student(turma, excludes=[]):
    search_term = console.input("\n [green]Procurar: [/green]")
    students = search_students(search_term, turma, excludes)

    if len(students) == 0:
        return None

    for index, student in enumerate(students):
        print(f"{index+1} - {summary_student(student)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(students):
            return students[option - 1]
        console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
        console.print()


def menu_list_turmas(user):
    turmas = get_turmas_from_user(user)

    if len(turmas) == 0:
        console.print("\n [bold red]Nenhuma turma encontrada.[/bold red]")
        console.print()
    
    for index, turma in enumerate(turmas):
        print(f"{index+1} - {turma['name']}")


def admin_turmas_menu():
    clear_screen()
    while True:
        console.rule("\n [bold blue]Menu Turmas (Administrador)[/bold blue]")
        console.print("[blue]1 -[/blue] [yellow]Listar[/yellow]")
        console.print("[blue]2 -[/blue] [yellow]Novo[/yellow]")
        console.print("[blue]3 -[/blue] [yellow]Buscar e Detalhar[/yellow]")
        console.print("[blue]4 -[/blue] [yellow]Editar[/yellow]")
        console.print("[blue]5 -[/blue] [yellow]Excluir[/yellow]")
        console.print("[blue]6 -[/blue] [yellow]Voltar[/yellow]")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 6:
                clear_screen()
                break
            console.print("\n :x: [bold red]Opção inválida[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            list_turmas()
        elif option == 2:
            new_turma()
        elif option == 3:
            show_turma()
        elif option == 4:
            edit_turma()
        elif option == 5:
            remove_turma()
        else:
            return
