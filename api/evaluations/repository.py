from ..utils import generate_id

from .persistence import read_evaluations, write_evaluations
from .common import evaluation_dict
from ..teams.repository import search_members

_evaluations = []


def reload_evaluations():
    global _evaluations
    _evaluations = read_evaluations()


def update_evaluations():
    write_evaluations(_evaluations)


def get_evaluations():
    if len(_evaluations) == 0:
        reload_evaluations()
    return _evaluations

def get_all_evaluations_from_sprint(sprint):
    return [
        evaluation
        for evaluation in get_evaluations()
        if sprint["id"] == evaluation["sprint"]["id"]
    ]


def get_all_evaluations_from_team(team):
    return [
        evaluation
        for evaluation in get_evaluations()
        if team["id"] == evaluation["sprint"]["team"]["id"]
    ]


def get_all_evaluations_from_sprint_and_member(sprint, member):
    return [
        evaluation
        for evaluation in get_evaluations()
        if sprint["id"] == evaluation["sprint"]["id"] and member["id"] == evaluation["evaluated"]["id"]
    ]


def get_all_evaluations_from_team_member(team, member):
    return [
        evaluation
        for evaluation in get_evaluations()
        if team["id"] == evaluation["sprint"]["team"]["id"] and member["id"] == evaluation["evaluated"]["id"]
    ]


def create_evaluation(sprint, evaluator, evaluated, grades):
    id = generate_id()
    evaluation = evaluation_dict(
        id,
        sprint, 
        evaluator,
        evaluated,
        grades
    )
    get_evaluations().append(evaluation)
    update_evaluations()
    return evaluation


def delete_evaluation(evaluation):
    get_evaluations().remove(evaluation)
    update_evaluations()

