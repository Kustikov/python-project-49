import secrets

RULES = "What number is missing in the progression?"
PASS = ".."
INDEX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
progression_length = 10


def brain_progression():
    number = secrets.choice(NUMBERS)
    step = secrets.choice(NUMBERS)
    hidden_index = secrets.choice(INDEX)
    expression = [number + step * i for i in range(progression_length)]
    result = expression[hidden_index]
    expression[hidden_index] = PASS
    question = (
        f"{' '.join(str(x) for x in expression)}"
    )
    return question, result