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

def get_all_evaluations_from_sprint(sprint):        #passa a ser de todos os times da turma
    return [
        evaluation
        for evaluation in get_evaluations()
        if sprint["id"] == evaluation["sprint"]["id"]
    ]


def get_all_evaluations_from_team(team):        #todas as avaliações do time, independente da sprint
    return [
        evaluation
        for evaluation in get_evaluations()
        if team["id"] == evaluation["team"]["id"]
    ]


def get_all_evaluations_from_sprint_and_team(sprint, team):     #todas as avaliações do time por sprint
    return [
        evaluation
        for evaluation in get_evaluations()
        if sprint["id"] == evaluation["sprint"]["id"] and team["id"] == evaluation["team"]["id"]
    ]


def get_all_evaluations_from_sprint_and_member(sprint, member):     #todas as avaliações do membro por sprint e por time, já que ele não pode estar inserido em mais de um time por turma
    return [
        evaluation
        for evaluation in get_evaluations()
        if sprint["id"] == evaluation["sprint"]["id"] and member["id"] == evaluation["evaluated"]["id"]
    ]


def get_all_evaluations_from_team_member(team, member):     #todas as avaliações de um membro do time
    return [
        evaluation
        for evaluation in get_evaluations()
        if team["id"] == evaluation["team"]["id"] and member["id"] == evaluation["evaluated"]["id"]
    ]


def create_evaluation(sprint, team, evaluator, evaluated, grades):
    id = generate_id()
    evaluation = evaluation_dict(
        id,
        sprint,
        team, 
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

