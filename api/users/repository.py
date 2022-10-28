from ..utils import generate_id
from .common import USER_TYPES, create_user_dict
from .persistence import read_users, write_users

_users = []


def reload_users():
    global _users
    _users = read_users()


def update_users():
    write_users(_users)


def get_users():
    if len(_users) == 0:
        reload_users()
    return _users


def get_instructors():
    instructors = []
    for user in get_users():
        if user["type"] == "INSTR":
            instructors.append(user)
    return instructors


def create_user(name, email, password, type):
    id = generate_id()
    user = create_user_dict(
        id,
        name,
        email,
        password,
        type
    )
    get_users().append(user)
    update_users()
    return user


def delete_user(user):
    get_users().remove(user)
    update_users()


def _get_first_user_by(field, value, users):
    for user in users:
        if value == user[field]:
            return user
    return None


def get_first_user_by(field, value):
    return _get_first_user_by(field, value, get_users())


def get_first_instructor_by(field, value):
    return _get_first_user_by(field, value, get_instructors())


def get_user_by_id(id):
    return get_first_user_by("id", id)


def get_users_by(field, value):
    users = []
    for user in get_users():
        if value == user[field]:
            users.append(user)
    return users


def search_users_by(field, value):
    users = []
    for user in get_users():
        if value.lower() in user[field].lower() or user[field].lower() in value.lower():
            users.append(user)
    return users


def _search_users(search_term, users):
    search_term = search_term.lower()
    users = []
    for user in users:
        if (
            search_term in user["id"].lower()
            or search_term in user["name"].lower()
            or search_term in user["email"].lower()
            or search_term in user["type"].lower()
            or search_term in USER_TYPES[user["type"]].lower()
        ):
            users.append(user)
    return users


def search_users(search_term):
    return _search_users(search_term, get_users())


def search_instructors(search_term):
    return _search_users(search_term, get_instructors())
