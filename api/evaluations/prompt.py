from ..utils import safe_int_input
from .common import QUESTIONS, ALTERNATIVES


def prompt_evaluation_form():
    grades = {}
    for question, question_text in QUESTIONS.items():
        print(question_text)
        print("Escolha entre as opções")
        for grade, alternative in enumerate(ALTERNATIVES):
            print(f"[{grade}] - {alternative}")
        answer = safe_int_input("Opção: ", none_when_invalid=True)
        while answer is None or answer < 0 or answer >= len(ALTERNATIVES):
            print("Opção inválida! Tente novamente.")
            answer = safe_int_input("Opção: ", none_when_invalid=True)
        grades[question] = answer
    return grades