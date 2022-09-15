from colorama import Fore, Style


def green_print(message):
    print(Fore.GREEN + message + Fore.RESET)


def red_print(message):
    print(Fore.RED + message + Fore.RESET)


def blue_bright_print(message):
    print(Fore.BLUE + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)


def cyan_print(message):
    print(Fore.CYAN + message + Fore.RESET)


def magenta_print(message):
    print(Fore.MAGENTA + message + Fore.RESET)


def yellow_print(message):
    print(Fore.YELLOW + message + Fore.RESET)


def bright_print(message):
    print(Style.BRIGHT + message + Style.RESET_ALL)


def bright_print(message):
    print(Style.BRIGHT + message + Style.RESET_ALL)
