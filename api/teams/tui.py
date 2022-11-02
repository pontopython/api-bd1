from api.utils import blue_bright_print, bright_input
from ..users.tui import search_and_select_user

from .common import MEMBERSHIP_CATEGORIES
from .repository import *

def summary_team(team):
    name = team["name"]
    members_count = len(team["members"])
    return f"{name} ({members_count} membros)"


def summary_member(member):
    name = member["name"]
    email = member["email"]
    category = member["category"]
    category_description = MEMBERSHIP_CATEGORIES[category]

    return f"{name} <{email}> como {category_description}"


def show_members(team, title="Membros:"):
    print(title)
    for member in team["members"]:
        print(f"    - {summary_member(member)}")


def search_and_select_member(team):
    search_term = input("Procurar: ")
    members = search_members(search_term, team) # TODO: Alec implementa esse método em repository depois

    if len(members) == 0:
        return None

    for index, member in enumerate(members):
        print(f"{index+1} - {summary_member(member)}")

    while True:
        option = int(input("Opção: "))
        if option > 0 and option <= len(members):
            return members[option - 1]
        print("Opção inválida.")


def add_members(team):
    while True:
        should_add = input("Deseja adicionar mais um membro (S/N)? ")
        if should_add == "S" or should_add == "s":
            print("Selecione um Membro")
            new_member = search_and_select_user()
            new_member["category"] = "COMUM"
            team["members"].append(new_member)
        else:
            break


def remove_members(team):
    while True:
        should_add = input("Deseja remover mais um membro (S/N)? ")
        if should_add == "S" or should_add == "s":
            print("Selecione um Membro")
            member_to_remove = search_and_select_member(team)
            team["members"].remove(member_to_remove)
        else:
            break


def detail_team(team, title="Detalhes do Time:"):
    id = team["id"]
    name = team["name"]

    print(title)
    print(f"Id: {id}")
    print(f"Nome: {name}")
    print("Membros:")


def list_teams():
    print("Times:")
    for team in get_teams():
        print(summary_team(team))


def search_and_select_team():
    search_term = input("Procurar: ")
    teams = search_teams(search_term)

    if len(teams) == 0:
        return None

    for index, team in enumerate(teams):
        print(f"{index+1} - {summary_team(team)}")

    while True:
        option = int(input("Opção: "))
        if option > 0 and option <= len(teams):
            return teams[option - 1]
        print("Opção inválida.")


def show_team():
    team = search_and_select_team()
    if team is None:
        print("Nenhum time encontrado.")
        return
    detail_team(team)


def new_user():
    print("Novo Time")
    
    name = input("Nome: ")
    
    print("Selecione um Líder Técnico")
    tech_leader = search_and_select_user()
    tech_leader["category"] = "LIDER"
    
    print("Selecione um Product Owner")
    product_owner = search_and_select_user()
    product_owner["category"] = "PRODU"

    members = [tech_leader, product_owner]

    team = create_team(name, members)
    add_members(team)
    update_teams()


def edit_team():
    print("Editar time")
    team = search_and_select_team()

    if team is None:
        print("Nenhum time encontrado.")
        return

    name = team['name']
    print(f"Nome: {name}")
    should_update = input("Deseja alterar (S/N)? ")
    if should_update == "S" or should_update == "s":
        team["name"] = input("Novo nome: ")
    
    show_members(team)
    add_members(team)

    show_members(team)
    remove_members(team)


def remove_team():
    print("Remover time")
    team = search_and_select_team()
    if team is None:
        print("Nenhum time encontrado.")
        return
    delete_team(team)

def select_team(team_ids: list):
    teams = []

    for team_id in team_ids:
        team = search_team_by("id", team_id)
        teams.append(team)

    blue_bright_print("\n          Selecione um time:")

    for index, team in enumerate(teams):
        print(f'    {index + 1}. {team["name"]}')
    
    input_team = int(bright_input("\nQual time deseja selecionar? "))

    if input_team > 0 and input_team <= len(teams):
        return teams[input_team - 1]
    else:
        red_print("Opção inválida. Tente novamente!")
        return select_team(team_ids)
