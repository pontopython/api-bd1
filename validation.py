import re


def has_name_valid_characters(name):
    "Verifica se tem caracteres especiais."
    return re.match('^[a-zA-Z0-9_]+$', name)


def is_name_valid(name, show=False):
    """
    Retorna True ou False. Verifica se o nome é valido ou não.
    Validações:
        - deve conter mais de 2 caracteres
        - não pode começar com número
        - não pode conter caracteres especiais, exceto underline "_"
    """
    if len(name) <= 2:
        if show == True:
            print('O nome deve ter mais de 2 caracteres. Tente novamente!')
        return False
    elif not has_name_valid_characters(name):
        if show == True:
            print('Formato inválido. Tente novamente!')
        return False
    elif re.match('\d', name[0]):
        if show == True:
            print('Nomes não podem começar com número')
        return False
    else:
        return True


def prompt_for_valid_username():
    """
    Loop pedindo para o usuário inserir o nome caso
    o nome seja inválido.
    """
    input_name = input('Digite o nome:')

    while not is_name_valid(input_name):
        input_name = input('Digite um nome válido:')

    return input_name


def is_email_valid(email):
    return re.match('^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$', email)


def prompt_for_valid_email():
    input_email = input('Digite o email: ')

    while not is_email_valid(input_email):
        print('E-mail inválido. Digite novamente!')
        input_email = input('Digite o e-mail: ')

    return input_email


def prompt_for_valid_team_name():
    input_team_name = input('Digite o nome do time: ')

    while not is_name_valid(input_team_name):
        input_team_name = input('Digite um nome válido para o time: ')

    return input_team_name


if __name__ == '__main__':
    # test
    name = prompt_for_valid_username()
    email = prompt_for_valid_email()
    team = prompt_for_valid_team_name()
    print(name)
    print(email)
    print(team)
