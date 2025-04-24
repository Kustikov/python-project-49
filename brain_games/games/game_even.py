from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 2
MAX = 20


def is_even(number):
    return "yes" if number % 2 == 0 else "no"


def brain_even():
    result = ""
    question = ""
    number = randint(MIN, MAX)
    question = number
    result = is_even(number)
    return question, result
