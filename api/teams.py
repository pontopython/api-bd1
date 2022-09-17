import uuid
from users import line_to_user_dict
from validation import prompt_for_valid_category, prompt_for_valid_username, prompt_for_valid_email, prompt_for_valid_team_name



def create_team_dict(id, team_name, members): #members = [{"nome": "nome do membro", "funcao": "funcao do membro"},...]
    return {
        "id": id,
        "team_name": team_name,
        "members": members
    }

def prompt_for_team_members():
    members = []
    while True:
        with open('users.txt', 'r') as file:
            category = prompt_for_valid_category()
            name = prompt_for_valid_username()
            email = prompt_for_valid_email()
            member = None
            for line in file:
                user = line_to_user_dict(line)
                if user["name"] == name and user["email"] == email and user["category"] == category:
                    member = {
                        "id" : user["id"],
                        "category": category,
                        "name": name,
                        "email": email,
                    }
                    members.append(member)
                    break
            if not member:
                print('Usuário não encontrado.')
            
            asking = input('Deseja continuar?').lower()
            if asking == 'n'or asking == 'nao' or asking == 'não':
                break
    return members



def create_team_interactively():
    print("\nFormulário de Criação de Time\n")

    team_name = prompt_for_valid_team_name()
    members = prompt_for_team_members()
    if not has_team_valid_members(members):
        print("O time precisa ter pelo menos um Líder técnico e um Product Owner")
        return create_team_interactively()
    team_dict = create_team_dict(uuid.uuid4(), team_name, members)
    save_team_to_file(team_dict)

def has_team_valid_members(members):
    """
    Verifica se o time tem pelo menos 1 Líder Técnico e 1 PO
    """
    needed_categories = set(['LT', 'PO'])
    category_of_members = set([member['category'] for member in members])
    return needed_categories.issubset(category_of_members)

def save_team_to_file(team):
    file = open("data/teams.txt", "a")
    line = team_dict_to_line(team)
    file.write(line)
    file.write("\n")
    file.close()
    print("Time salvo com sucesso!")

def print_team_members(team_name):
    found_team = None
    with open('data/teams.txt', 'r') as file:
        for line in file:
            team_dict = line_to_team_dict(line.rstrip())
            
            if team_name == team_dict["team_name"]:
                found_team = team_dict
                break
    
        if not found_team:
            print("Time não encontrado")
            return
    
    members = []

    with open("data/users.txt", "r") as file:
        for line in file:
            user_dict = line_to_user_dict(line)
            if user_dict["id"] in found_team["members_id"]:
                members.append({**user_dict, "password": "****"})
    
    print("Time: ", found_team["team_name"])
    for member in members:
        print(member["name"], member["category"])



def team_dict_to_line(team):
    team_id = team["id"]
    team_name = team["team_name"]
    members = [member["id"] for member in team["members"]]
    members_id = ','.join(members)
    return f"{team_id};{team_name};{members_id}"

def line_to_team_dict(line):
    splited_line = line.split(";")
    team_id = splited_line[0]
    team_name = splited_line[1]
    members_id = splited_line[2].split(',')
    team_dict = {
        "team_id": team_id,
        "team_name": team_name,
        "members_id": members_id
    }
    return team_dict


if __name__== "__main__":
    time = create_team_interactively()
    print_team_members("aaa")
    
