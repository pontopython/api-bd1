import uuid

from .utils import (blue_bright_print, green_print, red_print, bright_print)
from .validation import (
    prompt_for_valid_category,
    prompt_for_valid_email,
    prompt_for_valid_password,
    prompt_for_valid_username,
    prompt_for_user_search_type,
    prompt_for_confirmation
)

USERS_FILE = "data/users.txt"
LOGIN_FILE = "data/login.txt"


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
    category = user["category"]
    name = user["name"]
    email = user["email"]

    blue_bright_print(title)
    bright_print(f"         Id: {id}")
    bright_print(f"         Categoria: {category}")
    bright_print(f"         Nome: {name}")
    bright_print(f"         Email: {email}")


def find_and_show_user():
    options = {
        1: find_by_name, 
        2: find_by_email
    }
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
    name = input("         Qual o nome do usuário? ")
    user = search_user_on_file_by_name(name)
    return user


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


##### edição de usuário #####
#def change_line_edit_user():
#    open(USERS_FILE, "r") 
#    
#######


def find_and_delete_user():
    options = {
        1: find_by_name, 
        2: find_by_email
    }
    option = prompt_for_user_search_type(options)
    user = option()
   
    if user is None:
        red_print("\n         Usuário não encontrado!")
    else:
        login_file = open(LOGIN_FILE, 'r')
        login_lines = login_file.readlines()
        if login_lines[0] == user["id"]:
            red_print("\n         O usuário não pode excluir ele mesmo.")
            return

        with open(USERS_FILE, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                file_user = line_to_user_dict(line)
                if user["id"] == file_user["id"]:
                    username = user["name"]
                    bright_print(f"\n             Usuário {username} encontrado!")

                    confirmation = prompt_for_confirmation (f"""
                    Tem certeza que gostaria de excluir o usuário {username}?
                    1 - Sim
                    2 - Não
                    """)
                    if confirmation:
                        lines.pop(index)
                        write_file = open(USERS_FILE, 'w')
                        write_file.writelines(lines)
                        file.close()
                        write_file.close()
                        green_print(f"\n             Usuário excluído com sucesso!")
                    
                    break
                    

        






