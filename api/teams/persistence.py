from api.teams.common import create_team_dict
from api.turmas.repository import get_turma_by_id
from api.users.repository import get_user_by_id
from ..users.repository import get_user_by_id
from ..turmas.repository import get_turma_by_id

from .common import create_team_dict

TEAMS_FILE = "data/teams.txt"

def team_dict_to_line(team):
    team_id = team["id"]
    name = team["name"]
    turma_id = team["turma"]["id"]
    members = [f"{member['category']}:{member['id']}" for member in team["members"]]
    members_categories_and_ids = ",".join(members)
    return f"{team_id};{name};{turma_id};{members_categories_and_ids}"

def line_to_team_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    team_id = splitted_line[0]
    name = splitted_line[1]
    turma_id = splitted_line[2]
    turma = get_turma_by_id(turma_id)
    members_categories_and_ids = splitted_line[3].split(",")
    members = []
    for member_category_and_id in members_categories_and_ids:
        category, id = member_category_and_id.split(":")
        user = get_user_by_id(id).copy()
        user["category"] = category
        members.append(user)
    return create_team_dict(team_id, name, turma, members)

def write_teams(teams):
    file = open(TEAMS_FILE, "w")
    lines = [team_dict_to_line(team) + "\n" for team in teams]
    file.writelines(lines)
    file.close()

def read_teams():
    file = open(TEAMS_FILE, "r")
    teams = [line_to_team_dict(line) for line in file.readlines()]
    file.close()
    return teams