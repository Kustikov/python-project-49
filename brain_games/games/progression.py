from random import randint
from random import choice


PROGRESSION_LENGTH = 10
MIN = 1
MAX = 25


def print_rules():
    print("What number is missing in the progression?")


def get_progression(initial_term, common_difference):  # generate progression
    progression = [initial_term]
    i = 0
    while i < PROGRESSION_LENGTH - 1:
        initial_term += common_difference
        progression.append(initial_term)
        i += 1
    return progression


def get_question_and_hide_num(progression):
    result = choice(progression)
    new_progression = []
    for i in progression:
        if i == result:
            new_progression.append("..")
        else:
            new_progression.append(i)
    question = " ".join(map(str, new_progression))
    return question, result


def brain_progression():  # brain-progression
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    progression = get_progression(num1, num2)
    question, result = get_question_and_hide_num(progression)
    return question, result
