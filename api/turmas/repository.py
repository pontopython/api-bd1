from ..utils import generate_id
from ..users.repository import _search_users

from .common import create_turma_dict
from .persistence import read_turmas, write_turmas
from ..users.repository import _search_users


_turmas = []


def reload_turmas():
    global _turmas 
    _turmas = read_turmas()


def update_turmas():
    write_turmas(_turmas)


def get_turmas():
    if len(_turmas) == 0:
        reload_turmas()    
    return _turmas


def get_turmas_from_user(user):
    turmas = []
    for turma in get_turmas():
        students_ids = [student["id"] for student in turma["students"]]
        if (
            turma["group_leader"]["id"] == user["id"]
            or turma["fake_client"]["id"] == user["id"]
            or user["id"] in students_ids
        ):
            turmas.append(turma)
    return turmas


def create_turma(name, group_leader, fake_client, students):
    id = generate_id()
    user = create_turma_dict(
        id,
        name,
        group_leader,
        fake_client,
        students,
    )
    get_turmas().append(user)
    update_turmas()
    return user


def delete_turma(turma):
    get_turmas().remove(turma)
    update_turmas()


def get_first_turma_by(field, value):
    for turma in get_turmas():
        if value == turma[field]:
            return turma
    return None

def get_turma_by_id(id):
    return get_first_turma_by("id", id)


def get_turmas_by(field = None, value = None, dict_field = None, function = None):
    turmas = []
    for turma in get_turmas():
        if function:
            if function(turma, value):
                turmas.append(turma)
        elif value == turma[field] or (dict_field and value == turma[field][dict_field]):
            turmas.append(turma)
    return turmas


def search_turmas_by(field, value):
    turmas = []
    for turma in get_turmas():
        if value.lower() in turma[field].lower() or turma[field].lower() in value.lower():
            turmas.append(turma)
    return turmas


def search_turmas(search_term):
    search_term = search_term.lower()
    turmas = []
    for turma in get_turmas():
        if (
            search_term in turma["id"].lower()
            or search_term in turma["name"].lower()
            or search_term in turma["group_leader"]["name"].lower()
            or search_term in turma["fake_client"]["name"].lower()
        ):
            turmas.append(turma)
    return turmas


def search_students(search_term, turma):
    return _search_users(search_term, turma["students"])
