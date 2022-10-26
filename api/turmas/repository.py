#FUNCIONALIDADES A SEREM IMPLEMENTADAS:
#   1 - Listar turmas
#   2 - Editar turma
#   3 - Excluir turma (?)


def create_alunos_list():
    file = open(USERS_FILE, "r")
    lista_alunos = []
    for line in file:
        user = line_to_user_dict(line)
        if user["type"] == "COMUM":
            lista_alunos.append(user)
    file.close()
    return lista_alunos