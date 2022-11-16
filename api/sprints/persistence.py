import os
import json

from api.turmas.repository import get_turma_by_id
from .common import create_sprint_dict

SPRINTS_FILE = "data/sprints.json"

os.makedirs("data", exist_ok=True)
if not os.path.exists(SPRINTS_FILE):
    file = open(SPRINTS_FILE, "a")
    file.write("[]")
    file.close()

# dict layout
# {
#   "id": id da sprint
#   "group": id da turma dona dessas sprints
#   "name": nome da sprint
#   "status": aberta/fechada
# }

def write_sprints(sprints):
    file = open(SPRINTS_FILE, "w")
    file.write(json.dumps([
        {
            "id": sprint["id"],
            "group_id": sprint["group"]["id"],
            "name": sprint["name"],
            "status": sprint["status"]
        }
        for sprint in sprints
    ]))
    file.close()

def read_sprints():
    file = open(SPRINTS_FILE, "r")
    content = file.read()
    sprints = json.loads(content)
    file.close()
    sprints = [
        create_sprint_dict(
            sprint["id"],
            get_turma_by_id(sprint["group_id"]),
            sprint["name"],
            sprint["status"]
        )
        for sprint in sprints
    ]
    return sprints
