from random import randint

rules = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def brain_even():
    result = ""
    question = ""
    number = randint(1, 100)
    question = number
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    return question, result
