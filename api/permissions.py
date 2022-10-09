COMMON_PERMISSIONS = [
    "see_profile",
    "edit_profile",
    "list_teams",
    "search_teams",
    "evaluate_team_member",
    "see_grades",
]

PERMISSIONS_BY_CATEGORY = {
    "MT": COMMON_PERMISSIONS,
    "PO": COMMON_PERMISSIONS,
    "LT": COMMON_PERMISSIONS,
    "LG": [
        *COMMON_PERMISSIONS,
        "list_users",
        "create_users",
        "search_users",
        "create_teams",
        "edit_teams",
    ],
    "FC": COMMON_PERMISSIONS,
}

def current_user_has_permission(permission):
    from .login import get_logged_user

    user = get_logged_user()

    if user is None:
        return False

    category = user["category"]

    return permission in PERMISSIONS_BY_CATEGORY[category]