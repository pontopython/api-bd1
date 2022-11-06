import re


def validate_turma_name(name):
    valid = True
    errors = []

    if len(name) <= 3:
        valid = False
        errors.append("O nome deve conter mais de 2 caracteres.")

    if not re.match("^[A-zÀ-ú ]+$", name):
        valid = False
        errors.append("O nome contém caracteres inválidos.")

    return valid, errors
