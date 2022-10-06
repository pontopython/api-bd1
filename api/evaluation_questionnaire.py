from traceback import print_tb
from unicodedata import name
from utils import blue_bright_print, red_print, cyan_print, green_print, bright_print, magenta_print
from teams import search_teams_on_file_by_name, generate_teams_list, line_to_team_dict
from login import get_logged_user_id_from_file
from users import search_user_on_file_by_id


categories = {
    'PO': 'Product Owner',
    'LT': 'Líder Técnico',
    'MT':  'Membro do time'
}

def get_logged_user():
    id = get_logged_user_id_from_file()
    return search_user_on_file_by_id(id)


def search_teams_on_file_by_user(user):
    file = open('data/teams.txt', "r")
    teams = []

    for line in file:
        team = line_to_team_dict(line)
        if user in team["members"]:
            teams.append(team["name"])

    file.close()
    for name in teams:
        print(name)

    return teams


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


def evaluation_form(user):
    print(f"\n     Avaliação de {user['name']}\n")
    questions = {
        '1': {
            'question': "Trabalho em equipe, cooperação e descentralização de conhecimento:",
            'answers': {'0': 'Muito Ruim', '1': 'Ruim', '2': 'Regular', '3': 'Bom', '4': 'Muito Bom'},
        },
        '2': {
            'question': "Iniciativa e proatividade:",
            'answers': {'0': 'Muito Ruim', '1': 'Ruim', '2': 'Regular', '3': 'Bom', '4': 'Muito Bom'},
        },
        '3': {
            'question': "Autodidaxia e agregação de conhecimento ao grupo:",
            'answers': {'0': 'Muito Ruim', '1': 'Ruim', '2': 'Regular', '3': 'Bom', '4': 'Muito Bom'},
        },
        '4': {
            'question': "Entrega de resultados e participação efetiva no projeto:",
            'answers': {'0': 'Muito Ruim', '1': 'Ruim', '2': 'Regular', '3': 'Bom', '4': 'Muito Bom'},
        },
        '5': {
            'question': "Competência técnica:",
            'answers': {'0': 'Muito Ruim', '1': 'Ruim', '2': 'Regular', '3': 'Bom', '4': 'Muito Bom'},
        }
    }
    return questions


def show_questions(questions):
    lista = []
    for qk, qv in questions.items():
        print('\n', f'{qk}:{qv["question"]}')

        print('\nEscolha entre as opções indicadas:\n')
        for ak, av in qv['answers'].items():
            print(f'[{ak}]:{av}')

        answers_user = int(input('\nOpção:'))
        while answers_user < 0 or answers_user > 4:
            print('\nOpção inválida! Tente novamente.\n')
            answers_user = int(input('\nOpção:'))
        lista.append(answers_user)
    
    print (lista)
    return lista
    


if __name__ == '__main__':
    user_log = get_logged_user()
    search_teams_on_file_by_user(user_log)
    av_user = select_team()
    questions = evaluation_form(av_user)
    show_questions(questions)
