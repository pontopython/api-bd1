import uuid

from .users import (
    USERS_FILE,
    generate_users_list,
    line_to_user_dict,
    search_user_on_file_by_id,
)
from .utils import blue_bright_print, red_print, cyan_print, green_print, bright_print, magenta_print, bright_input
from .validation import prompt_for_edit_team_search_type, prompt_for_valid_email, prompt_for_valid_team_name, prompt_for_user_search_type, prompt_for_confirmation

TEAMS_FILE = "data/teams.txt"


def create_team_dict(id, name, members):
    return {"id": id, "name": name, "members": members}


def prompt_for_team_members():
    all_users = generate_users_list()
    members = []
    while True:
        bright_print("\n      Adicionar Usuário")
        email = prompt_for_valid_email()
        member = None
        for user in all_users:
            if user["email"] == email:
                member = user
                members.append(member)
                break
        if not member:
            red_print("         Usuário não encontrado.")

        asking = input("\n      Deseja adicionar mais um usuário? ").lower()
        if asking == "n" or asking == "nao" or asking == "não":
            break

    return members


def create_team_interactively():
    cyan_print("\n      Formulário de Criação de Time\n")

    name = prompt_for_valid_team_name()
    members = prompt_for_team_members()
    if not has_team_valid_members(members):
        magenta_print(
            "         O time precisa ter pelo menos um Líder técnico e um Product Owner")
        return create_team_interactively()
    team_dict = create_team_dict(uuid.uuid4(), name, members)
    save_team_to_file(team_dict)


def has_team_valid_members(members):
    """
    Verifica se o time tem pelo menos 1 Líder Técnico e 1 PO
    """
    needed_categories = set(["LT", "PO"])
    category_of_members = set([member["category"] for member in members])
    return needed_categories.issubset(category_of_members)


def save_team_to_file(team):
    file = open(TEAMS_FILE, "a")
    line = team_dict_to_line(team)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("\n             Time salvo com sucesso!")


def print_team_members(name):
    found_team = None
    with open(TEAMS_FILE, "r") as file:
        for line in file:
            team_dict = line_to_team_dict(line.rstrip())

            if name == team_dict["name"]:
                found_team = team_dict
                break

        if not found_team:
            red_print("         Time não encontrado!\n")
            return

    members = []

    with open(USERS_FILE, "r") as file:
        for line in file:
            user_dict = line_to_user_dict(line)
            if user_dict["id"] in found_team["members_id"]:
                members.append({**user_dict, "password": "****"})

    print("Time: ", found_team["name"])
    for member in members:
        print(member["name"], member["category"])


def team_dict_to_line(team):
    team_id = team["id"]
    name = team["name"]
    members = [member["id"] for member in team["members"]]
    members_id = ",".join(members)
    return f"{team_id};{name};{members_id}"


def line_to_team_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    members_id = splitted_line[2].split(",")
    members = []
    for member_id in members_id:
        user = search_user_on_file_by_id(member_id)
        members.append(user)
    team_dict = {"id": id, "name": name, "members": members}
    return team_dict


def search_teams_on_file_by_name(name):
    file = open(TEAMS_FILE, "r")
    teams = []

    for line in file:
        team = line_to_team_dict(line)
        if name.lower() in team["name"].lower():
            teams.append(team)

    file.close()
    return teams


def search_team_on_file_by_name(name):
    file = open(TEAMS_FILE, "r")

    for line in file:
        team = line_to_team_dict(line)
        if name.lower() in team["name"].lower():
            file.close()
            return team


def detail_team(team):
    id = team["id"]
    team_name = team["name"]

    blue_bright_print("\n     Detalhes do Time")
    print(f"         Id: {id}")
    print(f"         Nome: {team_name}")

    print("\n      Membros:")
    for member in team["members"]:
        category = member["category"]
        name = member["name"]
        email = member["email"]
        print(f"         - {category}: {name} <{email}>")


def find_and_show_team():
    name = input("         Qual nome do time? ")
    teams = search_team_on_file_by_name(name)

    if len(teams) == 0:
        red_print("         Nenhum time encontrado!\n")
    else:
        for team in teams:
            detail_team(team)


def generate_teams_list():
    file = open(TEAMS_FILE, "r")
    teams_list = []
    for line in file:
        team = line_to_team_dict(line)
        teams_list.append(team)
    file.close()
    return teams_list


def list_all_teams():
    print("\n----------")
    blue_bright_print("      Todos os Times:")
    teams_list = generate_teams_list()
    for team in teams_list:
        detail_team(team)
        print()
        print("\n")
    print("----------\n")


def find_by_name():
    name = bright_input("         Qual o nome do Time? ")
    team = search_team_on_file_by_name(name)
    return team

# def change_team_name():
#     name = input("         Qual o nome atual do Time? ")
#     team = search_teams_on_file_by_name(name)
#     return team
#     new_name = input ("         Qual o novo nome do Time? ")


def find_and_delete_team():
    team = find_by_name()
    if team is None:
        red_print("\n         Time não encontrado!")
    else:
        with open(TEAMS_FILE, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                file_team = line_to_team_dict(line)
                if team["id"] == file_team["id"]:
                    team_name = team["name"]
                    cyan_print(
                        f"\n\t\tTime {team_name} encontrado!")

                    confirmation = prompt_for_confirmation(f"""
                    Tem certeza que gostaria de excluir o time {team_name}?
                    1 - Sim
                    2 - Não
                    """)
                    if confirmation:
                        lines.pop(index)
                        write_file = open(TEAMS_FILE, 'w')
                        write_file.writelines(lines)
                        file.close()
                        write_file.close()
                        green_print(
                            f"\n             Usuário excluído com sucesso!")

                    break


def change_team_name():
    input("Qual nome atual do time?")


def edit_team():
    options = {
        1: change_team_name,
        2: prompt_for_team_members
        # 3: delete_user,
        # 4: mudar função do usuario ?
    }
    option = prompt_for_edit_team_search_type(option)
    edit = option()

    if edit == 1:
        change_team_name()
    else:
        prompt_for_team_members()
