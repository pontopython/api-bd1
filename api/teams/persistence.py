

TEAMS_FILE = "data/teams.txt"

def team_dict_to_line(team):
    team_id = team["id"]
    name = team["name"]
    members = [f"{member['category']}:{member['id']}" for member in team["members"]]
    members_categories_and_ids = ",".join(members)
    return f"{team_id};{name};{members_categories_and_ids}"

def line_to_team_dict(line):
    splitted_line = line.rstrip("\n").split(";")
    id = splitted_line[0]
    name = splitted_line[1]
    members_categories_and_ids = splitted_line[2].split(",")
    members = []
    for member_category_and_id in members_categories_and_ids:
        category, id = member_category_and_id.split(":")
        user = search_user_on_file_by_id(id)
        user["category"] = category
        members.append(user)
    team_dict = {"id": id, "name": name, "members": members}
    return team_dict

def write_teams(teams):
    file = open(TEAMS_FILE, "w")
    lines = [team_dict_to_line(team) + "\n" for team in teams]
    file.writelines(lines)
    file.close()

def read_teams():
    file = open(TEAMS_FILE, "r")
    teams = [line_to_team_dict(line) for line in file.readlines()]
    file.close()
    return teams