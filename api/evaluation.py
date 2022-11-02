import statistics
from api.sprints.sprints import get_opened_sprint

from api.turmas.repository import get_turmas_by

from .login import get_logged_user
from .teams.persistence import line_to_team_dict
from .utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    green_print,
    magenta_print,
    red_print,
)
import json

EVALUATIONS_JSON_FILE = "data/evaluations.json"      # tentar implementar depois

EVALUATIONS_TXT_FILE =  "data/evaluations.txt"

CATEGORIES = {
    "PRODU": "Product Owner",
    "LIDER": "Líder Técnico",
    "COMUM": "Membro do time",
}

def search_groups():
    user = get_logged_user()
    groups = {}
    lg_groups = get_turmas_by("group_leader", user['id'], 'id')
    fc_groups = get_turmas_by("fake_client", user['id'], 'id')
    student_groups = get_turmas_by(value=user['id'], function=lambda group, value: [student for student in group['students'] if student['id'] == value])

    if len(lg_groups) != 0:
        groups["Líder de Grupo"] = lg_groups

    if len(fc_groups) != 0:
        groups["Fake Client"] = fc_groups

    if len(student_groups) != 0:
        groups["Estudante"] = student_groups    

    return user, groups


def select_group(user, groups, select_member=True):
    if len(groups) < 1:
        print("Você não faz parte de nenhuma turma")
        return None, None, None

    else:
        menu = [(user_type, group) for user_type, groups in groups.items() for group in groups]
        enumerate_menu = enumerate(menu)

        print("Suas turmas:")
        
        for index, (user_type, group) in enumerate_menu:
            print(f'{index + 1}. {user_type} - {group["name"]}')
        
        input_group = int(input('Qual turma deseja selecionar? '))
    
        if input_group > 0 and input_group <= len(groups.keys()):
            group = menu[input_group - 1]
            return select_team(user, group, select_member)

        else:
            print("Opção inválida. Tente novamente!")
            return select_group(user, groups)


def select_team(user, group, select_member=True, show=True):
    teams = []
    
    with open("data/teams.txt", "r") as file:
        
        for line in file:
            team = line_to_team_dict(line)
            if team["turma"]['id'] == group[1]['id']:
                if group[0] in ['Líder de Grupo', 'Fake Client']:
                    teams.append(team)

                if group[0] == 'Estudante':
                    for member in team['members']:
                        if member['id'] == user['id']:
                            teams.append(team)
    if show:
        
        if len(teams) > 0:
            blue_bright_print("\n          Seus times:")
            
            for indice, team in enumerate(teams):
                print(f'     {indice+1}. {team["name"]}')

            input_team = int(bright_input("\nQual time deseja selecionar? "))

            if input_team > 0 and input_team <= len(teams):
                team = teams[input_team - 1]
                
                if select_member:
                    return select_team_member(user, team), team
                
                else:
                    return None, team

            else:
                red_print("\nOpção inválida. Tente novamente!\n")
                return select_team(user, select_member)
        
        else:
            red_print("Você não está inserido em nenhum time ainda.")
            return None, None
    
    else:
        return teams


def filter_not_evaluated_members(user, team, sprint):
    evaluated_members = []
    with open(EVALUATIONS_TXT_FILE, 'r') as file:
        for line in file:
            evaluation = line_to_evaluation_dict(line)
            if user['id'] == evaluation['evaluator_id'] \
                and team['id'] == evaluation['id_team'] \
                and sprint['id'] == evaluation['id_sprint']:
                evaluated_members.append(evaluation['evaluated_id'])
    not_evaluated_members = [member for member in team['members'] if member['id'] not in evaluated_members]

    return not_evaluated_members


def select_team_member(user, team):
    #       Mudar: 
    # - restringir a avaliação por sprint:  verificar qual a sprint que está aberta(sprints.json) e
    #       depois quais membros do time(teams.txt) o usuario logado ainda não avaliou(evaluations.txt)
    sprint = get_opened_sprint(team['id'])
    if sprint is None:
        print('Não tem sprint aberta')
        return
    not_evaluated_members = filter_not_evaluated_members(user, team, sprint)
    print()
    blue_bright_print(f'     Membros de {team["name"]}:')
    valid_members = []

    if team['turma']['group_leader']['id'] == user['id']:
        for member in not_evaluated_members:
            if member['category'] == 'LIDER':
                valid_members.append(member)

    elif team['turma']['fake_client']['id'] == user['id']:
        for member in not_evaluated_members:
            if member['category'] == 'PRODU':
                valid_members.append(member)

    else:
        valid_members = not_evaluated_members

    if len(valid_members) == 0:
        print('Não há membros para avaliar.')
        return None

    for indice, member in enumerate(valid_members):
        print(
            f'{indice+1}. {CATEGORIES[member["category"]].ljust(20," ")}{member["name"]}'
        )

    input_member = int(bright_input("\nQual membro deseja avaliar? "))
    
    if input_member > 0 and input_member <= len(valid_members):
        return valid_members[input_member - 1]

    else:
        red_print("Usuário inválido. Tente novamente!")
        return select_team_member(user, team)


def evaluation_form(evaluator=None, evaluated=None, team=None, sprint=None, show=True):
    questions = {
        "1": {
            "question": "Trabalho em equipe, cooperação e descentralização de conhecimento:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "2": {
            "question": "Iniciativa e proatividade:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "3": {
            "question": "Autodidaxia e agregação de conhecimento ao grupo:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "4": {
            "question": "Entrega de resultados e participação efetiva no projeto:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "5": {
            "question": "Competência técnica:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
    }
    if show:
        blue_bright_print(f"\n           Avaliação de {evaluated['name']}\n")
        lista = []
        for qk, qv in questions.items():
            green_print(f'\n{qk}. {qv["question"]}')

            print("\nEscolha entre as opções indicadas:\n")
            for ak, av in qv["answers"].items():
                print(f"[{ak}]: {av}")

            answer = int(bright_input("\nOpção: "))
            print()
            while answer < 0 or answer > 4:
                red_print("\nOpção inválida! Tente novamente.\n")
                answer = int(bright_input("\nOpção: "))
            lista.append(answer)

        return create_evaluation_dict(lista, evaluator, evaluated, team, sprint)

    else:
        return questions


def create_evaluation_dict_json(lista_skills, user, team):          #tentar implementar depois
    evaluation_dict = {
        "id_sprint": 1,
        "id_time": team,
        "id_avaliador": get_logged_user()["id"],
        "id_avaliado": user['id'],
        "skills": {
            "skill_1": lista_skills[0],
            "skill_2": lista_skills[1],
            "skill_3": lista_skills[2],
            "skill_4": lista_skills[3],
            "skill_5": lista_skills[4],
        }
    }

    return save_evaluation_json(evaluation_dict)


def save_evaluation_json(dict):
    with open(EVALUATIONS_JSON_FILE, "a") as file:
        file.write(json.dumps(dict) + '\n')


def read_evaluations_json() -> list:
    with open(EVALUATIONS_JSON_FILE, "r") as file:
        content = file.read()
        evaluations = json.loads(content)
    return evaluations


def create_evaluation_dict(lista_skills, evaluator, evaluated, team, sprint):
    evaluation = {
        "skill_1": lista_skills[0],
        "skill_2": lista_skills[1],
        "skill_3": lista_skills[2],
        "skill_4": lista_skills[3],
        "skill_5": lista_skills[4],
    }
    id_sprint = sprint['id']                             #colocar a sprint
    id_team = team['id']
    evaluator_id = evaluator["id"]
    evaluated_id = evaluated["id"]
    evaluated_category = evaluated["category"]
    evaluated_name = evaluated["name"]
    skill_1 = evaluation["skill_1"]
    skill_2 = evaluation["skill_2"]
    skill_3 = evaluation["skill_3"]
    skill_4 = evaluation["skill_4"]
    skill_5 = evaluation["skill_5"]

    line = f"{id_sprint};{id_team};{evaluator_id};{evaluated_id};{evaluated_category};{evaluated_name};{skill_1};{skill_2};{skill_3};{skill_4};{skill_5}"

    return save_evaluation(line)


def save_evaluation(line):
    file = open(EVALUATIONS_TXT_FILE, "a")
    file.write(line)
    file.write("\n")
    file.close()


def line_to_evaluation_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id_sprint = splitted_line[0]
    id_team = splitted_line[1]
    evaluator_id = splitted_line[2]
    evaluated_id = splitted_line[3]
    evaluated_category = splitted_line[4]
    evaluated_name = splitted_line[5]
    skill_1 = splitted_line[6]
    skill_2 = splitted_line[7]
    skill_3 = splitted_line[8]
    skill_4 = splitted_line[9]
    skill_5 = splitted_line[10]
    dict = {
        "id_sprint": id_sprint,
        "id_team": id_team,
        "evaluator_id": evaluator_id,
        "evaluated_id": evaluated_id,
        "evaluated_category": evaluated_category,
        "evaluated_name": evaluated_name,
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3,
        "skill_4": skill_4,
        "skill_5": skill_5,
    }
    return dict


def mean_grades(team, user):
    skills = [[], [], [], [], []]

    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            evaluation = line_to_evaluation_dict(line)
            if team == evaluation["id_team"] and user == evaluation["evaluated_id"]:
                skills[0].append(int(evaluation["skill_1"]))
                skills[1].append(int(evaluation["skill_2"]))
                skills[2].append(int(evaluation["skill_3"]))
                skills[3].append(int(evaluation["skill_4"]))
                skills[4].append(int(evaluation["skill_5"]))

    if len(skills[0]) > 0:
        mean = [
            round(statistics.mean(skills[0]), 1),
            round(statistics.mean(skills[1]), 1),
            round(statistics.mean(skills[2]), 1),
            round(statistics.mean(skills[3]), 1),
            round(statistics.mean(skills[4]), 1),
        ]

        total_mean = round(statistics.mean(mean), 1)

        return [mean, total_mean]
    else:
        return None


def print_mean_grades(team, user):
    mean = mean_grades(team, user["id"])
    questions = evaluation_form(user, team, show=False)

    if mean is None:
        magenta_print("\nVocê ainda não foi avaliado.")
        return

    blue_bright_print(f"\n          Médias de {user['name']}\n")
    for n, question in enumerate(questions):
        bright_print(f'{questions[question]["question"]}')
        if mean[0][n] > 2:
            green_print(f"{mean[0][n]}")
        elif mean[0][n] == 2:
            magenta_print(f"{mean[0][n]}")
        else:
            red_print(f"{mean[0][n]}")
    if mean[1] >= 2:
        green_print(f"\nMédia total: {mean[1]}\n")
    elif mean[1] == 2:
        magenta_print(f"\nMédia total: {mean[1]}\n")
    else:
        red_print(f"\nMédia total: {mean[1]}\n")


def print_mean_grades_LG(team_id, LT=False):
    with open("data/teams.txt", "r") as file:
        for line in file:
            team_dict = line_to_team_dict(line)
            if team_id == team_dict["id"]:
                team = team_dict
                break

    team_member_mean = {
        member["id"]: {"name": member["name"], "category": member["category"]}
        for member in team["members"]
    }

    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            dict_line = line_to_evaluation_dict(line)
            if team_id == dict_line["id_team"]:
                if team_member_mean[dict_line["evaluated_id"]].get("mean", None) is None:
                    member_mean = mean_grades(team_id, dict_line["evaluated_id"])
                    team_member_mean[dict_line["evaluated_id"]]["mean"] = member_mean

    questions = evaluation_form(show=False)
    members_to_list = team_member_mean

    if LT:
        members_to_list = {
            id: item
            for id, item in team_member_mean.items()
            if item["category"] == "LIDER"
        }
    for item in members_to_list.values():
        if "mean" not in item:
            magenta_print(
                f'\n{item["name"]} ({CATEGORIES[item["category"]]}) ainda não foi avaliado.'
            )
            continue
        blue_bright_print(
            f"\n          Médias de {item['name']} - {CATEGORIES[item['category']]}\n"
        )
        for n, question in enumerate(questions):
            bright_print(f'{questions[question]["question"]}', end=" ")
            if item["mean"][0][n] > 2:
                green_print(f'{item["mean"][0][n]}')
            elif item["mean"][0][n] == 2:
                magenta_print(f'{item["mean"][0][n]}')
            else:
                red_print(f'{item["mean"][0][n]}')
        if item["mean"][1] >= 2:
            green_print(f'\nMédia total: {item["mean"][1]}\n')
        elif item["mean"][1] == 2:
            magenta_print(f'\nMédia total: {item["mean"][1]}\n')
        else:
            red_print(f'\nMédia total: {item["mean"][1]}\n')


def print_mean_grades_FC(team):
    lista = []
    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            dict_line = line_to_evaluation_dict(line)
            if team == dict_line["id_team"]:
                if dict_line["evaluated_category"] == "PRODU":
                    if dict_line["evaluated_id"] not in [item[0] for item in lista]:
                        po_mean = mean_grades(team, dict_line["evaluated_id"])
                        lista.append(
                            (
                                dict_line["evaluated_id"],
                                dict_line["evaluated_name"],
                                po_mean,
                            )
                        )

    if len(lista) < 1:
        magenta_print("\nO PO desse time ainda não foi avaliado.")

    questions = evaluation_form(show=False)
    for item in lista:
        blue_bright_print(f"\n          Médias de {item[1]}\n")
        for n, question in enumerate(questions):
            bright_print(f'{questions[question]["question"]}', end=" ")
            if item[2][0][n] > 2:
                green_print(f"{item[2][0][n]}")
            elif item[2][0][n] == 2:
                magenta_print(f"{item[2][0][n]}")
            else:
                red_print(f"{item[2][0][n]}")
        if item[2][1] >= 2:
            green_print(f"\nMédia total: {item[2][1]}\n")
        elif item[2][1] == 2:
            magenta_print(f"\nMédia total: {item[2][1]}\n")
        else:
            red_print(f"\nMédia total: {item[2][1]}\n")


def run_evaluation():
    user, groups = search_groups()
    av_user, team = select_group(user, groups)
    sprint = get_opened_sprint(team['id'])
    if av_user is None or team is None:
        return
    evaluation_form(user, av_user, team, sprint)


def run_mean_grades():
    user, groups = search_groups()
    av_user, team = select_group(user, groups, select_member=False)

    if user["type"] == 'COMUM':
        print_mean_grades(team['id'], user)

    elif user["id"] == team['turma']['group_leader']['id']:
        only_LT = [
            "Ver somente as médias dos Líderes Técnicos",
            "Ver as notas de todo o time",
        ]
        blue_bright_print("\n       Selecione uma opção:".center(60))
        for indice, item in enumerate(only_LT):
            print(f"     {indice+1}. {item}")
        awnser = int(input("\n   Opção: "))
        while awnser != 1 and awnser != 2:
            awnser = int(input("\n   Opção: "))
        if awnser == 1:
            print_mean_grades_LG(team['id'], LT=True)
        elif awnser == 2:
            print_mean_grades_LG(team['id'])

    elif user["id"] == team['turma']['fake_client']['id']:
        print_mean_grades_FC(team['id'])


if __name__ == "__main__":
    run_evaluation()
    run_mean_grades()
