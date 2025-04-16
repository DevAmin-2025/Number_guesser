'''
Create ways to have colorful prints.
'''
from termcolor import colored


def print_excellent(text: str):
    print(colored(text, 'green', attrs=['reverse']))


def print_medium(text: str):
    print(colored(text, 'yellow', attrs=['reverse']))


def print_week(text: str):
    print(colored(text, 'red', attrs=['reverse']))


def print_information(text: str):
    print(colored(text, 'white', attrs=['reverse']))
