from random import randint


rules = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def brain_even():
    result = ""
    question = ""
    number = randint(1, 100)
    question = number
    result = number % 2
    if result == 0:
        result = "yes"
    else:
        result = "no"
    return question, result
