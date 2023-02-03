from random import randint


rules = "What is the result of the expression?"


def calculator():  # brain-calc
    num1 = randint(1, 30)
    num2 = randint(1, 10)
    index = randint(0, 2)
    operators = ["+", "-", "*"]
    operand = operators[index]
    question = f"{num1} {operand} {num2}"
    result = 0
    if operand == "*":
        result = num1 * num2
    elif operand == "+":
        result = num1 + num2
    elif operand == "-":
        result = num1 - num2
    return question, result
