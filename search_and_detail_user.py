from create_save import line_to_user_dict
from utils import red_print, blue_bright_print


def search_user_on_file(email):
    file = open("data/users.txt", "r")

    for line in file:
        user = line_to_user_dict(line)
        if email == user["email"]:
            file.close()
            return user

    file.close()
    return None


def detail_user(user):
    id = user["id"]
    category = user["category"]
    name = user["name"]
    email = user["email"]

    blue_bright_print("Detalhes do Usuário")
    print(f"Id: {id}")
    print(f"Categoria: {category}")
    print(f"Nome: {name}")
    print(f"Email: {email}")


def find_and_show_user():
    email = input("Qual o email do usuário? ")
    user = search_user_on_file(email)

    if user is None:
        red_print("Usuário não encontrado!")
    else:
        detail_user(user)


if __name__ == "__main__":
    user = find_and_show_user()
