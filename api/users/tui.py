<<<<<<< HEAD
from ..utils import safe_int_input, clear_screen
=======
from rich.table import Table

from ..utils import safe_int_input, console
>>>>>>> f0064dce9847383db81c3d6b28dbbcb0f19fd854
from .common import USER_TYPES
from .repository import (
    create_user,
    delete_user,
    get_users,
    get_instructors,
    get_common_users,
    search_users,
    search_instructors,
    search_common_users,
    update_users,
)
from .prompt import prompt_user_email, prompt_user_name, prompt_user_password, prompt_user_type


def summary_user(user):
    name = user["name"]
    email = user["email"]
    type = user["type"]
    type_description = USER_TYPES[type]
    return f"{name} <{email}> ({type_description})"


def detail_user(user, title="Detalhes do Usuário:"):
<<<<<<< HEAD
    clear_screen()
=======
    
>>>>>>> f0064dce9847383db81c3d6b28dbbcb0f19fd854
    id = user["id"]
    name = user["name"]
    email = user["email"]
    type = user["type"]
    type_description = USER_TYPES[type]

    table = Table(title=f"[bold green]{title}")

    table.add_column("Id")
    table.add_column("Nome")
    table.add_column("Email")
    table.add_column("Tipo")

    table.add_row(id, name, email, type_description)
    
    console.print(table)


def list_users():
<<<<<<< HEAD
    clear_screen()
    print("Todos os Usuários:")
=======
    table = Table(title="[bold green]Todos os Usuários")

    table.add_column("Id")
    table.add_column("Nome")
    table.add_column("Email")
    table.add_column("Tipo")

>>>>>>> f0064dce9847383db81c3d6b28dbbcb0f19fd854
    for user in get_users():
        id = user["id"]
        name = user["name"]
        email = user["email"]
        type = user["type"]
        type_description = USER_TYPES[type]
        table.add_row(id, name, email, type_description)
    
    console.print(table)

def list_common_users():
    clear_screen()
    print("Usuários Disponíveis:")
    for user in get_common_users():
        print(f"    - {summary_user(user)}")


def list_instructors():
    clear_screen()
    print("Instrutores:")
    for user in get_instructors():
        print(summary_user(user))


def search_and_select_user():
    clear_screen()
    search_term = input("Procurar: ")
    users = search_users(search_term)

    if len(users) == 0:
        print("Nenhum usuário encontrado.")
        return None


    for index, user in enumerate(users):
        print(f"{index+1} - {summary_user(user)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(users):
            return users[option - 1]
        print("Opção inválida.")

def search_and_select_common_user(excludes=[]):
    clear_screen()
    search_term = input("Procurar: ")
    users = search_common_users(search_term, excludes)

    if len(users) == 0:
        print("Nenhum usuário encontrado.")
        return None


    for index, user in enumerate(users):
        print(f"{index+1} - {summary_user(user)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(users):
            return users[option - 1]
        print("Opção inválida.")


def search_and_select_instructor(excludes=[]):
    clear_screen()
    search_term = input("Procurar Instrutor: ")
    users = search_instructors(search_term, excludes)

    if len(users) == 0:
        print("Nenhum instrutor encontrado.")
        return None

    for index, user in enumerate(users):
        print(f"{index+1} - {summary_user(user)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(users):
            return users[option - 1]
        print("Opção inválida.")


def show_user():
    clear_screen()
    user = search_and_select_user()
    if user is None:
        print("Nenhum usuário encontrado.")
        return
    detail_user(user)


def admin_create_a_new_user():
    clear_screen()
    print("Novo Usuário")
    name = prompt_user_name()
    email = prompt_user_email()
    password = prompt_user_password()
    type = prompt_user_type()

    create_user(name, email, password, type)


def instructor_create_a_new_common_user():
    clear_screen()
    print("Novo Usuário")
    name = prompt_user_name()
    email = prompt_user_email()
    password = prompt_user_password()

    create_user(name, email, password, "COMUM")


def edit_user(user):
    clear_screen()
    if user is None:
        return

    console.print("\n[green]Editar usuário[/green]\n")

    console.print(f"[blue]Nome:[/blue] {user['name']}")
    should_update = console.input("[yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        user["name"] = prompt_user_name("Novo nome: ")

    console.print(f"\n[blue]Email:[/blue] {user['email']}")
    should_update = console.input("[yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        user["email"] = input("Novo e-mail: ")

    console.print(f"\n[blue]Senha:[/blue] ********")
    should_update = console.input("[yellow]Deseja alterar ([/yellow][green]S[/green][yellow]/[/yellow][red]N[/red][yellow])? [/yellow]")
    if should_update == "S" or should_update == "s":
        user["password"] = prompt_user_password()

    update_users()


def admin_edit_user():
    clear_screen()
    user = search_and_select_user()
    edit_user(user)

    type_description = USER_TYPES[user["type"]]
    print(f"Tipo: {type_description}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        user["type"] = prompt_user_type("Qual o novo tipo do usuário?")

    update_users()


def remove_user():
    clear_screen()
    print("Remover usuário")
    user = search_and_select_user()
    if user is None:
        print("Nenhum usuário encontrado.")
        return
    delete_user(user)


def admin_users_menu():
    clear_screen()
    while True:
        print("Menu Usuários (Administrador)")
        print("1 - Listar")
        print("2 - Novo")
        print("3 - Buscar e Detalhar")
        print("4 - Editar")
        print("5 - Excluir")
        print("6 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 6:
                break
            print("Opção inválida.")

        if option == 1:
            list_users()
        elif option == 2:
            admin_create_a_new_user()
        elif option == 3:
            show_user()
        elif option == 4:
            admin_edit_user()
        elif option == 5:
            remove_user()
        else:
            return

def LG_users_menu():
    clear_screen()
    while True:
        print("Menu Usuários ")
        print("1 - Listar")
        print("2 - Novo")
        print("3 - Buscar e Detalhar")
        print("4 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 6:
                break
            print("Opção inválida.")

        if option == 1:
            list_users()
        elif option == 2:
            instructor_create_a_new_common_user()
        elif option == 3:
            show_user()
        else:
            return
