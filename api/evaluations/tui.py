from ..teams.tui import search_and_select_team, search_and_select_member
from ..sprints.repository import get_opened_sprint_from_team
from ..turmas.tui import search_and_select_turma
from ..teams.tui import select_team_from_turma
from ..sprints.tui import select_sprint_from_team

from .repository import create_evaluation
from .prompt import prompt_evaluation_form



def admin_create_evaluation(sprint):
    team = sprint["team"]

    print("Avaliador:")
    evaluator = search_and_select_member(team)
    
    print("Avaliado:")
    evaluated = search_and_select_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, evaluator, evaluated, grades)


def member_evaluate(sprint, evaluator, evaluated):
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


def admin_evaluations_menu():
    print("Selecione a Turma")
    turma = search_and_select_turma()
    if turma is None:
        return
    
    print("Selecione o Time")
    team = select_team_from_turma(turma)
    if team is None:
        return

    print("Selecione a sprint")
    sprint = select_sprint_from_team(team)
    if sprint is None:
        return

    print("Menu Avaliações (Administrador)")
    print("1 - Listar")
    print("2 - Criar avaliação")
    print("3 - Fechar")
    print("4 - Reabrir")
    print("5 - Voltar")
    
    while True:
        option = int(input("Opção: "))
        if option >= 1 and option <= 6:
            break
        print("Opção inválida.")
    
    if option == 1:
        print("not yet")
    elif option == 2:
        admin_create_evaluation(sprint)
    elif option == 3:
        print("not yet")
    elif option == 4:
        print("not yet")
    else:
        return