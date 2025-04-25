from random import randint

RULES = "What number is missing in the progression?"
PASS = ".."
HIDDEN_INDEX = randint(0, 9)
MIN = 1
MAX = 10
progression_length = 10


def brain_progression():
    number = randint(MIN, MAX)
    step = randint(MIN, MAX)
    expression = [number + step * i for i in range(progression_length)]
    result = expression[HIDDEN_INDEX]
    expression[HIDDEN_INDEX] = PASS
    question = (
        f"{' '.join(str(x) for x in expression)}"
    )
    return question, result