import uuid

from .permissions import current_user_has_permission
from .users import (
    USERS_FILE,
    edit_user_category_on_team,
    generate_users_list,
    line_to_user_dict,
    search_user_on_file_by_id,
    initial_category,
    change_user_category_on_team,
)
from .utils import (
    blue_bright_print,
    bright_input,
    bright_print,
    cyan_print,
    green_print,
    magenta_print,
    red_print,
)
from .validation import (
    prompt_for_confirmation,
    prompt_for_edit_team_search_type,
    prompt_for_valid_email,
    prompt_for_valid_team_name,
    prompt_for_valid_all_category
)

TEAMS_FILE = "data/teams.txt"


def create_team_dict(id, name, members):
    return {"id": id, "name": name, "members": members}


def prompt_for_team_members():
    all_users = generate_users_list()
    members = []
    while True:
        bright_print("\n     Adicionar Usuário")
        email = prompt_for_valid_email()
        member = None
        for user in all_users:
            if user["email"] == email:
                member = user
                member["category"] = prompt_for_valid_all_category()
                members.append(member)
                break
        if not member:
            red_print("\tUsuário não encontrado.")

        asking = bright_input("\n     Deseja adicionar mais um usuário? ").lower()
        if asking == "n" or asking == "nao" or asking == "não":
            break

    return members


def create_team_interactively():
    if not current_user_has_permission("create_teams"):
        red_print("Você não tem permissão para criar times!")
        return

    cyan_print("\n\tFormulário de Criação de Time\n")

    name = prompt_for_valid_team_name()
    members = prompt_for_team_members()
    if not has_team_valid_members(members):
        magenta_print(
            "\tO time precisa ter pelo menos um Líder técnico, um Product Owner, um Fake Client e um Líder do Grupo!"
        )
        return create_team_interactively()
    team_dict = create_team_dict(uuid.uuid4(), name, members)
    save_team_to_file(team_dict)


def has_team_valid_members(members):
    """
    Verifica se o time tem pelo menos 1 Líder Técnico, 1 PO, 1 Líder de Grupo e 1 Fake Client
    """
    needed_categories = set(["LT", "PO", "LG", "FC"])
    category_of_members = set([member["category"] for member in members])
    return needed_categories.issubset(category_of_members)


def save_team_to_file(team):
    file = open(TEAMS_FILE, "a")  # abre arquivo dos times
    line = team_dict_to_line(team)  # transforma time em linha
    file.write(line)  # adiciona no final do arquivo
    file.write("\n")  # adiciona pular uma linha
    file.close()  # salva e fecha arquivo
    green_print("\n\t\tTime salvo com sucesso!")


def find_team_line_number_on_file(team):
    id = team["id"]
    file = open(TEAMS_FILE, "r")  # abre arquivo dos times para leitura
    lines = file.readlines()
    for line_number, line in enumerate(lines):  # enumera cada linha do arquivo
        line_team = line_to_team_dict(line)  # procura um time com mesmo id
        if (
            line_team["id"] == id
        ):  # se o id da linha for o mesmo do time , retorna o numero da linha
            file.close()
            return line_number
    file.close()
    return None


def remove_team_from_file(team):
    read_file = open(TEAMS_FILE, "r")  # abre arquivo para leitura
    lines = read_file.readlines()  # cria lista com as linhas
    read_file.close()
    line_number = find_team_line_number_on_file(team)  # encontra a linha do time
    lines.pop(line_number)  # remove a linha do time da lista
    write_file = open(TEAMS_FILE, "w")  # abre arquivo para escrita
    write_file.writelines(lines)  # escreve as linhas
    write_file.close()  # fecha o arquivo


def update_team_on_file(team):
    remove_team_from_file(team)
    save_team_to_file(team)


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
    members = [f"{member['category']}:{member['id']}" for member in team["members"]]
    members_categories_and_ids = ",".join(members)
    return f"{team_id};{name};{members_categories_and_ids}"


def line_to_team_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    members_categories_and_ids = splitted_line[2].split(",")
    members = []
    for member_category_and_id in members_categories_and_ids:
        category, id = member_category_and_id.split(":")
        user = search_user_on_file_by_id(id)
        user["category"] = category
        members.append(user)
    team_dict = {"id": id, "name": name, "members": members}
    return team_dict


def search_teams_on_file_by_name(name):
    file = open(TEAMS_FILE, "r")
    found_team = None

    for line in file:
        team = line_to_team_dict(line)
        if name.lower() in team["name"].lower():
            found_team = team
            break

    file.close()
    return found_team


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
    if not current_user_has_permission("search_teams"):
        red_print("Você não tem permissão para procurar times!")
        return

    name = input("         Qual nome do time? ")
    team = search_teams_on_file_by_name(name)

    if team is None:
        red_print("         Nenhum time encontrado!\n")
    else:
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
    if not current_user_has_permission("list_teams"):
        red_print("Você não tem permissão para listar times!")
        return

    print("\n----------")
    blue_bright_print("      Todos os Times:")
    teams_list = generate_teams_list()
    for team in teams_list:
        detail_team(team)
        print()
        print("\n")
    print("----------\n")


def find_team_by_name():
    name = bright_input("         Qual o nome do Time? ")
    team = search_team_on_file_by_name(name)
    return team


def find_and_delete_team():
    if not current_user_has_permission("delete_teams"):
        red_print("Você não tem permissão para deletar times!")
        return

    team = find_team_by_name()

    if team is None:
        red_print("\n         Time não encontrado!")
        return
    else:
        team_name = team["name"]
        cyan_print(f"\n\t\tTime {team_name} encontrado!")

        confirmation = prompt_for_confirmation(
            f"""
                    Tem certeza que gostaria de excluir o time {team_name}?
                    1 - Sim
                    2 - Não
                    """
        )
        if confirmation:
            remove_team_from_file(team)

        green_print(f"\n             Time excluído com sucesso!")


def change_team_name():
    team = find_team_by_name()
    if team is None:
        red_print("\n         Time não encontrado!")
        return
    else:
        team_name = team["name"]
        cyan_print(f"\n\t\tTime {team_name} encontrado!")
        team["name"] = prompt_for_valid_team_name()
        update_team_on_file(team)


def add_member_to_a_team():
    team_to_update = find_team_by_name()

    if team_to_update is None:
        red_print("\n         Time não encontrado!")
        return
    else:
        team_name = team_to_update["name"]
        cyan_print(f"\n\t\tTime {team_name} encontrado!")

    new_members = prompt_for_team_members()
    team_to_update["members"] = team_to_update["members"] + new_members
    update_team_on_file(team_to_update)

    green_print("\tUsuário adicionado ao time com sucesso!")


def delete_member_on_a_team():
    search_team = find_team_by_name()

    if search_team is None:
        red_print("\n         Time não encontrado!")
        return
    else:
        team_name = search_team["name"]
        cyan_print(f"\n\t\tTime {team_name} encontrado!")

    email = prompt_for_valid_email()
    filtred_members = []

    for member in search_team["members"]:
        if member["email"] != email:
            filtred_members.append(member)
    search_team["members"] = filtred_members
    update_team_on_file(search_team)


def edit_team():  # colocar pesquisar times para fazer edição
    if not current_user_has_permission("edit_teams"):
        red_print("Você não tem permissão para editar times!")
        return

    options = {
        1: change_team_name,
        2: add_member_to_a_team,
        3: delete_member_on_a_team,
        4: edit_user_category_on_team,
    }
    option = prompt_for_edit_team_search_type(options)
    edit = option()

    if edit == 1:
        change_team_name()
    elif edit == 2:
        add_member_to_a_team()
    elif edit == 3:
        delete_member_on_a_team()
    elif edit == 4:
        edit_user_category_on_team


def change_team_name():
    team = find_team_by_name()

    if team is None:
        red_print("\tTime não encontrado!")
        return

    team_name = team["name"]
    cyan_print(f"\n\t\tTime {team_name} encontrado!")
    team["name"] = prompt_for_valid_team_name(change=True)
    update_team_on_file(team)
