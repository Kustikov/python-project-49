from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 2
MAX = 20

def is_prime(number):
    if number <= 1:
        return "no"
    devider = range(2, number)
    for i in devider:
        if number % i == 0:
            return "no"
    return "yes"

        
def brain_prime():
    result = ""
    question = ""
    number = randint(MIN, MAX)
    question = number
    result = is_prime(number)
    return question, result