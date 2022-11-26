from ..utils import safe_int_input
from ..turmas.tui import search_and_select_turma
from .repository import get_all_sprints_from_group, create_sprint, get_opened_sprint_from_group, update_sprints


def summary_sprint(sprint):
    name = sprint["name"]
    id = sprint["id"]
    status = sprint["status"]
    return f"{name} #{id} ({status})"


def show_sprints_from_group(group):
    sprints = get_all_sprints_from_group(group)
    print("Sprints")
    for sprint in sprints:
        print(f"    - {summary_sprint(sprint)}")


def has_group_opened_sprint(group):
    opened_sprints = get_opened_sprint_from_group(group)
    return opened_sprints is not None


def open_sprint_for_group(group):
    if has_group_opened_sprint(group):
        print("Já existe uma sprint aberta.")
        return
    sprint_name = input('Qual o nome da sprint? ')
    create_sprint(group, sprint_name)


def close_sprint_from_group(group):
    if not has_group_opened_sprint(group):
        print("Não existe sprint aberta.")
        return
    sprint = get_opened_sprint_from_group(group)
    print(summary_sprint(sprint))
    answer = input("Tem certeza que deseja fechar essa sprint (S/N)? ")
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
        print("Nenhuma sprint encontrada.")
        return None

    for index, sprint in enumerate(valid_sprints):
        print(f"{index+1} - {summary_sprint(sprint)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(sprints):
            return valid_sprints[option - 1]
        print("Opção inválida.")


def reopen_sprint_from_group(group):
    if has_group_opened_sprint(group):
        print("Já existe uma sprint aberta.")
        return
    sprint = select_sprint_from_group(group)

    if sprint is None:
        return

    print(summary_sprint(sprint))
    answer = input("Tem certeza que deseja reabrir essa sprint (S/N)? ")
    if answer != "S" and answer != "s":
        return
    sprint["status"] = "aberta"
    update_sprints()


def admin_and_LG_sprints_menu(turma=None):
    if turma is None:
        print("Selecione a Turma")
        turma = search_and_select_turma()

    if turma is None:
        print("Nenhuma turma encontrada.")
        return

    while True:
        print("Menu Sprints (Administrador)")
        print(f"Turma: {turma['name']}")
        print("1 - Listar")
        print("2 - Abrir Nova")
        print("3 - Fechar")
        print("4 - Reabrir")
        print("5 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 6:
                break
            print("Opção inválida.")

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
