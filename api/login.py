import stdiomask

from .users import line_to_user_dict
from .utils import bright_print


# Formulário_Login
def login_user():
    bright_print("\nLogin do Usuário\n")
    login = input("Usuário:")
    password = stdiomask.getpass(prompt="Senha:", mask="*")

    return login, password


# Verificação_Existência_Usuário_Na_Base
def search_user_by_email(login):
    file = open("data/users.txt", "r")
    ver = False

    while ver != True:

        for line in file:
            user = line_to_user_dict(line)

            if login == user["email"]:
                return user

        break
    file.close()

    return


# Validação_das_Credenciais
def Credential_Validation(user, password):

    if (
        user is not None and password == user["name"]
    ):  ## ERRO na comparaçao com user['password']**********
        print("ok")  # *****TESTE*****

    else:
        print("Credenciais Inválidas!")


# Registro_do_Log
def access_log(user):
    file = open("data/register_log.txt," "a")


if __name__ == "__main__":

    login, password = login_user()
    user = search_user_by_email(login)
    Credential_Validation(user, password)
