from ..utils import generate_id

from ..users.repository import _search_users

from .common import create_team_dict
from .persistence import read_teams, write_teams
from ..users.repository import get_users


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


def create_team(name, members):
    id = generate_id()
    team = create_team_dict(
        id,
        name,
        members,
    )
    get_teams().append(team)
    update_teams()
    return team


def delete_team(team):
    get_teams().remove(team)
    update_teams()

def search_members(search_term, team):
    return _search_users(search_term, team["members"])

