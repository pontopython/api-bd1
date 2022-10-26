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


def get_first_user_by(field, value):
    for user in get_users():
        if value == user[field]:
            return user
    return None


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


def search_users(search_term):
    search_term = search_term.lower()
    users = []
    for user in get_users():
        if (
            search_term in user["id"].lower()
            or search_term in user["name"].lower()
            or search_term in user["email"].lower()
            or search_term in user["type"].lower()
            or search_term in USER_TYPES[user["type"]].lower()
        ):
            users.append(user)
    return users