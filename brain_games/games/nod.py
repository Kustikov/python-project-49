from random import randint


rules = "Find the greatest common divisor of given numbers."


def random_of_two_numbers():  # num's for brain-nod
    num1 = randint(1, 50)
    num2 = randint(1, 20)
    result = f"{num1} {num2}"
    return result


def brain_gcd():  # brain-nod
    question = random_of_two_numbers()
    list = question.split(" ")
    result = 0
    num1 = int(list[0])
    num2 = int(list[1])
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    result = num1 + num2
    return question, result
