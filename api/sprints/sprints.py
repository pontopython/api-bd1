from api.login import get_logged_user
from ..turmas.tui import select_leader_group
from ..teams.tui import select_team
from .repository import create_sprint, search_sprint_by, update_sprint

def has_opened_sprint(team_id):
    sprints = search_sprint_by("team_id", team_id)
    opened_sprints = [sprint for sprint in sprints if sprint['status'] == 'aberta']

    return len(opened_sprints) > 0

def select_sprint_tui(team_id):
    sprints = search_sprint_by("team_id", team_id)
    
    for index, sprint in enumerate(sprints):
        print(f'{index + 1}. {sprint["id"]} - {sprint["status"]}')
    
    input_sprint = int(input("Qual sprint deseja selecionar? "))

    if input_sprint > 0 and input_sprint <= len(sprints):
        sprint = sprints[input_sprint - 1]
        return sprint
    else:
        print("Opção inválida. Tente novamente!")
        return select_sprint_tui(team_id)


def close_sprint_tui():
    user = get_logged_user()
    id = user['id']

    selected_group = select_leader_group(id)

    if selected_group is None:
        return

    selected_group_team_ids = selected_group['teams']
    selected_team = select_team(selected_group_team_ids)

    selected_sprint = select_sprint_tui(selected_team['id'])
    selected_sprint['status'] = 'fechada'
    update_sprint('id', selected_sprint['id'], selected_sprint)

def create_sprint_tui():
    user = get_logged_user()
    id = user['id']

    selected_group = select_leader_group(id)

    if selected_group is None:
        print("Deu ruim")
        return

    selected_group_team_ids = selected_group['teams']
    selected_team = select_team(selected_group_team_ids)

    if has_opened_sprint(selected_team['id']):
        print("Já existe uma sprint aberta.")
        return

    sprint = create_sprint(selected_team['id'])
    return sprint

if __name__ == '__main__':
    create_sprint_tui()
    close_sprint_tui()
