from ..utils import generate_id

from ..users.repository import _search_users

from .common import create_team_dict
from .persistence import read_teams, write_teams


_teams = []


def reload_teams():
    global _teams 
    _teams = read_teams()


def update_teams():
    write_teams(_teams)


def get_teams():
    if len(_teams) == 0:
        reload_teams()    
    return _teams


def get_teams_from_turma(turma):
    teams = []
    for team in get_teams():
        if team["turma"]["id"] == turma["id"]:
            teams.append(team)
    return teams


def create_team(name, turma, members):
    id = generate_id()
    team = create_team_dict(
        id,
        name,
        turma,
        members,
    )
    get_teams().append(team)
    update_teams()
    return team


def delete_team(team):
    get_teams().remove(team)
    update_teams()


def search_teams(search_term):
    search_term = search_term.lower()
    teams_found = []
    for team in get_teams():
        if (
            search_term in team["id"].lower()
            or search_term in team["name"].lower()
            or search_term in team["turma"]["name"].lower()
            or search_term in team["turma"]["group_leader"]["name"].lower()
            or search_term in team["turma"]["fake_client"]["name"].lower()
        ):
            teams_found.append(team)
    return teams_found


def search_members(search_term, team):
    return _search_users(search_term, team["members"])
