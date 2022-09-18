import stdiomask

from .users import detail_user, search_user_on_file, search_user_on_file_by_id
from .utils import bright_input, cyan_print, red_print

LOGIN_FILE = "data/login.txt"


def prompt_for_user_credentials():
    cyan_print("\n     Login do Usuário\n")
    email = bright_input("        Email: ")
    password = stdiomask.getpass(prompt="        Senha: ", mask="*")

    return email, password


def is_user_credentials_valid(email, password, show_errors=False):
    user = search_user_on_file(email)

    if user is None:
        if show_errors:
            red_print("         Não foi encontrado um usuário com este e-mail.")
        return False

    correct_password = user["password"]
    if password != correct_password:
        if show_errors:
            red_print("         Senha incorreta.")
        return False

    return True


def save_user_id_on_login_file(id):
    file = open(LOGIN_FILE, "w")
    file.write(id)
    file.close()


def get_logged_user_id_from_file():
    file = open(LOGIN_FILE, "r")
    lines = file.readlines()
    if len(lines) > 0:  # verifica se tem pelo menos um usuário logado
        id_line = lines[0]
        id = id_line.rstrip("\n")
        return id
    else:
        return None


def get_logged_user():
    id = get_logged_user_id_from_file()
    return search_user_on_file_by_id(id)


def login_user():
    email, password = prompt_for_user_credentials()
    if is_user_credentials_valid(email, password):
        user = search_user_on_file(email)
        save_user_id_on_login_file(user["id"])
    else:
        red_print("         Credenciais inválidas! Tente Novamente.")


def logout_user():
    file = open(LOGIN_FILE, "w")
    file.write("")
    file.close()


def show_profile():
    user = get_logged_user()
    print("\n----------")
    detail_user(user, title="Meu Perfil")
    print("----------\n")
