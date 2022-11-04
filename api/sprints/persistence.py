import os
import json

SPRINTS_FILE = "data/sprints.json"

os.makedirs("data", exist_ok=True)
if not os.path.exists(SPRINTS_FILE):
    file = open(SPRINTS_FILE, "a")
    file.write("[]")
    file.close()

# dict layout
# {
#   "id": id da sprint
#   "team_id": id do time dono dessas sprints
#   "status": aberta/fechada
# }

def write_sprints(sprints):
    file = open(SPRINTS_FILE, "w")
    file.write(json.dumps(sprints))
    file.close()

def read_sprints():
    file = open(SPRINTS_FILE, "r")
    content = file.read()
    sprints = json.loads(content)
    file.close()
    return sprints
