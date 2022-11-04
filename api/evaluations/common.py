QUESTIONS = {
    "EQUIPE": "Trabalho em equipe, cooperação e descentralização de conhecimento",
    "INICIA": "Iniciativa e proatividade",
    "AUTODI": "Autodidaxia e agregação de conhecimento ao grupo",
    "ENTREG": "Entrega de resultados e participação efetiva no projeto",
    "COMPET": "Competência técnica",
}

ALTERNATIVES = [
    "Muito Ruim",
    "Ruim",
    "Regular",
    "Bom",
    "Muito Bom",
]

def evaluation_dict(id, sprint, evaluator, evaluated, grades):
    return {
        "id": id,
        "sprint": sprint,
        "evaluator": evaluator,
        "evaluated": evaluated,
        "grades": grades
    }
