from ..users.repository import get_user_by_id
from .common import create_turma_dict

TURMAS_FILE = "data/turmas.txt"


def turma_dict_to_line(turma):
    id = turma["id"]
    name = turma["name"]
    group_leader_id = turma["group_leader"]["id"]
    fake_client_id = turma["fake_client"]["id"]
    students_ids = ",".join([student["id"] for student in turma["students"]])
    teams_ids = ",".join([team["id"] for team in turma["teams"]])

    return f"{id};{name};{group_leader_id};{fake_client_id};{students_ids};{teams_ids}"


def line_to_turma_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    group_leader_id = splitted_line[2]
    group_leader = get_user_by_id(group_leader_id)
    fake_client_id = splitted_line[3]
    fake_client = get_user_by_id(fake_client_id)
    students_ids = splitted_line[4].split(",")
    students = [get_user_by_id(id) for id in students_ids]
    teams = []

    return create_turma_dict(id, name, group_leader, fake_client, students, teams)


def write_turmas(turmas):
    file = open(TURMAS_FILE, "w")
    lines = [turma_dict_to_line(turma) + "\n" for turma in turmas]
    file.writelines(lines)
    file.close()


def read_turmas():
    file = open(TURMAS_FILE, "r")
    turmas = [line_to_turma_dict(line) for line in file.readlines()]
    file.close()
    return turmas
