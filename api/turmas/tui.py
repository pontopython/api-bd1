from ..utils import blue_bright_print, bright_input, red_print, safe_int_input, clear_screen
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
    clear_screen()
    id = turma["id"]
    name = turma["name"]
    group_leader_name = turma["group_leader"]["name"]
    group_leader_email = turma["group_leader"]["email"]
    fake_client_name = turma["fake_client"]["name"]
    fake_client_email = turma["fake_client"]["email"]
    students_count = len(turma["students"])
    students = turma["students"]
    count = 0

    print(title)
    print(f"Id: {id}")
    print(f"Nome: {name}")
    print(f"Líder de Grupo: {group_leader_name} <{group_leader_email}>")
    print(f"Fake Client: {fake_client_name} <{fake_client_email}>")
    print(f"Total de Alunos: {students_count}")
    while count < len(students):
        aluno = students[count]
        print(f"Aluno: {aluno['name']}")
        count += 1


def list_turmas():
    print("Turmas:")
    for turma in get_turmas():
        print(f"    - {summary_turma(turma)}")


def search_and_select_turma():
    search_term = input("Procurar: ")
    turmas = search_turmas(search_term)

    if len(turmas) == 0:
        print("Nenhuma turma encontrada.")
        return None

    for index, turma in enumerate(turmas):
        print(f"{index+1} - {summary_turma(turma)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(turmas):
            return turmas[option - 1]
        print("Opção inválida.")


def select_turma_from_user(user):
    turmas = get_turmas_from_user(user)

    if len(turmas) == 0:
        print("Nenhuma turma encontrada.")
        return None

    if len(turmas) == 1:
        return turmas[0]

    for index, turma in enumerate(turmas):
        print(f"{index+1} - {summary_turma(turma)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(turmas):
            return turmas[option - 1]
        print("Opção inválida.")


def show_turma():
    turma = search_and_select_turma()
    if turma is None:
        return
    detail_turma(turma)


def new_turma():
    print("Nova Turma")
    name = prompt_turma_name()

    print("Selecione um Líder de Grupo")
    group_leader = search_and_select_instructor()
    while group_leader is None:
        group_leader = search_and_select_instructor()
    print("Líder do Grupo selecionado")

    print("Selecione um Fake Client")
    fake_client = search_and_select_instructor(excludes=[group_leader])
    while fake_client is None:
        fake_client = search_and_select_instructor(excludes=[group_leader])
    print("Fake Client selecionado")

    list_common_users()
    print("Selecione os estudantes:")
    students = [search_and_select_common_user()]
    while True:
        should_continue = input("Deseja adicionar mais um estudante (S/N)? ")
        if should_continue != "s" and should_continue != "S":
            break
        new_student = search_and_select_common_user(excludes=students)
        if new_student is not None:
            students.append(new_student)

    create_turma(name, group_leader, fake_client, students)


def edit_turma():
    print("Editar Turma")
    turma = search_and_select_turma()

    if turma is None:
        return

    print(f"Nome: {turma['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma["name"] = prompt_turma_name("Novo nome: ")

    print(f"Líder do Grupo: {turma['group_leader']['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma['group_leader'] = search_and_select_instructor(excludes=[turma['fake_client']])

    print(f"Fake Client: {turma['fake_client']['name']}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        turma['fake_client'] = search_and_select_instructor(excludes=[turma['group_leader']])

    list_members_turma(turma)
    add_student(turma)

    list_members_turma(turma)
    remove_student(turma)

    update_turmas()


def list_members_turma(turma):
    print("Estudantes: ")
    for student in turma["students"]:
        print(f"    - {summary_student(student)}")


def remove_student(turma):
    while True:
        should_add = input("Deseja remover um estudante (S/N)? ")
        if should_add == "S" or should_add == "s":
            print("Selecione um Estudante")
            student_to_remove = search_and_select_common_user()
            if student_to_remove is None:
                continue
            turma["students"].remove(student_to_remove)
        else:
            break

def add_student(turma):
    while True:
        should_add = input("Deseja adicionar mais um estudante (S/N)? ")
        if should_add == "S" or should_add == "s":
            print("Selecione um Estudante")
            new_student = search_and_select_common_user(excludes=turma["students"])
            if new_student is None:
                continue
            turma["students"].append(new_student)
        else:
            break

def remove_turma():
    print("Remover Turma")
    turma = search_and_select_turma()
    if turma is None:
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


def search_and_select_student(turma, excludes=[]):
    search_term = input("Procurar: ")
    students = search_students(search_term, turma, excludes)

    if len(students) == 0:
        return None

    for index, student in enumerate(students):
        print(f"{index+1} - {summary_student(student)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(students):
            return students[option - 1]
        print("Opção inválida.")


def menu_list_turmas(user):
    turmas = get_turmas_from_user(user)

    if len(turmas) == 0:
        print("Nenhuma turma encontrada.")
    
    for index, turma in enumerate(turmas):
        print(f"{index+1} - {turma['name']}")


def admin_turmas_menu():
    clear_screen()
    while True:
        print("Menu Turmas (Administrador)")
        print("1 - Listar")
        print("2 - Novo")
        print("3 - Buscar e Detalhar")
        print("4 - Editar")
        print("5 - Excluir")
        print("6 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            clear_screen()
            if option >= 1 and option <= 6:
                break
            print("Opção inválida.")

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
