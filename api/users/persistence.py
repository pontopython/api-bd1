import os

from .common import create_user_dict

USERS_FILE = "data/users.txt"

os.makedirs("data", exist_ok=True)
if not os.path.exists(USERS_FILE):
    open(USERS_FILE, "a").close()


def user_dict_to_line(user):
    id = user["id"]
    name = user["name"]
    email = user["email"]
    password = user["password"]
    type = user["type"]

    return f"{id};{name};{email};{password};{type}"


def line_to_user_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    email = splitted_line[2]
    password = splitted_line[3]
    type = splitted_line[4]

    return create_user_dict(id, name, email, password, type)


def write_users(users):
    file = open(USERS_FILE, "w")
    lines = [user_dict_to_line(user) + "\n" for user in users]
    file.writelines(lines)
    file.close()


def read_users():
    file = open(USERS_FILE, "r")
    users = [line_to_user_dict(line) for line in file.readlines()]
    file.close()
    return users