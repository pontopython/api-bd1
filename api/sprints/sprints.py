from api.utils import blue_bright_print, bright_input, magenta_print, red_print
from ..users.tui import search_and_select_instructor
from ..turmas.tui import select_turma_from_group_leader
from ..teams.tui import select_team_from_turma
from .repository import create_sprint, search_sprint_by, update_sprint, get_opened_sprint_from_team


def has_opened_sprint(team):
    opened_sprints = get_opened_sprint_from_team(team)
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
    blue_bright_print("\n          Selecione uma sprint:")
    for index, sprint in enumerate(valid_sprints):
        print(f'     {index + 1}. {sprint["name"]} - {sprint["status"]}')
    
    input_sprint = int(bright_input("\nQual sprint deseja selecionar? "))

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
    print("Selecione o líder de grupo: ")
    instructor = search_and_select_instructor()

    turma = select_turma_from_group_leader(instructor)
    if turma is None:
        return
    
    team = select_team_from_turma(turma)
    if team is None:
        return

    if has_opened_sprint(team):
        magenta_print("\nJá existe uma sprint aberta.")
        return

    sprint_name = bright_input('Qual o nome da sprint? ')
    sprint = create_sprint(team['id'], sprint_name)
    return sprint


if __name__ == '__main__':
    create_sprint_tui()
    close_sprint_tui()
