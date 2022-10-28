import uuid

from .utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    cyan_print,
    green_print,
    red_print,
)
from .validation import (
    prompt_for_confirmation,
    prompt_for_edit_user_search_type,
    prompt_for_user_search_type,
    prompt_for_valid_email,
    prompt_for_valid_password,
    prompt_for_valid_username,
    prompt_for_valid_option,
)

USERS_FILE = "data/users.txt"
LOGIN_FILE = "data/login.txt"

USER_TYPES = {
    "ADMIN": "Administrador",
    "LIDER": "Líder de Turma",
    "FAKEC": "Fake Client",
    "COMUM": "Comum",
}


def create_user_dict(id, name, email, password, type):
    return {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "type": type,
    }


def user_dict_to_line(user):
    id = user["id"]
    name = user["name"]
    email = user["email"]
    password = user["password"]
    type = user["type"]

    return f"{id};{name};{email};{password};{type}"


def line_to_user_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    email = splitted_line[2]
    password = splitted_line[3]
    type = splitted_line[4]

    return create_user_dict(id, name, email, password, type)


def create_user_interactively():
    blue_bright_print("\n\tFormulário de Criação de Usuário\n")
    id = uuid.uuid4()

    name = prompt_for_valid_username()
    email = prompt_for_valid_email()
    password = prompt_for_valid_password(show=True)
    type = prompt_for_valid_option("Selecione o tipo do usuário:", USER_TYPES)
    user = create_user_dict(id, name, email, password, type)
    save_user_to_file(user)


def save_user_to_file(user):
    file = open(USERS_FILE, "a")
    line = user_dict_to_line(user)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("\n\tUsuário salvo com sucesso!")


def find_user_line_number_on_file(user):
    id = user["id"]
    file = open(USERS_FILE, "r")  # abre arquivo dos usuários para leitura
    lines = file.readlines()
    for line_number, line in enumerate(lines):  # enumera cada linha do arquivo
        line_user = line_to_user_dict(line)  # procura um time com mesmo id
        if (
            line_user["id"] == id
        ):  # se o id da linha for o mesmo do time , retorna o numero da linha
            file.close()
            return line_number
    file.close()
    return None


def remove_user_from_file(user):
    read_file = open(USERS_FILE, "r")  # abre arquivo para leitura
    lines = read_file.readlines()  # cria lista com as linhas
    read_file.close()
    line_number = find_user_line_number_on_file(user)  # encontra a linha do usuário
    lines.pop(line_number)  # remove a linha do usuário da lista
    write_file = open(USERS_FILE, "w")  # abre arquivo para escrita
    write_file.writelines(lines)  # escreve as linhas
    write_file.close()  # fecha o arquivo


def update_user_on_file(user):
    remove_user_from_file(user)
    save_user_to_file(user)


def search_user_on_file_by_email(email):
    file = open(USERS_FILE, "r")

    for line in file:
        user = line_to_user_dict(line)
        if email.lower() == user["email"].lower():
            file.close()
            return user

    file.close()
    return None


def search_user_on_file_by_name(name):
    file = open(USERS_FILE, "r")

    for line in file:
        user = line_to_user_dict(line)
        if name.lower() == user["name"].lower():
            file.close()
            return user

    file.close()
    return None


def search_user_on_file_by_id(id):
    file = open(USERS_FILE, "r")

    for line in file:
        user = line_to_user_dict(line)
        if id == user["id"]:
            file.close()
            return user

    file.close()
    return None


def detail_user(user, title="\n     Detalhes do Usuário"):
    id = user["id"]
    name = user["name"]
    email = user["email"]
    type = user["type"]
    type_description = USER_TYPES[type]

    blue_bright_print(title)
    bright_print(f"         Id: {id}")
    bright_print(f"         Nome: {name}")
    bright_print(f"         Email: {email}")
    bright_print(f"         Tipo: {type_description}")


def find_and_show_user():
    options = {1: find_by_name, 2: find_by_email}
    option = prompt_for_user_search_type(options)
    user = option()
    if user is None:
        red_print("         Usuário não encontrado!")
    else:
        detail_user(user)


def find_by_email():
    email = input("         Qual o email do usuário? ")
    user = search_user_on_file_by_email(email)
    return user


def find_by_name():
    name = bright_input("\n     Qual o nome do usuário? ")
    user = search_user_on_file_by_name(name)
    return user


def create_users_list():
    file = open(USERS_FILE, "r")
    users_list = []
    for line in file:
        user = line_to_user_dict(line)
        users_list.append(user)
    file.close()
    return users_list

# CRIA LISTAS DE USUÁRIOS BASEADAS NO ATRIBUTO E NO VALOR, DIRETO DO DICT DO USUÁRIO
def create_users_list_dynamic(attribute, value):
    file = open(USERS_FILE, "r")
    list = []
    for line in file:
        user = line_to_user_dict(line)
        if value == user[f"{attribute}"]:
            list.append(user)
    file.close()
    return list


def list_all_users():
    print("\n----------")
    blue_bright_print("Todos os usuários: \n")
    users_list = create_users_list()
    for user in users_list:
        name = user["name"]
        email = user["email"]
        type = user["type"]
        type_description = USER_TYPES[type]
        print(f"{name} - {email} - {type_description}")
    print("----------\n")


def find_and_delete_user():
    options = {1: find_by_name, 2: find_by_email}
    option = prompt_for_user_search_type(options)
    user = option()

    if user is None:
        red_print("\n         Usuário não encontrado!")
    else:
        login_file = open(LOGIN_FILE, "r")
        login_lines = login_file.readlines()
        if login_lines[0] == user["id"]:
            red_print("\n         O usuário não pode excluir ele mesmo.")
            return

        with open(USERS_FILE, "r") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                file_user = line_to_user_dict(line)
                if user["id"] == file_user["id"]:
                    username = user["name"]
                    cyan_print(f"\n\t\tUsuário {username} encontrado!")

                    confirmation = prompt_for_confirmation(
                        f"""
                    Tem certeza que gostaria de excluir o usuário {username}?
                    1 - Sim
                    2 - Não
                    """
                    )
                    if confirmation:
                        lines.pop(index)
                        write_file = open(USERS_FILE, "w")
                        write_file.writelines(lines)
                        file.close()
                        write_file.close()
                        green_print(f"\n             Usuário excluído com sucesso!")

                    break


def change_user_name():
    user = find_user_interactively()
    if user is None:
        red_print("\n         Usuário não encontrado!")
        return
    else:
        user_name = user["name"]
        cyan_print(f"\n\t\tUsuário {user_name} encontrado!")
        user["name"] = prompt_for_valid_username()
        update_user_on_file(user)

# REPENSAR

# def change_user_category_on_team():
#     cyan_print("\n\tPesquise o usuário para adicionar a categoria")
#     user = find_by_name()
#     if user is None:
#         red_print("\n\tUsuário não encontrado! Tente novamente\n")
#         user = find_by_name()
#         return
#     else:
#         user_name = user["name"]
#         green_print(f"\n\tUsuário {user_name} encontrado!")
#         user["category"] = prompt_for_valid_category()
#         update_user_on_file(user)
#     while True:
#         asking = bright_input(
#             "\n     Deseja mudar a categoria de mais algum usuário do time? "
#         ).lower()
#         if asking == "n" or asking == "nao" or asking == "não":
#             break
#         while asking == "s" or asking == "sim":
#             user = find_by_name()
#             user_name = user["name"]
#             green_print(f"\n\tUsuário {user_name} encontrado!")
#             user["category"] = prompt_for_valid_category()
#             update_user_on_file(user)
#             asking = bright_input(
#                 "\n     Deseja mudar a categoria de mais algum usuário do time? "
#             ).lower()
#         return


# def edit_user_category_on_team():
#     cyan_print("\n\tPesquise o usuário para mudar a categoria")
#     user = find_by_name()
#     if user is None:
#         red_print("\n\tUsuário não encontrado! Tente novamente\n")
#         user = find_by_name()
#         return
#     else:
#         user_name = user["name"]
#         green_print(f"\n\tUsuário {user_name} encontrado!")
#         user["category"] = prompt_for_valid_all_category()
#         update_user_on_file(user)
#     while True:
#         asking = bright_input(
#             "\n     Deseja mudar a categoria de mais algum usuário do time? "
#         ).lower()
#         if asking == "n" or asking == "nao" or asking == "não":
#             break
#         while asking == "s" or asking == "sim":
#             user = find_by_name()
#             user_name = user["name"]
#             green_print(f"\n\tUsuário {user_name} encontrado!")
#             user["category"] = prompt_for_valid_all_category()
#             update_user_on_file(user)
#             asking = bright_input(
#                 "\n     Deseja mudar a categoria de mais algum usuário do time? "
#             ).lower()
#         return


def edit_user():
    options = {1: change_user_name}
    option = prompt_for_edit_user_search_type(options)
    edit = option()

    if edit == 1:
        change_user_name()


def select_user_interactively(users):
    bright_print("Selecione um usuários abaixo: ")
    for index, user in enumerate(users):
        name = user["name"]
        email = user["email"]
        type = user["type"]
        type_description = USER_TYPES[type]
        bright_print(f"{index} - {name} <{email}> ({type_description})")

    option = int(bright_input("    Opção: "))
    while option >= len(users) or option < 0:
        red_print("        Você digitou uma opção inválida, tente novamente.")
        option = int(bright_input("    Opção: "))

    return users[option]


def find_user_interactively():
    filtered_users = []
    all_users = create_users_list()

    search_text = input("Digite alguma do usuário ai: ")

    for user in all_users:
        type_description = USER_TYPES[user["type"]]
        if (
            search_text.lower() in user["name"].lower()
            or search_text.lower() in user["email"].lower()
            or search_text.lower() in type_description.lower()
            or search_text == user["id"]
        ):
            filtered_users.append(user)

    return select_user_interactively(filtered_users)
