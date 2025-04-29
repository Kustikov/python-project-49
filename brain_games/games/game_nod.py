import secrets

RULES = "Find the greatest common divisor of given numbers."
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 -= number_2
        else:
            number_2 -= number_1
    return number_1


def brain_gcd():
    number_1 = secrets.choice(NUMBERS)
    number_2 = secrets.choice(NUMBERS)
    question = f"{number_1} {number_2}"
    result = gcd(number_1, number_2)
    return question, result


