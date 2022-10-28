import re

import stdiomask

from .utils import bright_print, red_print, bright_input


def has_name_valid_characters(name):
    "Verifica se tem caracteres especiais."
    return re.match("^[a-zA-Z0-9_-]+$", name)


def is_name_valid(name, show=False):
    """
    Retorna True ou False. Verifica se o nome é valido ou não.
    Validações:
        - deve conter mais de 2 caracteres
        - não pode começar com número
        - não pode conter caracteres especiais, exceto underline "_"
    """
    if len(name) <= 2:
        if show == True:
            red_print(
                "        O nome deve ter mais de 2 caracteres. Tente novamente!")
        return False
    elif not has_name_valid_characters(name):
        if show == True:
            red_print("        Formato inválido. Tente novamente!")
        return False
    elif re.match("\d", name[0]):
        if show == True:
            red_print("        Nomes não podem começar com número")
        return False
    else:
        return True


def prompt_for_valid_username(change=False):
    """
    Loop pedindo para o usuário inserir o nome caso
    o nome seja inválido.
    """
    message = "\tDigite o novo nome para o usuário: " if change else "\tDigite o nome do usuário: "
    input_name = input(message)

    while not is_name_valid(input_name, True):
        input_name = input("\tDigite um nome para usuário válido: ")

    return input_name


def is_email_valid(email):
    return re.match("^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$", email)


def prompt_for_valid_email():
    input_email = input("\t Digite o email: ")

    while not is_email_valid(input_email):
        red_print("\t E-mail inválido. Digite novamente!")
        input_email = input("        Digite o e-mail: ")

    return input_email


def prompt_for_valid_team_name(change=False):
    message = "     Digite um novo nome para o time: " if change else "     Digite o nome do time: "
    input_team_name = input(message)

    while not is_name_valid(input_team_name):
        input_team_name = input("\tDigite um nome válido para o time: ")

    return input_team_name


def has_password_valid_characters(password):
    return re.match(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password
    )


def is_password_valid(password, show=False):
    """
    \n Retorna True ou False. Verifica se a senha é valida ou não.
        Validações:
            - deve conter mais de 8 caracteres
            - deve conter pelo menos 1 letra maiúscula
            - deve conter pelo menos 1 letra minúscula
            - deve conter pelo menos 1 número
            - deve conter pelo menos 1 carácter especial (@!%*?&)
    """
    if len(password) < 8:
        if show == True:
            red_print("\tA senha deve ter mais de 8 caracteres.")
        return False
    elif not has_password_valid_characters(password):
        if show == True:
            red_print("\tFormato inválido!")
        return False
    else:
        return True


def prompt_for_valid_password(show=False):
    """
    Loop pedindo para o usuário inserir a senha caso
    ela seja inválida.
    """
    if show == True:
        bright_print(
            """
        Sua senha deve conter:
            No mínimo 8 caracteres
            No mínimo 1 letra maiúscula
            No mínimo 1 letra minúscula
            No mínimo 1 número
            No mínimo 1 carácter especial (@!%*?&)
        """)

    input_password = stdiomask.getpass(
        prompt="        Digite a senha: ", mask="*")

    while not is_password_valid(input_password, show):
        input_password = stdiomask.getpass(
            prompt="        Digite uma senha válida: ", mask="*")

    return input_password


def prompt_for_valid_option(question, options):
    bright_print(f"    {question}")

    descriptions = options.values()

    for index, description in enumerate(descriptions):
        bright_print(f"        {index} - {description}")

    option = int(bright_input("    Opção: "))
    while option >= len(descriptions) or option < 0:
        red_print("        Você digitou uma opção inválida, tente novamente.")
        option = int(bright_input("    Opção: "))

    keys = list(options.keys())

    return keys[option]

def prompt_for_valid_category_admin():
    categories = {0: "AD", 1: "MT", 2: "LG", 3: "FC"}

    bright_print(
        """
     Qual a categoria do usuário?
         0 - Administrador
         1 - Membro do Time
         2 - Líder do Grupo
         3 - Fake Client
        """
    )

    option = int(input("     Opção: "))
    while option > 3 or option < 0:
        red_print("         Você digitou uma opção inválida, tente novamente.")
        option = int(input("     Opção: "))

    return categories[option]


def prompt_for_user_search_type(options):

    bright_print(
        """
     Buscar usuário por :
         1 - Nome
         2 - Email
         """
    )

    option = int(input("     Opção: "))
    while option > 2 or option < 1:
        red_print("         Você digitou uma opção inválida, tente novamente.")
        option = int(input("     Opção: "))

    return options[option]


def prompt_for_confirmation(question):

    bright_print(question)
    response = int(input("     Opção: "))

    while response > 2 or response < 1:
        red_print("         Você digitou uma opção inválida, tente novamente.")
        response = int(input("     Opção: "))

    return response == 1


def prompt_for_edit_team_search_type(options):

    bright_print(
        """
     Escolha a opção desejada :
         1 - Alterar nome do time
         2 - Adicionar novo usuário
         3 - Excluir um usuário
         4 - Mudar categoria do usuário
         """
    )

    option = int(input("     Opção: "))
    while option > 4 or option < 1:
        red_print("         Você digitou uma opção inválida, tente novamente.")
        option = int(input("     Opção: "))

    return options[option]


def prompt_for_edit_user_search_type(options):

    bright_print(
        """
     Escolha a opção desejada :
         1 - Alterar nome do usuário
         2 - Alterar categoria do usuário

         """
    )

    option = int(input("     Opção: "))
    while option > 4 or option < 1:
        red_print("         Você digitou uma opção inválida, tente novamente.")
        option = int(input("     Opção: "))

    return options[option]
