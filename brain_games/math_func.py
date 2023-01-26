from random import randint
from random import choice


def random_number():
    random_number = randint(1, 30)
    return random_number


def is_even():  # brain-even
    result = ""
    number = random_number()
    print(f"Question: {number}")
    result = number % 2
    if result == 0:
        return "yes"
    else:
        return "no"


def random_expression():  # generate expression for calc
    num1 = random_number()
    num2 = random_number()
    index = randint(0, 2)
    operators = ["+", "-", "*"]
    current_operator = operators[index]
    result = f"{num1} {current_operator} {num2}"
    return result


def result_of_expression():  # brain-calc
    expression = random_expression()
    print(f"Question: {expression}")
    num_list = expression.split(" ")  # str.answer from user to int
    operand = num_list[1]
    num1 = int(num_list[0])
    num2 = int(num_list[2])
    result = 0
    if operand == "*":
        result = num1 * num2
    elif operand == "+":
        result = num1 + num2
    elif operand == "-":
        result = num1 - num2
    return result


def random_of_two_numbers():  # num's for brain-nod
    num1 = random_number()
    num2 = random_number()
    result = f"{num1} {num2}"
    return result


def get_max_devider():  # brain-nod
    numbers = random_of_two_numbers()
    print(f"Question: {numbers}")
    list = numbers.split(" ")
    result = 0
    num1 = int(list[0])
    num2 = int(list[1])
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    result = num1 + num2
    return result


def get_random_progression():  # generate progression
    start = random_number()
    diff = random_number()
    progression = [start]
    i = 0
    list_length = 10
    while i < list_length - 1:
        start += diff
        progression.append(start)
        i += 1
    return progression


def get_hidden_num():  # brain-progression
    progression = get_random_progression()
    new_progression = []
    hidden_num = choice(progression)
    for i in progression:
        if i == hidden_num:
            new_progression.append("..")
        else:
            new_progression.append(i)
    question = " ".join(map(str, new_progression))
    print(f"Question: {question}")
    return hidden_num


def is_prime():  # brain-prime
    number = random_number()
    if number < 2:
        return "no"
    print(f"Question: {number}")
    for i in range(2, int((number) / 2) + 1):
        if number % i == 0:
            return "no"
    return "yes"
