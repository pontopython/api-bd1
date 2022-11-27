from ..utils import safe_int_input, clear_screen, console
from ..teams.tui import search_and_select_team, search_and_select_member, select_LT_member, select_PO_member
from ..sprints.repository import get_opened_sprint_from_group
from ..turmas.tui import search_and_select_turma
from ..teams.tui import select_team_from_turma, select_member, select_member_or_instructor
from ..sprints.tui import select_sprint_from_group
from rich.table import Table

from .repository import (
    create_evaluation,
    get_all_evaluations_from_sprint,
    get_all_evaluations_from_team,
    get_all_evaluations_from_sprint_and_member,
    get_all_evaluations_from_team_member,
    update_evaluations,
    get_already_evaluated_by_a_user,
)
from .prompt import prompt_evaluation_form
from .common import QUESTIONS, ALTERNATIVES


def summary_evaluation(evaluation):
    evaluator_name = evaluation["evaluator"]["name"]
    evaluated_name = evaluation["evaluated"]["name"]
    average = sum(evaluation["grades"].values()) / len(evaluation["grades"])
    return f"Avaliador: %s, Avaliado: %s, Média: %.2f" % (evaluator_name, evaluated_name, average)


def detail_evaluation(evaluation):
    evaluator_name = evaluation["evaluator"]["name"]
    evaluated_name = evaluation["evaluated"]["name"]

    table = Table()

    table.add_column("[blue]Avaliador[/blue]")
    table.add_column("[blue]Avaliado[/blue]")

    table.add_row(evaluator_name, evaluated_name)

    console.print(table)

    for question, question_desc in QUESTIONS.items():
        grade = evaluation["grades"][question]
        console.print(f"\n [purple]Questão:[/purple] {question_desc}")
        console.print(
            "[yellow]Nota:[/yellow] %.2f - %s" % (grade, ALTERNATIVES[grade])
        )  # TODO: Alessandra, usa isso nos outros lugares que mostra nota

    average = sum(evaluation["grades"].values()) / len(evaluation["grades"])
    console.print(f"\n [yellow]Média:[/yellow] %.2f" % average)
    console.print()

def admin_list_evaluations(sprint):
    evaluations = get_all_evaluations_from_sprint(sprint)
    console.print("\n[blue]Avaliações[/blue]")
    for evaluation in evaluations:
        console.print(f"\n    - {summary_evaluation(evaluation)}")
        console.print()
    console.print()

def admin_create_evaluation(team, sprint):
    console.print("\n [purple]Avaliador:[/purple]")
    evaluator = select_member_or_instructor(team)
    console.print()

    console.print("\n [purple]Avaliado:[/purple]")
    evaluated = select_member(team)
    console.print()

    grades = prompt_evaluation_form()

    create_evaluation(sprint, evaluator, evaluated, grades)


def common_user_evaluate_member(user, team, sprint):
    console.print("\n [purple]Avaliado:[/purple]")
    console.print()

    already_evaluated = get_already_evaluated_by_a_user(team, sprint, user)
    evaluated = select_member(team, excludes=[user, *already_evaluated])

    if evaluated is None:
        console.print("\n [bold red]Não há mais membros para avaliar![/bold red]")
        console.print()
        return

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def LG_user_evaluate_LT(user, team, sprint):
    console.print("\n [purple]Avaliado:[/purple]")
    console.print()
    evaluated = select_LT_member(team)
    already_evaluated = get_already_evaluated_by_a_user(team, sprint, user)
    if evaluated["id"] in [e["id"] for e in already_evaluated]:
        console.print("\n [bold red]Líder técnico já foi avaliado[/bold red]")
        console.print()
        return

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def FC_user_evaluate_PO(user, team, sprint):
    console.print("\n [purple]Avaliado:[/purple]")
    console.print()
    evaluated = select_PO_member(team)
    already_evaluated = get_already_evaluated_by_a_user(team, sprint, user)
    if evaluated["id"] in [e["id"] for e in already_evaluated]:
        console.print("[bold red]Product owner já foi avaliado[/bold red]")
        console.print()
        return

    grades = prompt_evaluation_form()

    create_evaluation(sprint, team, user, evaluated, grades)


def self_evaluation(user, team, sprint):
    already_evaluated = get_already_evaluated_by_a_user(team, sprint, user)
    if user["id"] in [e["id"] for e in already_evaluated]:
        console.print("\n [bold red]Você já se avaliou![/bold red]")
        console.print()
    grades = prompt_evaluation_form()
    create_evaluation(sprint, team, user, user, grades)


def select_evaluation(sprint):
    evaluations = get_all_evaluations_from_sprint(sprint)

    if len(evaluations) == 0:
        console.print("\n [bold red]Nenhuma avaliação encontrada.[/bold red]")
        console.print()
        return None

    for index, evaluation in enumerate(evaluations):
        print(f"{index+1} - {summary_evaluation(evaluation)}")

    while True:
        option = safe_int_input("Opção: ")
        if option > 0 and option <= len(evaluations):
            return evaluations[option - 1]
        console.print("\n :x: [bold red]Opção inválida.[/bold red] :x:", justify="center")
        console.print()

def admin_detail_evaluation(sprint):
    evaluation = select_evaluation(sprint)
    detail_evaluation(evaluation)


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
        console.print(f"\n [purple]Questão:[/purple] {QUESTIONS[question]}")
        console.print(f"\n [purple]Média:[/purple] {avg_by_question[question]}")
        console.print()    

    total_avg = sum(avg_by_question.values()) / len(avg_by_question)
    console.print(f"\n [purple]Média total:[/purple] {total_avg}")
    console.print()

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
    console.print("\n [green]Selecione a Turma[/green]")
    console.print()
    turma = search_and_select_turma()
    if turma is None:
        return

    console.print("\n [green]Selecione a sprint[/green]")
    console.print()
    sprint = select_sprint_from_group(turma)
    if sprint is None:
        return

    console.print("\n [green]Selecione o Time[/green]")
    console.print()
    team = select_team_from_turma(turma)
    if team is None:
        return

    while True:
        console.rule("\n [bold blue]Menu Avaliações (Administrador)[/bold blue]")
        console.print(f"\n [green]Time:[/green] {team['name']}, [green]Sprint:[/green] {sprint['name']} #{sprint['id']}\n")
        console.print("[blue]1 -[/blue] Listar")
        console.print("[blue]2 -[/blue] Criar")
        console.print("[blue]3 -[/blue] Detalhar")
        console.print("[blue]4 -[/blue] Estatísticas deste time nesta sprint")
        console.print("[blue]5 -[/blue] Estatísticas deste time em todas as sprints")
        console.print("[blue]6 -[/blue] Estatísticas de um membro nesta sprint")
        console.print("[blue]7 -[/blue] Estatísticas de um membro em todas as sprints")
        console.print("[blue]8 -[/blue] Voltar")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 9:
                break
            console.print("\n :x: [bold red]Opção inválida.[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            admin_list_evaluations(sprint)
        elif option == 2:
            admin_create_evaluation(team, sprint)
        elif option == 3:
            admin_detail_evaluation(sprint)
        elif option == 4:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 5:
            admin_detail_team_statistics_in_all_sprints(team)
        elif option == 6:
            admin_detail_member_statistics_in_one_sprint(sprint)
        elif option == 7:
            admin_detail_member_statistics_in_all_sprints(team)
        else:
            return


def common_user_evaluations_menu(team, user):
    if team is None or user is None:
        return

    sprint = get_opened_sprint_from_group(team['turma']) or select_sprint_from_group(team["turma"], closed=True)
    if sprint is None:
        return

    while True:
        console.rule("\n [bold blue]Menu Avaliações[/bold blue] ")
        console.print(f"\n [green]Time:[/green] {team['name']}, [green]Sprint:[/green] {sprint['name']} #{sprint['id']}\n")
        console.print("[blue]1 -[/blue] Avaliar Membro")
        console.print("[blue]2 -[/blue] Autoavaliação")
        console.print("[blue]3 -[/blue] Estatísticas deste time nesta sprint")
        console.print("[blue]4 -[/blue] Estatísticas deste time em todas as sprints")
        console.print("[blue]5 -[/blue] Minhas estatísticas nesta sprint")
        console.print("[blue]6 -[/blue] Minhas estatísticas em todas as sprints")
        console.print("[blue]7 -[/blue] Voltar")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 7:
                break
            console.print("\n :x: [bold red]Opção inválida.[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            if sprint["status"] == "fechada":
                console.print("\n [bold red]Você não pode fazer uma avaliação em uma sprint fechada.[/bold red]")
                console.print()
                continue
            common_user_evaluate_member(user, team, sprint)
        elif option == 2:
            if sprint["status"] == "fechada":
                console.print("\n [bold red]Você não pode fazer uma avaliação em uma sprint fechada.[/bold red]")
                console.print()
                continue
            self_evaluation(user, team, sprint)
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


def LG_user_evaluations_menu(turma, user):
    sprint = get_opened_sprint_from_group(turma) or select_sprint_from_group(turma, closed=True)
    if sprint is None:
        return

    console.print("\n [green]Selecione o Time[/green]")
    console.print()
    team = select_team_from_turma(turma)
    if team is None:
        return

    while True:
        console.rule("\n [bold blue]Menu Avaliações[/bold blue] ")
        console.print(f"\n [green]Time:[/green] {team['name']}, [green]Sprint:[/green] {sprint['name']} #{sprint['id']}\n")
        console.print("[blue]1 -[/blue] Avaliar Líder Técnico")
        console.print("[blue]2 -[/blue] Estatísticas deste time nesta sprint")
        console.print("[blue]3 -[/blue] Estatísticas deste time em todas as sprints")
        console.print("[blue]4 -[/blue] Selecionar outro time")
        console.print("[blue]5 -[/blue] Voltar")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 5:
                break
            console.print("\n :x: [bold red]Opção inválida.[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            if sprint["status"] == "fechada":
                console.print("\n [bold red]Você não pode fazer uma avaliação em uma sprint fechada.[/bold red]")
                console.print()
                continue
            LG_user_evaluate_LT(user, team, sprint)
        elif option == 2:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 3:
            admin_detail_team_statistics_in_all_sprints(team)
        elif option == 4:
            select_team_from_turma(turma)
        else:
            return


def FC_user_evaluations_menu(turma, user):
    sprint = get_opened_sprint_from_group(turma) or select_sprint_from_group(turma, closed=True)
    if sprint is None:
        return

    console.print("\n [green]Selecione o Time[/green]")
    console.print()
    team = select_team_from_turma(turma)
    if team is None:
        return


    while True:
        console.rule("\n [bold blue]Menu Avaliações[/bold blue]")
        console.print(f"\n [green]Time:[/green] {team['name']}, [green]Sprint:[/green] {sprint['name']} #{sprint['id']}\n")
        console.print("[blue]1 -[/blue] Avaliar Product Owner")
        console.print("[blue]2 -[/blue] Estatísticas deste time nesta sprint")
        console.print("[blue]3 -[/blue] Estatísticas deste time em todas as sprints")
        console.print("[blue]4 -[/blue] Selecionar outro time")
        console.print("[blue]5 -[/blue] Voltar")
        console.print()

        while True:
            option = safe_int_input("Opção: ")
            if option >= 1 and option <= 5:
                break
            console.print("\n :x: [bold red]Opção inválida.[/bold red] :x:", justify="center")
            console.print()

        if option == 1:
            if sprint["status"] == "fechada":
                console.print("\n [bold red]Você não pode fazer uma avaliação em uma sprint fechada.[/bold red]")
                console.print()
                continue
            FC_user_evaluate_PO(user, team, sprint)
        elif option == 2:
            admin_detail_team_statistics_in_one_sprint(sprint)
        elif option == 3:
            admin_detail_team_statistics_in_all_sprints(team)
        elif option == 4:
            select_team_from_turma(turma)
        else:
            return
