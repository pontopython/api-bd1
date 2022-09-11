

def create_user_dict(id, name, email, password):
    return {
        "id": id,
        "name": name,
        "email": email,
        "password": password
    }


def user_dict_to_line(user):
    id = user["id"]
    name = user["name"]
    email = user["email"]
    password = user["password"]

    return f"{id};{name};{email};{password}"


def line_to_user_dict(line):
    splited_line = line.split(";")
    id = int(splited_line[0])
    name = splited_line[1]
    email = splited_line[2]
    password = splited_line[3]

    return create_user_dict(id, name, email, password)


def create_user_interactively():
    print("\nFormulário de Criação de Usuário")
    id = int(input("Id: "))
    name = input("Nome: ")
    email = input("Digite o E-mail: ")
    import stdiomask
    password = stdiomask.getpass(prompt="Digite a senha: ", mask="*")

    return create_user_dict(id, name, email, password)


def save_user_to_file(user):
    file = open("data/users.txt", "a")
    line = user_dict_to_line(user)
    file.write(line)
    file.write("\n")
    file.close()
    print("Usuário salvo com sucesso!")


def search_user_on_file(id):
    file = open("data/users.txt", "r")

    for line in file:
        user = line_to_user_dict(line)
        if id == user["id"]:
            file.close()
            return user

    file.close()
    return None


def detail_user(user):
    id = user["id"]
    name = user["name"]
    email = user["email"]

    print("Detalhes do Usuário")
    print(f"Id: {id}")
    print(f"Nome: {name}")
    print(f"Email: {email}")


def find_and_show_user():
    id = int(input("Qual o id do usuário? "))
    user = search_user_on_file(id)

    if user is None:
        print("Usuário não encontrado!")
    else:
        detail_user(user)


if __name__ == "__main__":
    while True:
        print("Menu Principal")
        print("1 - Criar usuário")
        print("2 - Buscar usuário")
        print("3 - Sair")

        option = int(input("Digite sua opção: "))

        if option == 1:
            user = create_user_interactively()
            save_user_to_file(user)
        elif option == 2:
            find_and_show_user()
        elif option == 3:
            break
        else:
            print("Opção inválida!")
            option = int(input("Digite sua opção: "))
        print("\n")
