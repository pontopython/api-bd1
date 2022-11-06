MEMBERSHIP_CATEGORIES = {
    "LIDER": "Líder Técnico",
    "PRODU": "Product Owner",
    "COMUM": "Membro",
}


def create_team_dict(id, name, turma, members):
    return {"id": id, "name": name, "turma": turma, "members": members}
