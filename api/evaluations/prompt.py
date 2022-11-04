from .common import QUESTIONS, ALTERNATIVES

def prompt_evaluation_form():
    grades = {}
    for question, question_text in QUESTIONS.items():
        print(question_text)
        print("Escolha entre as opções")
        for grade, alternative in enumerate(ALTERNATIVES):
            print(f"[{grade}] - {alternative}")
        answer = int(input("\nOpção: "))
        while answer < 0 or answer >= len(ALTERNATIVES):
            print("Opção inválida! Tente novamente.")
            answer = int(input("Opção: "))
        grades[question] = answer
    return grades