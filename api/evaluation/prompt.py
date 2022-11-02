from .persistence import evaluation_dict_to_line

def prompt_evaluation_form(user=None, team=None, show=True):
    questions = {
        "1": {
            "question": "Trabalho em equipe, cooperação e descentralização de conhecimento:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "2": {
            "question": "Iniciativa e proatividade:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "3": {
            "question": "Autodidaxia e agregação de conhecimento ao grupo:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "4": {
            "question": "Entrega de resultados e participação efetiva no projeto:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
        "5": {
            "question": "Competência técnica:",
            "answers": {
                "0": "Muito Ruim",
                "1": "Ruim",
                "2": "Regular",
                "3": "Bom",
                "4": "Muito Bom",
            },
        },
    }
    if show:
        print(f"\nAvaliação de {user['name']}\n")
        lista = []
        for qk, qv in questions.items():
            print(f'\n{qk}. {qv["question"]}')

            print("\nEscolha entre as opções indicadas:\n")
            for ak, av in qv["answers"].items():
                print(f"[{ak}]: {av}")

            answers_user = int(input("\nOpção: "))
            print()
            while answers_user < 0 or answers_user > 4:
                print("\nOpção inválida! Tente novamente.\n")
                answers_user = int(input("\nOpção: "))
            lista.append(answers_user)

        return evaluation_dict_to_line(user, lista, team)

    else:
        return questions