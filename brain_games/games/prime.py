from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 1
MAX = 30


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int((number) / 2) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    number = randint(MIN, MAX)
    question = number
    if is_prime(number):
        return question, "yes"
    else:
        return question, "no"
