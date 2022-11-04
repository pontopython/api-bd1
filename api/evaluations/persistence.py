import os

from ..sprints.repository import get_sprint_by_id
from ..users.repository import get_user_by_id
from .common import evaluation_dict

EVALUATIONS_FILE = "data/evaluations.txt"

os.makedirs("data", exist_ok=True)
if not os.path.exists(EVALUATIONS_FILE):
    open(EVALUATIONS_FILE, "a").close()


def evaluation_dict_to_line(evaluation):
    id = evaluation["id"]
    sprint_id = evaluation["sprint"]["id"]
    evaluator_id = evaluation["evaluator"]["id"]
    evaluated_id = evaluation["evaluated"]["id"]
    grades = ",".join([
        f"{question}:{grade}"
        for question, grade in evaluation["grades"].items()
    ])
    return f"{id};{sprint_id};{evaluator_id};{evaluated_id};{grades}" 


def line_to_evaluation_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    sprint_id = splitted_line[1]
    sprint = get_sprint_by_id(sprint_id)
    evaluator_id = splitted_line[2]
    evaluator = get_user_by_id(evaluator_id)
    evaluated_id = splitted_line[3]
    evaluated = get_user_by_id(evaluated_id)
    grades = {}
    grades_lines = splitted_line[4].split(",")
    for grade_line in grades_lines:
        question, grade = grade_line.split(":")
        grades[question] = int(grade)
    return evaluation_dict(id, sprint, evaluator, evaluated, grades)


def write_evaluations(evaluations):
    file = open(EVALUATIONS_FILE, "w")
    lines = [evaluation_dict_to_line(evaluation) for evaluation in evaluations]
    file.writelines(lines)
    file.close()


def read_evaluations():
    file = open(EVALUATIONS_FILE, "r")
    evaluations = [evaluation_dict_to_line(line) for line in file.readlines()]
    file.close()
    return evaluations