from random import choice, randint

import prompt

FIRST_NUMBER = 2
LAST_NUMBER = 20
EXPRESSION_LIST = ["+", "-", "*"]


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


def brain_calc_cli():
    random_number_1 = randint(FIRST_NUMBER, LAST_NUMBER)
    random_number_2 = randint(FIRST_NUMBER, LAST_NUMBER)
    random_expression = choice(EXPRESSION_LIST)
    question_for_user = (
        f"Question: {random_number_1} {random_expression} {random_number_2}"
    )
    print(question_for_user)
    user_answer = prompt.string("Your answer: ")
    return question_for_user, user_answer
