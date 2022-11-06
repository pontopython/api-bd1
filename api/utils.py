import shortuuid

from colorama import Fore, Style


def green_print(message, *args, **kwargs):
    print(Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET, *args, **kwargs)


def red_print(message, *args, **kwargs):
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET, *args, **kwargs)


def blue_bright_print(message, *args, **kwargs):
    print(Fore.BLUE + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET, *args, **kwargs)


def green_input(message, *args, **kwargs):
    return input(Fore.GREEN + message + Fore.RESET, *args, **kwargs)


def red_input(message, *args, **kwargs):
    return input(Fore.RED + message + Fore.RESET, *args, **kwargs)


def cyan_print(message, *args, **kwargs):
    print(Fore.CYAN + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET, *args, **kwargs)


def magenta_print(message, *args, **kwargs):
    print(Fore.MAGENTA + message + Fore.RESET, *args, **kwargs)


def yellow_print(message, *args, **kwargs):
    print(Fore.YELLOW + message + Fore.RESET, *args, **kwargs)


def bright_print(message, *args, **kwargs):
    print(Style.BRIGHT + message + Style.RESET_ALL, *args, **kwargs)


def bright_input(message, *args, **kwargs):
    return input(Style.BRIGHT + message + Style.RESET_ALL, *args, **kwargs)
    

def generate_id():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortuuid.set_alphabet(alphabet)
    return shortuuid.random(length=6)


def safe_int_input(prompt="", none_when_invalid=False):
    try:
        return int(input(prompt))
    except ValueError:
        if none_when_invalid:
            return None
        else:
            return 0