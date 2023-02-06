from random import randint
from random import choice


rules = "What number is missing in the progression?"


def get_progression(initial_term, common_difference):  # generate progression
    progression = [initial_term]
    i = 0
    list_length = 10
    while i < list_length - 1:
        initial_term += common_difference
        progression.append(initial_term)
        i += 1
    return progression


def get_question(progression):
    question = " ".join(map(str, progression))
    return question


def brain_progression():  # brain-progression
    initial_term = randint(1, 10)
    common_difference = randint(1, 30)
    progression = get_progression(initial_term, common_difference)
    new_progression = []
    result = choice(progression)
    for i in progression:
        if i == result:
            new_progression.append("..")
        else:
            new_progression.append(i)
    question = get_question(new_progression)
    return question, result
