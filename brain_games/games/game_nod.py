from random import randint

RULES = "Find the greatest common divisor of given numbers."
MIN = 2
MAX = 20


def gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 -= number_2
        else:
            number_2 -= number_1
    return number_1


def brain_gcd():
    number_1 = randint(MIN, MAX)
    number_2 = randint(MIN, MAX)
    question = f"{number_1} {number_2}"
    result = gcd(number_1, number_2)
    return question, result


