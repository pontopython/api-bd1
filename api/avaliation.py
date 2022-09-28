from unicodedata import category
from teams import search_teams_on_file_by_name

categories = {
    'PO': 'Product Owner',
    'LT': 'Líder Técnico',
    'MT':  'Membro do time'
}

def select_team():
    input_team = input('Qual time deseja avaliar? ')
    team = search_teams_on_file_by_name(input_team)
    return select_team_member(team)
        
def select_team_member(team):
    for indice, member in enumerate(team['members']):
        print(f'{indice+1}. {categories[member["category"]].ljust(20," ")}{member["name"]}')
    input_member = int(input('Qual membro deseja avaliar? '))
    if input_member > 0 and input_member <= len(team['members']):
        return team['members'][input_member-1]
    else:
        print('Usuário inválido. Tente novamente!')
        return select_team_member(team)


if __name__ == '__main__':
    select_team()