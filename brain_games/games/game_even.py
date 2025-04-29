import secrets


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(number):
    return "yes" if number % 2 == 0 else "no"


def brain_even():
    result = ""
    question = ""
    number = secrets.choice(NUMBERS)
    question = number
    result = is_even(number)
    return question, result
