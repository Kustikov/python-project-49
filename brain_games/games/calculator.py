from random import randint


rules = "What is the result of the expression?"


def random_expression():  # generate expression for calc
    num1 = randint(1, 30)
    num2 = randint(1, 10)
    index = randint(0, 2)
    operators = ["+", "-", "*"]
    current_operator = operators[index]
    result = f"{num1} {current_operator} {num2}"
    return result


def calculator():  # brain-calc
    question = random_expression()
    num_list = question.split(" ")  # str.answer from user to int
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
    return question, result
