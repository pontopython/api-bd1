from utils import green_print, red_print, blue_bright_print, cyan_print, yellow_print, magenta_print, bright_print
import stdiomask
import uuid


def create_user_dict(id, category, name, email, password):
    return {
        "id": id,
        "category": category,
        "name": name,
        "email": email,
        "password": password
    }


def user_dict_to_line(user):
    id = user["id"]
    category = user["category"]
    name = user["name"]
    email = user["email"]
    password = user["password"]

    return f"{id};{category};{name};{email};{password}"


def line_to_user_dict(line):
    splited_line = line.split(";")
    id = splited_line[0]
    category = splited_line[1]
    name = splited_line[2]
    email = splited_line[3]
    password = splited_line[4]
    

    return create_user_dict(id, category, name, email, password)


def create_user_interactively():
    blue_bright_print("\nFormulário de Criação de Usuário\n")
    id = uuid.uuid4()

    options = {
        0: 'PO',
        1: 'LT',
        2: 'LG',
        3: 'FC',
        4: 'MT'
    }

    bright_print('''Qual a categoria do usuário?
    [0] - PO
    [1] - Líder Técnico
    [2] - Líder do Grupo
    [3] - Fake Cliente
    [4] - Membro do Time''')

    category = prompt_for_valid_category()
    name = input("Nome: ")
    email = input("Digite o E-mail: ")
    password = stdiomask.getpass(prompt="Digite a senha: ", mask="*")
    return create_user_dict(id, options[category], name, email, password)


def prompt_for_valid_category():
    category = int(input(""))
    if category > 4 or category < 0:
        red_print('Você digitou uma opção inválida, tente novamente.')
        return prompt_for_valid_category()
    return category


def save_user_to_file(user):
    file = open("data/users.txt", "a")
    line = user_dict_to_line(user)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("Usuário salvo com sucesso!")


if __name__ == "__main__":
    user = create_user_interactively()
    save_user_to_file(user)
