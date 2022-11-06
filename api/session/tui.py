import stdiomask

from ..users.prompt import prompt_user_email
from ..users.repository import get_user_by_email
from ..turmas.tui import select_turma_from_user
from ..teams.repository import get_team_from_turma_and_student

from .current import get_session, update_session

def summary_session(session):
    user_name = session["user"]["name"]

    if session["turma"] is None:
        turma_name = "-"
    else:
        turma_name = session["turma"]["name"]

    if session["team"] is None:
        team_name = "-"
    else:
        team_name = session["team"]["name"]

    return f"{user_name} (Turma: {turma_name}, Time: {team_name})"

def login():
    email = prompt_user_email()
    user = get_user_by_email(email)
    if user is None:
        print("Usuário não encontrado!")
        return

    password = stdiomask.getpass(prompt="Senha: ", mask="*")
    if password != user["password"]:
        print("Credenciais inválidas!")
        return

    turma = select_turma_from_user(user)

    if turma is None:
        team = None
    else:
        team = get_team_from_turma_and_student(turma, user)

    session = get_session()
    session["user"] = user
    session["turma"] = turma
    session["team"] = team

    update_session()
