def create_turma_dict(id, name, group_leader, fake_client, students):
    return {
        "id": id,
        "name": name,
        "group_leader": group_leader,
        "fake_client": fake_client,
        "students": students,
    }