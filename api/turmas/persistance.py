from utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    cyan_print,
    green_print,
    red_print,
)

TURMAS_FILE = "../data/turmas.txt"

def write_turma(turma):
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

def create_turma_dict(id, name, id_lider, id_client, lista_alunos, lista_times):
    return {
        "id": id,
        "name": name,
        "lider_turma_id": id_lider,
        "fake_client_id": id_client,
        "alunos": lista_alunos,
        "times": lista_times
    }