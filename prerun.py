
from api.old_users import create_user_interactively, save_user_to_file
from api.utils import create_empty_data_if_needed
from api.turmas import create_turma_interactively

USER_TYPES = {
    "ADMIN": "Administrador",
    "LIDER": "Líder de Turma",
    "FAKEC": "Fake Client",
    "COMUM": "Comum",
}

#create_empty_data_if_needed()
#create_user_interactively()

#teste
alunos = [
    {'id': '73972da4-b794-49b4-b96b-657171c1569f', 'name': 'Jhonny', 'email': 'jhonny@gmail.com', 'password': 'Abcd123!', 'type': 'LIDER'},
    {'id': 'a0269b72-0eaf-4224-a280-74536d155996', 'name': 'Karolina', 'email': 'karolina@gmail.com', 'password': 'Abcd1111!', 'type': 'LIDER'}
    ]

create_turma_interactively()

