#import evaluation form
#make evaluation form return a dict
from utils import green_print

EVALUATIONS_FILE = "../data/evaluations.txt"

#PARA TESTES APENAS
def create_evaluation_dict(evaluation_id, sprint, evaluator, evaluated, soft_skill1, soft_skill2, soft_skill3, soft_skill4, soft_skill5,):
    return {
        "evaluation_id": evaluation_id,
        "sprint": sprint,
        "evaluator": evaluator,
        "evaluated": evaluated,
        "soft_skill1": soft_skill1,
        "soft_skill2": soft_skill2,
        "soft_skill3": soft_skill3,
        "soft_skill4": soft_skill4,
        "soft_skill5": soft_skill5,
    }
#PARA TESTES APENAS


def evaluation_dict_to_line(evaluation):
    evaluation_id = evaluation["evaluation_id"]
    sprint = evaluation["sprint"]
    evaluator = evaluation["evaluator"]
    evaluated = evaluation["evaluated"]
    soft_skill1 = evaluation["soft_skill1"]
    soft_skill2 = evaluation["soft_skill2"]
    soft_skill3 = evaluation["soft_skill3"]
    soft_skill4 = evaluation["soft_skill4"]
    soft_skill5 = evaluation["soft_skill5"]

    return f"{evaluation_id};{sprint};{evaluator};{evaluated};{soft_skill1};{soft_skill2};{soft_skill3};{soft_skill4};{soft_skill5}"

def save_evaluation_to_file(evaluation):
    file = open(EVALUATIONS_FILE, "a")
    line = evaluation_dict_to_line(evaluation)
    file.write(line)
    file.write("\n")
    file.close()
    green_print("\n             Avaliação salva com sucesso!")

#TESTE
save_evaluation_to_file(create_evaluation_dict(976435, 1, 'Alec', 'Larissa', 2, 3, 3, 2, 1)) 