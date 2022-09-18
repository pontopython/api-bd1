import uuid

from .utils import blue_bright_print, green_print, red_print, bright_print
from .validation import (
    prompt_for_valid_category,
    prompt_for_valid_email,
    prompt_for_valid_password,
    prompt_for_valid_username,
)

USERS_FILE = "data/users.txt"


def create_user_dict(id, category, name, email, password):
    return {
        "id": id,
        "category": category,
        "name": name,
        "email": email,
        "password": password,
    }


def user_dict_to_line(user):
    id = user["id"]
    category = user["category"]
    name = user["name"]
    email = user["email"]
    password = user["password"]

    return f"{id};{category};{name};{email};{password}"


def line_to_user_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    category = splitted_line[1]
    name = splitted_line[2]
    email = splitted_line[3]
    password = splitted_line[4]

    return create_user_dict(id, category, name, email, password)


def create_user_interactively():
    blue_bright_print("\n     Formulário de Criação de Usuário\n")
    id = uuid.uuid4()

    category = prompt_for_valid_category()
    name = prompt_for_valid_username()
    email = prompt_for_valid_email()
    password = prompt_for_valid_password(show=True)
    return create_user_dict(id, category, name, email, password)


def save_user_to_file(user):
    file = open(USERS_FILE, "a")
    line = user_dict_to_line(user)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("\n             Usuário salvo com sucesso!")


def search_user_on_file(email):
    file = open(USERS_FILE, "r")

    for line in file:
        user = line_to_user_dict(line)
        if email == user["email"]:
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
    category = user["category"]
    name = user["name"]
    email = user["email"]

    blue_bright_print(title)
    bright_print(f"         Id: {id}")
    bright_print(f"         Categoria: {category}")
    bright_print(f"         Nome: {name}")
    bright_print(f"         Email: {email}")


def find_and_show_user():
    email = input("         Qual o email do usuário? ")
    user = search_user_on_file(email)

    if user is None:
        red_print("         Usuário não encontrado!")
    else:
        detail_user(user)


def generate_users_list():
    file = open(USERS_FILE, "r")
    users_list = []
    for line in file:
        user = line_to_user_dict(line)
        users_list.append(user)
    file.close()
    return users_list


def list_all_users():
    print("\n----------")
    blue_bright_print("Todos os usuários: \n")
    users_list = generate_users_list()
    for user in users_list:
        name = user["name"]
        email = user["email"]
        category = user["category"]
        print(f"{name} - {email} - {category}")
    print("----------\n")
