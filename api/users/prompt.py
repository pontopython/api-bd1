import stdiomask
from rich import print
from rich.panel import Panel

from ..utils import safe_int_input, console 
from .common import USER_TYPES
from .validation import validate_user_email, validate_user_name, validate_user_password


def prompt_user_name(prompt="Nome: "):
    while True:
        name = input(prompt)
        valid, errors = validate_user_name(name)

        if valid:
            return name

        for error in errors:
            print(error)

def prompt_user_email(prompt="Email: "):
    while True:
        print(f":e-mail: {prompt}", end="")
        email = input()
        valid, errors = validate_user_email(email)

        if valid:
            return email

        for error in errors:
            print(error)

def prompt_user_password():
    console.print("""Sua senha deve conter:
            [yellow]No mínimo 8 caracteres[/yellow]
            [yellow]No mínimo 1 letra maiúscula[/yellow]
            [yellow]No mínimo 1 letra minúscula[/yellow]
            [yellow]No mínimo 1 número[/yellow]
            [yellow]No mínimo 1 carácter especial (@!%*?&)[/yellow]""")

    while True:
        password = stdiomask.getpass(prompt="Senha: ", mask="*")
        valid, errors = validate_user_password(password)

        if valid:
            return password

        for error in errors:
            print(error)


def prompt_user_type(prompt="Qual tipo de usuário?"):
    while True:
        console.rule(f"\n[bold blue]{prompt}[/bold blue]")
        console.print("[blue]1 -[/blue] Administrador")
        console.print("[blue]2 -[/blue] Instrutor")
        console.print("[blue]3 -[/blue] Usuário Comum")
        option = safe_int_input("\nOpção: ")

        if option in [1, 2, 3]:
            return list(USER_TYPES.keys())[option - 1]

        console.print(":x: [bold red]Opção inválida[/bold red] :x:\n", justify= "center")
