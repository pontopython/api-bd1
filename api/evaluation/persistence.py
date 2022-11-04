import os

from .common import create_evaluation_dict
from login import get_logged_user

EVALUATIONS_FILE = "data/evaluations.txt"

os.makedirs("data", exist_ok=True)
if not os.path.exists(EVALUATIONS_FILE):
    open(EVALUATIONS_FILE, "a").close()


def evaluation_dict_to_line(user, lista, team,sprint):
    evaluation = {
        "skill_1": lista[0],
        "skill_2": lista[1],
        "skill_3": lista[2],
        "skill_4": lista[3],
        "skill_5": lista[4],
    }
    id_sprint = sprint["id"]
    id_team = team["id"]
    id_user_log = get_logged_user()["id"] #mudar depois que criar o novo login
    category_user_log = get_logged_user()["category"]
    id_evaluated_user = user["id"]
    category_evaluated_user = user["category"]
    name_evaluated_user = user["name"]
    skill_1 = evaluation["skill_1"]
    skill_2 = evaluation["skill_2"]
    skill_3 = evaluation["skill_3"]
    skill_4 = evaluation["skill_4"]
    skill_5 = evaluation["skill_5"]
    
    return f"{id_sprint};{id_team};{id_user_log};{category_user_log};{id_evaluated_user};{category_evaluated_user};{name_evaluated_user};{skill_1};{skill_2};{skill_3};{skill_4};{skill_5}"


def line_to_evaluation_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id_sprint = splitted_line[0]
    id_team = splitted_line[1]
    id_user_log = splitted_line[2]
    category_user_log = splitted_line[3]
    id_evaluated_user = splitted_line[4]
    category_evaluated_user = splitted_line[5]
    name_evaluated_user = splitted_line[6]
    skill_1 = splitted_line[7]
    skill_2 = splitted_line[8]
    skill_3 = splitted_line[9]
    skill_4 = splitted_line[10]
    skill_5 = splitted_line[11]
    
    return create_evaluation_dict(id_sprint, id_team, id_user_log, category_user_log, id_evaluated_user, category_evaluated_user, name_evaluated_user, skill_1, skill_2, skill_3, skill_4, skill_5)


def write_evaluation(evaluation):
    file = open(EVALUATIONS_FILE, "w")
    lines = [evaluation_dict_to_line(evaluation) + "\n"]
    file.writelines(lines)
    file.close()


def read_evaluation():
    file = open(EVALUATIONS_FILE, "r")
    evaluation = [evaluation_dict_to_line(line) for line in file.readlines()]
    file.close()
    return evaluation