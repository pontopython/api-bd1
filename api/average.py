import statistics

from api.evaluation import evaluation_form, line_to_evaluation_dict, search_groups, select_group
from api.sprints.tui import select_sprint_tui
from api.utils import blue_bright_print, bright_input, bright_print, green_print, magenta_print, red_print

EVALUATIONS_TXT_FILE =  "data/evaluations.txt"

CATEGORIES = {
    "PRODU": "Product Owner",
    "LIDER": "Líder Técnico",
    "COMUM": "Membro do time",
}


def average_grades(team_id, user_id, sprint=None):
    skills = [[], [], [], [], []]

    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            evaluation = line_to_evaluation_dict(line)
            if sprint is not None:
                if team_id == evaluation["id_team"] and user_id == evaluation["evaluated_id"] and sprint['id'] == evaluation['id_sprint']:
                    skills[0].append(int(evaluation["skill_1"]))
                    skills[1].append(int(evaluation["skill_2"]))
                    skills[2].append(int(evaluation["skill_3"]))
                    skills[3].append(int(evaluation["skill_4"]))
                    skills[4].append(int(evaluation["skill_5"]))
            else:
                if team_id == evaluation["id_team"] and user_id == evaluation["evaluated_id"]:
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


def print_average_grades(team, user, sprint=None):
    average = average_grades(team['id'], user["id"], sprint)
    questions = evaluation_form(show=False)

    if average is None:
        magenta_print("\nVocê ainda não foi avaliado.")
        return

    blue_bright_print(f"\n          Médias de {user['name']}\n")
    for n, question in enumerate(questions):
        bright_print(f'{questions[question]["question"]}')
        if average[0][n] > 2:
            green_print(f"{average[0][n]}")
        elif average[0][n] == 2:
            magenta_print(f"{average[0][n]}")
        else:
            red_print(f"{average[0][n]}")
    if average[1] >= 2:
        green_print(f"\nMédia total: {average[1]}\n")
    elif average[1] == 2:
        magenta_print(f"\nMédia total: {average[1]}\n")
    else:
        red_print(f"\nMédia total: {average[1]}\n")


def print_average_grades_LG(team, sprint=None, LT=False):
    
    team_member_average = {
        member["id"]: {"name": member["name"], "category": member["category"]}
        for member in team["members"]
    }

    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            dict_line = line_to_evaluation_dict(line)
            if team['id'] == dict_line["id_team"]:
                if team_member_average[dict_line["evaluated_id"]].get("average", None) is None:
                    member_average = average_grades(team['id'], dict_line["evaluated_id"], sprint)
                    team_member_average[dict_line["evaluated_id"]]["average"] = member_average

    questions = evaluation_form(show=False)
    members_to_list = team_member_average

    if LT:
        members_to_list = {
            id: item
            for id, item in team_member_average.items()
            if item["category"] == "LIDER"
        }
    for item in members_to_list.values():
        if "average" not in item:
            magenta_print(
                f'\n{item["name"]} ({CATEGORIES[item["category"]]}) ainda não foi avaliado.'
            )
            continue
        blue_bright_print(
            f"\n          Médias de {item['name']} - {CATEGORIES[item['category']]}\n"
        )
        for n, question in enumerate(questions):
            bright_print(f'{questions[question]["question"]}', end=" ")
            if item["average"][0][n] > 2:
                green_print(f'{item["average"][0][n]}')
            elif item["average"][0][n] == 2:
                magenta_print(f'{item["average"][0][n]}')
            else:
                red_print(f'{item["average"][0][n]}')
        if item["average"][1] >= 2:
            green_print(f'\nMédia total: {item["average"][1]}\n')
        elif item["average"][1] == 2:
            magenta_print(f'\nMédia total: {item["average"][1]}\n')
        else:
            red_print(f'\nMédia total: {item["average"][1]}\n')


def print_average_grades_FC(team, sprint):
    lista = []
    with open(EVALUATIONS_TXT_FILE, "r") as file:
        for line in file:
            dict_line = line_to_evaluation_dict(line)
            if team["id"] == dict_line["id_team"]:
                if dict_line["evaluated_category"] == "PRODU":
                    if dict_line["evaluated_id"] not in [item[0] for item in lista]:
                        po_average = average_grades(team["id"], dict_line["evaluated_id"], sprint)
                        lista.append(
                            (
                                dict_line["evaluated_id"],
                                dict_line["evaluated_name"],
                                po_average,
                            )
                        )

    if len(lista) < 1:
        magenta_print("\nO Product Owner desse time ainda não foi avaliado.")

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


def by_sprint_question(team):
    by_sprint = [
        "Ver as médias por sprint",
        "Ver as médias de todas as sprints"
    ]
    blue_bright_print("\n       Ver médias por sprint?".center(60))
    
    for indice, item in enumerate(by_sprint):
        print(f"     {indice+1}. {item}")
    awnser_sprint = int(bright_input("\n   Opção: "))
    
    while awnser_sprint != 1 and awnser_sprint != 2:
        awnser_sprint = int(bright_input("\n   Opção: "))
    
    if awnser_sprint == 1:
        sprint = select_sprint_tui(team['id'], closed=True)
    
    elif awnser_sprint == 2:
        sprint = None
    
    return sprint


def run_average_grades():
    user, groups = search_groups()
    av_user, team = select_group(user, groups, select_member=False)
    sprint = by_sprint_question(team)
    
    if user["type"] == 'COMUM':
        print_average_grades(team, user, sprint)

    elif user["type"] == 'ADMIN':
        print_average_grades_LG(team, sprint)

    elif user["id"] == team['turma']['group_leader']['id']:
        only_LT = [
            "Ver somente as médias dos Líderes Técnicos",
            "Ver as notas de todo o time",
        ]
        blue_bright_print("\n       Quais médias quer ver?".center(60))
        for indice, item in enumerate(only_LT):
            print(f"     {indice+1}. {item}")
        awnser = int(input("\n   Opção: "))
        while awnser != 1 and awnser != 2:
            awnser = int(input("\n   Opção: "))
        if awnser == 1:
            print_average_grades_LG(team, sprint, LT=True)
        elif awnser == 2:
            print_average_grades_LG(team, sprint)

    elif user["id"] == team['turma']['fake_client']['id']:
        print_average_grades_FC(team, sprint)


if __name__ == "__main__":
    run_average_grades()