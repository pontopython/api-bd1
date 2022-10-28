import re


def validate_user_name(name):
    valid = True
    errors = []

    if len(name) <= 2:
        valid = False
        errors.append("O nome deve conter mais de 2 caracteres.")

    if not re.match("^[A-zÀ-ú ]+$", name):
        valid = False
        errors.append("O nome contém caracteres inválidos.")

    return valid, errors


def validate_user_password(password):
    valid = True
    errors = []

    if len(password) < 8:
        valid = False
        errors.append("A senha deve conter mais de 8 caracteres.")

    if re.match(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password
    ):
        valid = False
        errors.append("A senha não contém todos os atributos necessários.")

    return valid, errors
