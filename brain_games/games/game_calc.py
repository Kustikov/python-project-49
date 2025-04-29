from random import choice
import secrets


RULES = "What is the result of the expression?"
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def calculator():
    number_1 = secrets.choice(NUMBERS)
    number_2 = secrets.choice(NUMBERS)
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
