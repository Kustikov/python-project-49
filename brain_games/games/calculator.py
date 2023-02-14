from random import randint
from random import choice


MIN = 1
MAX = 15
RULES = "What is the result of the expression?"


def calculator():  # brain-calc
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    operators = ["+", "-", "*"]
    operand = choice(operators)
    question = f"{num1} {operand} {num2}"
    result = 0
    if operand == "*":
        result = num1 * num2
    elif operand == "+":
        result = num1 + num2
    elif operand == "-":
        result = num1 - num2
    return question, result
