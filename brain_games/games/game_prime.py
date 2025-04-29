import secrets

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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
    number = secrets.choice(NUMBERS)
    question = number
    result = is_prime(number)
    return question, result