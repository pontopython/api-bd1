import uuid
from api.teams import create_teams_list
from api.turmas.persistance import write_turma
from api.users import create_users_list_dynamic

from turmas.prompts import (
    prompt_for_turma_lider,
    prompt_for_alunos)

from turmas.persistance import create_turma_dict

from utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    cyan_print,
    green_print,
    red_print,
)
from validation import (
    prompt_for_valid_turma_name,
    prompt_for_valid_username,
    prompt_for_valid_option,
)

from users import (create_alunos_list, select_user_interactively)

TURMAS_FILE = "data/turmas.txt"

def create_turma_interactively():
    blue_bright_print("\n\tFormulário de Criação de Turma\n")
    id = uuid.uuid4()
    name = prompt_for_valid_turma_name()
    id_lider = prompt_for_turma_lider()
    #ALTERAR
    id_client = uuid.uuid4()
    lista_alunos = prompt_for_alunos()
    lista_times = create_teams_list()
    turma = create_turma_dict(id, name, id_lider, id_client, lista_alunos, lista_times)
    write_turma(turma)