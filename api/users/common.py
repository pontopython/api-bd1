USER_TYPES = {
    "ADMIN": "Administrador",
    "INSTR": "Instrutor",
    "COMUM": "Usuário Comum",
}


def create_user_dict(id, name, email, password, type):
    return {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "type": type,
    }
