
def create_evaluation_dict(id_sprint, id_team, id_user_log, category_user_log, id_evaluated_user, category_evaluated_user, name_evaluated_user, skill_1, skill_2, skill_3, skill_4, skill_5):
    return {
        "id_sprint": id_sprint,
        "id_team": id_team,
        "id_user_log": id_user_log,
        "category_user_log": category_user_log,
        "id_evaluated_user": id_evaluated_user,
        "category_evaluated_user": category_evaluated_user,
        "name_evaluated_user": name_evaluated_user,
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3,
        "skill_4": skill_4,
        "skill_5": skill_5,
    }