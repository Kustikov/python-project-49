from random import randint


rules = "Find the greatest common divisor of given numbers."


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    result = num1 + num2
    return result


def brain_gcd():  # brain-nod
    result = 0
    num1 = randint(1, 50)
    num2 = randint(1, 20)
    question = f"{num1} {num2}"
    result = gcd(num1, num2)
    return question, result
