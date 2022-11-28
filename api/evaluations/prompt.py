from ..utils import safe_int_input,clear_screen, console
from .common import QUESTIONS, ALTERNATIVES


def prompt_evaluation_form():
    clear_screen()
    grades = {}
    for question, question_text in QUESTIONS.items():
        print(question_text)
        console.print("\n [green]Escolha entre as opções[\green]\n")
        console.print()
        for grade, alternative in enumerate(ALTERNATIVES):
            print(f"[{grade}] - {alternative}")
        answer = safe_int_input("\nOpção: ", none_when_invalid=True)
        while answer is None or answer < 0 or answer >= len(ALTERNATIVES):
            console.print("\n :x: [bold red]Opção inválida! Tente novamente.[/bold red] :x:", justify="center")
            console.print()
            answer = safe_int_input("\nOpção: ", none_when_invalid=True)
        grades[question] = answer
    return grades