from api.login import get_logged_user
from api.utils import red_print
from ..turmas.tui import select_leader_group
from ..teams.tui import select_team
from .repository import create_sprint, search_sprint_by, update_sprint


def get_opened_sprint(team_id):
    sprints = search_sprint_by("team_id", team_id)
    opened_sprints = [
        sprint for sprint in sprints if sprint['status'] == 'aberta']

    if len(opened_sprints) > 0:
        return opened_sprints[0]

    return None
        


def has_opened_sprint(team_id):
    opened_sprints = get_opened_sprint(team_id)

    return opened_sprints is not None


def select_sprint_tui(team_id, closed=False):
    sprints = search_sprint_by("team_id", team_id)
    if not closed:
        valid_sprints = sprints
    if closed:
        valid_sprints = []
        for sprint in sprints:
            if sprint['status'] == 'fechada':
                valid_sprints.append(sprint)
    
    for index, sprint in enumerate(valid_sprints):
        print(f'{index + 1}. {sprint["id"]} - {sprint["status"]}')
    
    input_sprint = int(input("Qual sprint deseja selecionar? "))

    if input_sprint > 0 and input_sprint <= len(valid_sprints):
        sprint = valid_sprints[input_sprint - 1]
        return sprint
    else:
        red_print("Opção inválida. Tente novamente!")
        return select_sprint_tui(team_id, closed)


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
