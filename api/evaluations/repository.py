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

