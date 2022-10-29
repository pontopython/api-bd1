from ..utils import generate_id, red_print

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

def print_team_members(name):
    found_team = None
    teams = []
    for team in get_teams():
        if name == team["name"]:
            found_team = team
            break
    
        if not found_team:
            red_print("         Time não encontrado!\n")
            return
    
    members = []
    for member in get_users():
        if member["id"] in found_team["members_id"]:
            members.append(member)
    print("Time: ", found_team["name"])
    for member in members:
        print(member["name"], member["category"])        

def search_members():
    #teste
    print(get_teams())

def search_team_by(field, value):
    for team in get_teams():
        if value.lower() == team[field].lower():
            return team
