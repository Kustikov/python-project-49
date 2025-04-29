import secrets
from random import randint

RULES = "What number is missing in the progression?"
PASS = ".."
HIDDEN_INDEX = randint(0, 9)
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
progression_length = 10


def brain_progression():
    number = secrets.choice(NUMBERS)
    step = secrets.choice(NUMBERS)
    expression = [number + step * i for i in range(progression_length)]
    result = expression[HIDDEN_INDEX]
    expression[HIDDEN_INDEX] = PASS
    question = (
        f"{' '.join(str(x) for x in expression)}"
    )
    return question, result