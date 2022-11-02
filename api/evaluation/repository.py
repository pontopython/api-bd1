from .persistence import read_evaluation, write_evaluation
from .common import create_evaluation_dict
from ..teams.repository import search_members

_evaluation = []

def reload_evaluation():
    global _evaluation
    _evaluation = read_evaluation()

def update_evaluation():
    write_evaluation(_evaluation)

def get_evaluation():
    if len(_evaluation) == 0:
        reload_evaluation()
    return _evaluation

def create_evaluation(id_sprint, id_team, id_user_log, category_user_log, id_evaluated_user, category_evaluated_user, name_evaluated_user, skill_1, skill_2, skill_3, skill_4, skill_5):
    evaluation = create_evaluation_dict(
        id_sprint, 
        id_team, 
        id_user_log, 
        category_user_log, 
        id_evaluated_user,
        category_evaluated_user,
        name_evaluated_user,
        skill_1,
        skill_2,
        skill_3,
        skill_4,
        skill_5
    )
    get_evaluation().append(evaluation)
    update_evaluation()
    return evaluation

def delete_evaluation(evaluation):
    get_evaluation().remove(evaluation)
    update_evaluation()

