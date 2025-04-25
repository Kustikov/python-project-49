from random import choice, randint

RULES = "What is the result of the expression?"
MIN = 2
MAX = 10


def calculator():
    number_1 = randint(MIN, MAX)
    number_2 = randint(MIN, MAX)
    operators = ["+", "-", "*"]
    operand = choice(operators)
    question = f"{number_1} {operand} {number_2}"
    result = 0
    match operand:
        case "+":
            result = number_1 + number_2
        case "-":
            result = number_1 - number_2
        case "*":
            result = number_1 * number_2
    return question, result
