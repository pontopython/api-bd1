from ..teams.tui import search_and_select_team, search_and_select_member
from ..sprints.repository import get_opened_sprint_from_team

from .repository import create_evaluation
from .prompt import prompt_evaluation_form



def admin_create_evaluation():
    print("Time:")
    team = search_and_select_team()
    if team is None:
        return None
    
    sprint = get_opened_sprint_from_team(team)
    if sprint is None:
        print("Time não possui sprint aberta.")
    
    print("Avaliador:")
    evaluator = search_and_select_member(team)
    
    print("Avaliado:")
    evaluated = search_and_select_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, evaluator, evaluated, grades)


def current_user_evaluates():
    # TODO: Criar método equivalente ao de cima mas com as devidas restrições
    # para o usuário logado.
    pass


def admin_list_evaluations():
    # TODO: Administrador seleciona turma e time e depois lista as avaliações
    pass


def admin_detail_evaluation():
    # TODO: Administrador seleciona turma e time e depois mostra detalhes de
    # uma avaliação
    pass

def admin_detail_team_statistics():
    # TODO: Administrador seleciona turma e time e depois e mostra as médias das
    # notas
    pass