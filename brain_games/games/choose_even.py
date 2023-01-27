from random import randint


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
