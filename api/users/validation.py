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

def validate_user_email(email):
    valid = True
    errors = []

    if len(email) <= 2:
        valid = False
        errors.append("O nome deve conter mais de 2 caracteres.")

    if not re.match("^[A-zÀ-ú ]+$", email):
        valid = False
        errors.append("O nome contém caracteres inválidos.")

    return valid, errors


def validate_user_password(password):
    valid = True
    errors = []

    if len(password) < 8:
        valid = False
        errors.append("A senha deve conter mais de 8 caracteres.")

    if not re.search("[A-Z]", password):
        valid = False
        errors.append("A senha deve conter pelo menos uma letra maiúscula.")
        
    if not re.search("[a-z]", password):
        valid = False
        errors.append("A senha deve conter pelo menos uma letra minúscula.")
        
    if not re.search("[0-9]", password):
        valid = False
        errors.append("A senha deve conter pelo menos um número.")

    if not re.search("[\(\)\@\$\!\%\*\?\&\-\+]", password):
        valid = False
        errors.append("A senha deve conter pelo menos um dos caracteres especiais: (, ), @, $, !, %, *, ?, &, -, +")

    return valid, errors
