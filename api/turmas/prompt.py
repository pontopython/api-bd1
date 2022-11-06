from .validation import validate_turma_name

def prompt_turma_name(prompt="Nome da Turma: "):
    while True:
        name = input(prompt)
        valid, errors = validate_turma_name(name)

        if valid:
            return name

        for error in errors:
            print(error)

        