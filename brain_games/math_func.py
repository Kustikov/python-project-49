from random import randint


def random_number():
    random_number = randint(1, 100)
    return random_number


def random_expression():  # Generate random expression
    num1 = random_number()
    num2 = random_number()
    index = randint(0, 2)
    operators = ["+", "-", "*"]
    current_operator = operators[index]
    result = f"{num1} {current_operator} {num2}"
    return result


def result_of_expression(str):  # calculate random expression
    num_list = str.split(" ")
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
