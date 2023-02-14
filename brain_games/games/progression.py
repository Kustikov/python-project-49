from random import randint
from random import choice


PROGRESSION_LENGTH = 10
MIN = 1
MAX = 25
RULES = "What number is missing in the progression?"


def get_progression(initial_term, common_difference, PROGRESSION_LENGTH):  # generate progression
    progression = [initial_term]
    i = 0
    while i < PROGRESSION_LENGTH - 1:
        initial_term += common_difference
        progression.append(initial_term)
        i += 1
    return progression


def get_question_and_hide_num(progression):
    result = choice(progression)
    question = ""
    for i in progression:
        if i == result:
            question = f"{question} .."
        else:
            question = f"{question} {i}"
    question = question.strip()
    return question, result


def brain_progression():  # brain-progression
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    progression = get_progression(num1, num2, PROGRESSION_LENGTH)
    question, result = get_question_and_hide_num(progression)
    return question, result
