group_name = input("Digite o nome do grupo:")
members = input("Digite nome completo dos integrantes:")
print(group_name)
print(members)


def ler_txt(members):
    arq = open("requirements.txt", 'r')
    category = []
    for category in arq:
        category.append(linha)

    return category

print(ler_txt)

def creat_team_dict (team_name, members):
    return {
        "team_name" : team_name,
        "members" : members,
    }


def creat_team_dict_to_line (creat_team):
    team_name = creat_team_dict["team_name"]
    members = creat_team_dict["members"]

    return f"{team_name};{members};"

def line_to_creat_team_dict (line):
    splited_line = line.split(";")
    team_name = splited_line[0]
    members = splited_line[1]
    

def save_creat_team_to_file(user):
    file = open("data/teams.txt", "a")
    line = creat_team_dict_to_line(user)
    file.write(line)
    file.write("\n")
    file.close()
    print("Equipe criada!") 
