from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int((number) / 2) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    number = randint(1, 30)
    question = number
    if is_prime(number):
        return question, "yes"
    else:
        return question, "no"
