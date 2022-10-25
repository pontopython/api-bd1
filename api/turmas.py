import uuid
from api.teams import create_teams_list
from api.users import create_users_list_dynamic

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
    prompt_for_valid_turma_name,
    prompt_for_valid_username,
    prompt_for_valid_option,
)

from users import (create_alunos_list, select_user_interactively)

TURMAS_FILE = "data/turmas.txt"

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
    lider = select_user_interactively(create_users_list_dynamic("type", "LIDER"))




def create_turma_dict(id, name, id_lider, id_client, lista_alunos, lista_times):
    return {
        "id": id,
        "name": name,
        "lider_turma_id": id_lider,
        "fake_client_id": id_client,
        "alunos": lista_alunos,
        "times": lista_times
    }

def save_turma_to_file(turma):
    file = open(TURMAS_FILE, "a")
    line = turma_dict_to_line(turma)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("\n\tTurma registrada com sucesso!")

def turma_dict_to_line(turma):
    id = turma["id"]
    name = turma["name"]
    id_lider = turma["lider_turma_id"]
    id_client = turma["fake_client_id"]
    alunos = turma["alunos"]
    times = turma["times"]

    return f"{id};{name};{id_lider};{id_client};{alunos},{times}"

def line_to_turma_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    id_lider = splitted_line[2]
    id_client = splitted_line[3]
    alunos = splitted_line[4]
    times = splitted_line[5]

    return create_turma_dict(id, name, id_lider, id_client, alunos, times)

def create_turma_interactively():
    blue_bright_print("\n\tFormulário de Criação de Turma\n")
    id = uuid.uuid4()
    id_lider = prompt_for_turma_lider()
    #ALTERAR
    id_client = uuid.uuid4()
    name = prompt_for_valid_turma_name()
    lista_alunos = prompt_for_alunos()
    lista_times = create_teams_list()
    turma = create_turma_dict(id, name, id_lider, id_client, lista_alunos, lista_times)
    save_turma_to_file(turma)