# from api.users.repository import
from api.utils import blue_bright_print, bright_input, red_print
from .repository import delete_turma, get_turmas, search_turmas, create_turma, delete_turma, get_turmas_by
from .prompt import prompt_turma_name
from ..users.tui import search_and_select_instructor, search_and_select_user


def summary_turma(turma):
    name = turma["name"]
    students_count = len(turma["students"])
    return f"    - {name} ({students_count} alunos)"


def detail_turma(turma, title="Detalhes da Turma:"):
    id = turma["id"]
    name = turma["name"]
    group_leader_name = turma["group_leader"]["name"]
    group_leader_email = turma["group_leader"]["email"]
    fake_client_name = turma["fake_client"]["name"]
    fake_client_email = turma["fake_client"]["email"]
    students_count = len(turma["students"])

    print(title)
    print(f"Id: {id}")
    print(f"Nome: {name}")
    print(f"Líder de Grupo: {group_leader_name} <{group_leader_email}>")
    print(f"Fake Client: {fake_client_name} <{fake_client_email}>")
    print(f"Total de Alunos: {students_count}")
    print(f"Times: ")
    for team in turma["teams"]:
        team_name = team["name"]
        members_count = len(team["members"])
        print(f"    - {team_name} ({members_count} membros)")


def list_turma():
    print("Turmas:")
    for user in get_turmas():
        print(summary_turma)


def search_and_select_turma():
    search_term = input("Procurar: ")
    turmas = search_turmas(search_term)

    if len(turmas) == 0:
        return None

    for index, user in enumerate(turmas):
        print(f"{index+1} - {summary_turma(user)}")

    while True:
        option = int(input("Opção: "))
        if option > 0 and option <= len(turmas):
            return turmas[option - 1]
        print("Opção inválida.")


def show_turma():
    turma = search_and_select_turma()
    if turma is None:
        print("Nenhuma turma encontrada.")
        return
    detail_turma


def new_turma():
    print("Nova Turma")
    name = prompt_turma_name()

    print("Selecione um Líder de Grupo")
    group_leader = search_and_select_instructor()
    while group_leader is None:
        group_leader = search_and_select_instructor()
        print("Líder do Grupo selecionado")

    print("Selecione um Fake Client")
    fake_client = search_and_select_instructor()
    while fake_client is None:
        fake_client = search_and_select_instructor()
        print("Fake Client selecionado")

    students = [search_and_select_user()]
    teams = []

    create_turma(name, group_leader, fake_client, students, teams)


def edit_turma():
    print("Editar Turma")
    turma = search_and_select_turma()

    if turma is None:
        print("Nenhuma turma encontrada.")
        return

    print(f"Nome: {turma['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma["name"] = prompt_turma_name("Novo nome: ")

    print(f"Líder do Grupo: {turma['group_leader']['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma['group_leader']['name'] = search_and_select_user()

    print(f"Fake Client: {turma['fake_client']['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma['fake_client']['name'] = search_and_select_user()


def remove_turma():
    print("Remover Turma")
    turma = search_and_select_turma()
    if turma is None:
        print("Nenhuma turma encontrada.")
        return
    delete_turma(turma)

def select_leader_group(leader_id):
    groups = get_turmas_by("group_leader", leader_id, 'id')

    if len(groups) < 1:
        red_print("Você não é líder em nenhuma turma")
        return

    blue_bright_print("\n     Turmas em que você é líder:")

    for index, group in enumerate(groups):
        print(f'    {index + 1}. {group["name"]}')

    input_group = int(bright_input("\nQual turma deseja selecionar? "))

    if input_group > 0 and input_group <= len(groups):
        group = groups[input_group - 1]
        return group
    else:
        red_print("Opção inválida. Tente novamente!")
        return select_leader_group(leader_id)
