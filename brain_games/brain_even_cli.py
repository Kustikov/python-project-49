from random import randint

import prompt

from brain_games.storage import FIRST_NUMBER, LAST_NUMBER


def brain_even_cli():
    number = randint(FIRST_NUMBER, LAST_NUMBER)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    answer = answer.lower()
    return [number, answer]
