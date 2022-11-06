import os

from ..users.repository import get_user_by_id
from ..turmas.repository import get_turma_by_id
from ..teams.repository import get_team_by_id
from .common import session_dict

SESSION_FILE = "data/session.txt"

os.makedirs("data", exist_ok=True)
if not os.path.exists(SESSION_FILE):
    open(SESSION_FILE, "a").close()

current_session = None


def session_dict_to_line(session):
    if session["user"] is None:
        return ""

    user_id = session["user"]["id"]
    
    if session["turma"] is None:
        turma_id = ""
    else:
        turma_id = session["turma"]["id"]
    
    if session["team"] is None:
        team_id = ""
    else:
        team_id = session["team"]["id"]

    return f"{user_id};{turma_id};{team_id}"


def session_line_to_dict(line):
    if line == "":
        return session_dict(None, None, None)

    splitted_line = line.rstrip("\n").split(";")
    user_id = splitted_line[0]
    turma_id = splitted_line[1]
    team_id = splitted_line[2]

    user = get_user_by_id(user_id)
    turma = get_turma_by_id(turma_id)
    team = get_team_by_id(team_id)

    return session_dict(user, turma, team)


def write_session(session):
    file = open(SESSION_FILE, "w")
    file.write(session_dict_to_line(session))
    file.close()


def read_session():
    file = open(SESSION_FILE, "r")
    line = file.readline()
    file.close()
    return session_line_to_dict(line)
