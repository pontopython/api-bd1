from ..utils import generate_id
from .common import create_sprint_dict
from .persistence import read_sprints, write_sprints

SPRINTS = []


def reload_teams():
    global SPRINTS
    SPRINTS = read_sprints()


def update_sprints():
    write_sprints(SPRINTS)


def update_sprint(field, value, new_value, many=False):
    global SPRINTS

    sprints = get_sprints()

    for sprint in sprints:
        if sprint[field] == value:
            sprint = new_value

            if not many:
                break

    update_sprints()


def get_sprints():
    if len(SPRINTS) == 0:
        reload_teams()
    return SPRINTS


def create_sprint(team_id, sprint_name, status='aberta'):
    id = generate_id()
    sprint = create_sprint_dict(id, team_id, sprint_name, status)
    get_sprints().append(sprint)
    update_sprints()
    return sprint


def delete_sprint(sprint):
    get_sprints().remove(sprint)
    update_sprints()


def search_sprint_by(field, value):
    results = []

    for sprint in get_sprints():
        if sprint[field] == value:
            results.append(sprint)

    return results
