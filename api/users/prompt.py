from .common import USER_TYPES
from .validation import validate_user_name, validate_user_password
import stdiomask


def prompt_user_name(prompt="Nome: "):
    while True:
        name = input(prompt)
        valid, errors = validate_user_name(name)

        if valid:
            return name

        for error in errors:
            print(error)


def prompt_user_password():
    print("""Sua senha deve conter:
            No mínimo 8 caracteres
            No mínimo 1 letra maiúscula
            No mínimo 1 letra minúscula
            No mínimo 1 número
            No mínimo 1 carácter especial (@!%*?&)""")
    
    while True:
        password = input(stdiomask.getpass(
        prompt="Senha: ", mask="*"))
        valid, errors = validate_user_password(password)

        if valid:
            return password

        for error in errors:
            print(error)


def prompt_user_type(prompt="Qual tipo de usuário?"):
    while True:
        print(prompt)
        print("1 - Administrador")
        print("2 - Usuário Comum")
        option = int(input())

        if option in [1, 2]:
            return list(USER_TYPES.keys())[option - 1]

        print("Opção inválida")
