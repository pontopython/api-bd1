from ..utils import safe_int_input
from ..teams.tui import search_and_select_team, search_and_select_member, select_LT_member, select_PO_member
from ..sprints.repository import get_opened_sprint_from_group
from ..turmas.tui import search_and_select_turma
from ..teams.tui import select_team_from_turma, select_member, select_member_or_instructor
from ..sprints.tui import select_sprint_from_group

from .repository import (
    create_evaluation,
    get_all_evaluations_from_sprint,
    get_all_evaluations_from_team,
    get_all_evaluations_from_sprint_and_member,
    get_all_evaluations_from_team_member,
    update_evaluations,
)
from .prompt import prompt_evaluation_form
from .common import QUESTIONS, ALTERNATIVES


def summary_evaluation(evaluation):
    evaluator_name = evaluation["evaluator"]["name"]
    evaluated_name = evaluation["evaluated"]["name"]
    average = sum(evaluation["grades"].values()) / len(evaluation["grades"])
    return f"Avaliador: {evaluator_name}, Avaliado: {evaluated_name}, Média: {average}"


def detail_evaluation(evaluation):
    evaluator_name = evaluation["evaluator"]["name"]
    evaluated_name = evaluation["evaluated"]["name"]
    print(f"Avaliador: {evaluator_name}")
    print(f"Avaliado: {evaluated_name}")

    for question, question_desc in QUESTIONS.items():
        grade = evaluation["grades"][question]
        print(f"Questão: {question_desc}")
        print(
            "Nota: %.2f - %s" % (grade, ALTERNATIVES[grade])
        )  # TODO: Alessandra, usa isso nos outros lugares que mostra nota

    average = sum(evaluation["grades"].values()) / len(evaluation["grades"])
    print(f"Média: {average}")


def admin_list_evaluations(sprint):
    evaluations = get_all_evaluations_from_sprint(sprint)
    print("Avaliações")
    for evaluation in evaluations:
        print(f"    - {summary_evaluation(evaluation)}")


def admin_create_evaluation(team, sprint):
    print("Avaliador:")
    evaluator = select_member_or_instructor(team)

    print("Avaliado:")
    evaluated = select_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, evaluator, evaluated, grades)


def common_user_evaluate_member(user, team, sprint):
    print("Avaliado:")
    evaluated = select_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def LG_user_evaluate_LT(user, team, sprint):
    print("Avaliado:")
    evaluated = select_LT_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def FC_user_evaluate_PO(user, team, sprint):
    print("Avaliado:")
    evaluated = select_PO_member(team)

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def self_evaluation(user, sprint):
    grades = prompt_evaluation_form()
    create_evaluation(sprint, user, user, grades)


def select_evaluation(sprint):
    evaluations = get_all_evaluations_from_sprint(sprint)

    if len(evaluations) == 0:
        print("Nenhuma avaliação encontrada.")
        return None

    for index, evaluation in enumerate(evaluations):
        print(f"{index+1} - {summary_evaluation(evaluation)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(evaluations):
            return evaluations[option - 1]
        print("Opção inválida.")


def admin_detail_evaluation(sprint):
    evaluation = select_evaluation(sprint)
    detail_evaluation(evaluation)


def admin_reevaluate(sprint):
    evaluation = select_evaluation(sprint)
    new_grades = prompt_evaluation_form()
    evaluation["grades"] = new_grades
    update_evaluations()


def show_statistics(evaluations):
    sum_by_question = {}
    avg_by_question = {}

    for question in QUESTIONS:
        sum_by_question[question] = 0
        avg_by_question[question] = 0
        for evaluation in evaluations:
            sum_by_question[question] += evaluation["grades"][question]

    if len(evaluations) != 0:
        for question in sum_by_question:
            avg_by_question[question] = sum_by_question[question] / len(evaluations)

    for question in QUESTIONS:
        print(f"Questão: {QUESTIONS[question]}")
        print(f"Média: {avg_by_question[question]}")

    total_avg = sum(avg_by_question.values()) / len(avg_by_question)
    print(f"Média total: {total_avg}")


def admin_detail_team_statistics_in_one_sprint(sprint):
    evaluations = get_all_evaluations_from_sprint(sprint)
    show_statistics(evaluations)


def admin_detail_team_statistics_in_all_sprints(team):
    evaluations = get_all_evaluations_from_team(team)
    show_statistics(evaluations)

def show_user_statistics_in_one_sprint(user, sprint):
    evaluations = get_all_evaluations_from_sprint_and_member(sprint, user)
    show_statistics(evaluations)

def admin_detail_member_statistics_in_one_sprint(team, sprint):
    member = select_member(team)
    show_user_statistics_in_one_sprint(member, sprint)


def show_member_statistics_in_all_sprints(user, team):
    evaluations = get_all_evaluations_from_team_member(team, user)
    show_statistics(evaluations)

def admin_detail_member_statistics_in_all_sprints(team):
    member = select_member(team)
    show_member_statistics_in_all_sprints(member, team)


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
    sprint = select_sprint_from_group(turma)
    if sprint is None:
        return
    
    while True:
        print("Menu Avaliações (Administrador)")
        print(f"Time: {team['name']}, Sprint: {sprint['name']} #{sprint['id']}")
        print("1 - Listar")
        print("2 - Criar")
        print("3 - Detalhar")
        print("4 - Reavaliar")
        print("5 - Estatísticas deste time nesta sprint")
        print("6 - Estatísticas deste time em todas as sprints")
        print("7 - Estatísticas de um membro nesta sprint")
        print("8 - Estatísticas de um membro em todas as sprints")
        print("9 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 9:
                break
            print("Opção inválida.")

        if option == 1:
            admin_list_evaluations(sprint)
        elif option == 2:
            admin_create_evaluation(team, sprint)
        elif option == 3:
            admin_detail_evaluation(sprint)
        elif option == 4:
            admin_reevaluate(sprint)
        elif option == 5:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 6:
            admin_detail_team_statistics_in_all_sprints(team)
        elif option == 7:
            admin_detail_member_statistics_in_one_sprint(sprint)
        elif option == 8:
            admin_detail_member_statistics_in_all_sprints(team)
        else:
            return


def common_user_evaluations_menu(team, user):
    if team is None or user is None:
        return

    sprint = get_opened_sprint_from_group(team['turma'])
    if sprint is None:
        return
    
    while True:
        print("Menu Avaliações (Usuário Comum)")
        print(f"Time: {team['name']}, Sprint: {sprint['name']} #{sprint['id']}")
        print("1 - Avaliar Membro")
        print("2 - Autoavaliação")
        print("3 - Estatísticas deste time nesta sprint")
        print("4 - Estatísticas deste time em todas as sprints")
        print("5 - Minhas estatísticas nesta sprint")
        print("6 - Minhas estatísticas em todas as sprints")
        print("7 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 7:
                break
            print("Opção inválida.")

        if option == 1:
            common_user_evaluate_member(user, team, sprint)
        elif option == 2:
            self_evaluation(user, sprint)
        elif option == 3:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 4:
            admin_detail_team_statistics_in_all_sprints(team)
        elif option == 5:
            show_user_statistics_in_one_sprint(user, sprint)
        elif option == 6:
            show_member_statistics_in_all_sprints(user, sprint)
        else:
            return


def LG_user_evaluations_menu(team, user):
    if team is None or user is None:
        return

    sprint = get_opened_sprint_from_group(team['turma'])
    if sprint is None:
        return
    
    while True:
        print("Menu Avaliações (Usuário Comum)")
        print(f"Time: {team['name']}, Sprint: {sprint['name']} #{sprint['id']}")
        print("1 - Avaliar Líder Técnico")
        print("2 - Estatísticas deste time nesta sprint")
        print("3 - Estatísticas deste time em todas as sprints")
        print("4 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 4:
                break
            print("Opção inválida.")

        if option == 1:
            LG_user_evaluate_LT(user, team, sprint)
        elif option == 2:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 3:
            admin_detail_team_statistics_in_all_sprints(team)
        else:
            return


def FC_user_evaluations_menu(team, user):
    if team is None or user is None:
        return

    sprint = get_opened_sprint_from_group(team['turma'])
    if sprint is None:
        return
    
    while True:
        print("Menu Avaliações (Usuário Comum)")
        print(f"Time: {team['name']}, Sprint: {sprint['name']} #{sprint['id']}")
        print("1 - Avaliar Product Owner")
        print("2 - Estatísticas deste time nesta sprint")
        print("3 - Estatísticas deste time em todas as sprints")
        print("4 - Voltar")

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 4:
                break
            print("Opção inválida.")

        if option == 1:
            FC_user_evaluate_PO(user, team, sprint)
        elif option == 2:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 3:
            admin_detail_team_statistics_in_all_sprints(team)
        else:
            return
