from ..utils import generate_id
from .common import create_sprint_dict
from .persistence import read_sprints, write_sprints

SPRINTS = []


def reload_sprints():
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
        reload_sprints()
    return SPRINTS

def get_sprint_by_id(id):
    for sprint in get_sprints():
        if sprint["id"] == id:
            return sprint
    return None


def get_all_sprints_from_group(group):
    sprints = []
    for sprint in get_sprints():
        if group["id"] == sprint["group"]["id"]:
            sprints.append(sprint)
    return sprints

def get_opened_sprint_from_group(group):
    opened_sprints = [
        sprint
        for sprint in get_sprints()
        if sprint['status'] == 'aberta' and sprint["group"]["id"] == group["id"]
    ]

    if len(opened_sprints) > 0:
        return opened_sprints[0]

    return None


def create_sprint(group, sprint_name, status='aberta'):
    id = generate_id()
    sprint = create_sprint_dict(id, group, sprint_name, status)
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
