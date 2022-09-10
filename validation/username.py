import re


def get_input_name():
    "Input nome"
    return str(input('Digite o nome: '))


def name_has_valid_characters(name):
    "Verifica se tem caracteres especiais."
    return re.match('^[a-zA-Z0-9_]+$', name)


def is_name_valid(name):
    """
    Retorna True ou False. Verifica se o nome é valido ou não.
    Validações:
        - deve conter mais de 2 caracteres
        - não pode começar com número
        - não pode conter caracteres especiais, exceto underline "_"
    """
    if len(name) <= 2:
        print('O nome deve ter mais de 2 caracteres. Tente novamente!')
        return False
    elif not name_has_valid_characters(name):
        print('Formato inválido. Tente novamente!')
        return False
    elif re.match('\d', name[0]):
        print('Nomes não podem começar com número')
        return False
    else:
        return True


def validate():
    """
    Loop pedindo para o usuário inserir o nome caso
    o nome seja inválido.
    """
    input_name = get_input_name()

    while not is_name_valid(input_name):
        input_name = get_input_name()

    return input_name


if __name__ == '__main__':
    # test
    name = validate()
    print(name)
