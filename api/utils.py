import os

from colorama import Fore, Style


def green_print(message):
    print(Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)


def red_print(message):
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)


def blue_bright_print(message):
    print(Fore.BLUE + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)


def green_input(message):
    input(Fore.GREEN + message + Fore.RESET)


def red_input(message):
    input(Fore.RED + message + Fore.RESET)


def cyan_print(message):
    print(Fore.CYAN + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)


def magenta_print(message):
    print(Fore.MAGENTA + message + Fore.RESET)


def yellow_print(message):
    print(Fore.YELLOW + message + Fore.RESET)


def bright_print(message):
    print(Style.BRIGHT + message + Style.RESET_ALL)


def bright_input(message):
    input(Style.BRIGHT + message + Style.RESET_ALL)


def create_empty_data_if_needed():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/user.txt"):
        open("data/users.txt", "a").close()  # Create empty file
    if not os.path.exists("data/login.txt"):
        open("data/login.txt", "a").close()  # Create empty file
