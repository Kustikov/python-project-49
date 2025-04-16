from random import randint

import prompt

FIRST_NUMBER = 2
LAST_NUMBER = 100


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def brain_even_cli():
    random_number = randint(FIRST_NUMBER, LAST_NUMBER)
    print(f"Question: {random_number}")
    user_answer = prompt.string("Your answer: ")
    return random_number, user_answer
