from random import randint

RULES = 'Answer "yes" if the number is even, \
otherwise answer "no".'
MIN = 1
MAX = 100


def is_even(number):
    return number % 2 == 0


def brain_even():
    result = ""
    question = ""
    number = randint(MIN, MAX)
    question = number
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    return question, result
