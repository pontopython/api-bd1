from validation import is_name_valid

from repository import create_alunos_list

from users import select_user_interactively

from utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    cyan_print,
    green_print,
    red_print,
)

def prompt_for_valid_turma_name(change=False):
    """
    Loop pedindo para o usuário inserir o nome caso
    o nome seja inválido.
    """
    message = "\tDigite o novo nome para a turma: " if change else "\tDigite o nome da turma: "
    input_name = input(message)

    while not is_name_valid(input_name, True):
        input_name = input("\tDigite um nome de turma válido: ")

    return input_name

def prompt_for_alunos():
    alunos = []

    while True:
        bright_print("\n     Adicionar Aluno")
        aluno = select_user_interactively(create_alunos_list())
        alunos.append(aluno)

        asking = bright_input("\n     Deseja adicionar mais um usuário? (s/n) ").lower()
        if asking == "n" or asking == "nao" or asking == "não":
            break

    return alunos

def prompt_for_turma_lider():
    bright_print("Selecione um líder para a turma: ")
    lider = select_user_interactively(create_users_list_dynamic("type", "LIDER"))
    return lider["id"]