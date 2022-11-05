from ..users.tui import search_and_select_instructor
from ..turmas.tui import select_turma_from_group_leader, search_and_select_turma
from ..teams.tui import select_team_from_turma
from .repository import get_all_sprints_from_team, create_sprint, update_sprints, search_sprint_by, update_sprint, get_opened_sprint_from_team


def summary_sprint(sprint):
    name = sprint["name"]
    id = sprint["id"]
    status = sprint["status"]
    return f"{name} #{id} ({status})"


def show_sprints_from_team(team):
    sprints = get_all_sprints_from_team(team)
    print("Sprints")
    for sprint in sprints:
        print(f"    - {summary_sprint(sprint)}")


def has_opened_sprint(team):
    opened_sprints = get_opened_sprint_from_team(team)
    return opened_sprints is not None


def open_sprint_for_team(team):
    if has_opened_sprint(team):
        print("Já existe uma sprint aberta.")
        return
    sprint_name = input('Qual o nome da sprint? ')
    create_sprint(team, sprint_name)


def close_sprint_from_team(team):
    if not has_opened_sprint(team):
        print("Não existe sprint aberta.")
        return
    sprint = get_opened_sprint_from_team(team)
    print(summary_sprint(sprint))
    answer = input("Tem certeza que deseja fechar essa sprint (S/N)? ")
    if answer != "S" and answer != "s":
        return
    sprint["status"] = "fechada"
    update_sprints()    

def select_sprint_from_team(team):
    sprints = get_all_sprints_from_team(team)

    if len(sprints) == 0:
        print("Nenhuma sprint encontrada.")
        return None

    for index, sprint in enumerate(sprints):
        print(f"{index+1} - {summary_sprint(sprint)}")

    while True:
        option = int(input("Opção: "))
        if option > 0 and option <= len(sprints):
            return sprints[option - 1]
        print("Opção inválida.")


def reopen_sprint_from_team(team):
    if has_opened_sprint(team):
        print("Já existe uma sprint aberta.")
        return
    sprint = select_sprint_from_team(team)

    if sprint is None:
        return
    
    print(summary_sprint(sprint))
    answer = input("Tem certeza que deseja reabrir essa sprint (S/N)? ")
    if answer != "S" and answer != "s":
        return
    sprint["status"] = "aberta"
    update_sprints()    
    
        
def select_sprint_tui(team_id, closed=False):
    sprints = search_sprint_by("team_id", team_id)
    if not closed:
        valid_sprints = sprints
    if closed:
        valid_sprints = []
        for sprint in sprints:
            if sprint['status'] == 'fechada':
                valid_sprints.append(sprint)
    print("\n          Selecione uma sprint:")
    for index, sprint in enumerate(valid_sprints):
        print(f'     {index + 1}. {sprint["name"]} - {sprint["status"]}')
    
    input_sprint = int(input("\nQual sprint deseja selecionar? "))

    if input_sprint > 0 and input_sprint <= len(valid_sprints):
        sprint = valid_sprints[input_sprint - 1]
        return sprint
        list_users()
    else:
        print("Opção inválida. Tente novamente!")
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

    open_sprint_for_team(team)


def admin_sprints_menu():
    print("Selecione a Turma")
    turma = search_and_select_turma()
    if turma is None:
        return
    
    print("Selecione o Time")
    team = select_team_from_turma(turma)
    if team is None:
        return

    print("Menu Sprints (Administrador)")
    print("1 - Listar")
    print("2 - Abrir Nova")
    print("3 - Fechar")
    print("4 - Reabrir")
    print("5 - Voltar")
    
    while True:
        option = int(input("Opção: "))
        if option >= 1 and option <= 6:
            break
        print("Opção inválida.")
    
    if option == 1:
        show_sprints_from_team(team)
    elif option == 2:
        open_sprint_for_team(team)
    elif option == 3:
        close_sprint_from_team(team)
    elif option == 4:
        reopen_sprint_from_team(team)
    else:
        return