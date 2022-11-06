from .persistence import read_session, write_session

_current_session = None


def get_session():
    global _current_session

    if _current_session is None:
        _current_session = read_session()

    if _current_session is None:
        _current_session = {
            "user": None,
            "turma": None,
            "team": None,
        }

    return _current_session


def update_session():
    write_session(_current_session)


def logout():
    global _current_session

    _current_session = {
        "user": None,
        "turma": None,
        "team": None,
    }

    update_session()
