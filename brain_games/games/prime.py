from random import randint


def brain_prime():  # brain-prime
    number = randint(1, 40)
    question = number
    if number < 2:
        return "no"
    for i in range(2, int((number) / 2) + 1):
        if number % i == 0:
            return question, "no"
    return question, "yes"
