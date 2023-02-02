from random import randint
from random import choice


rules = "What number is missing in the progression?"


def get_random_progression():  # generate progression
    start = randint(1, 10)
    diff = randint(1, 30)
    progression = [start]
    i = 0
    list_length = 10
    while i < list_length - 1:
        start += diff
        progression.append(start)
        i += 1
    return progression


def progression():  # brain-progression
    progression = get_random_progression()
    new_progression = []
    result = choice(progression)
    for i in progression:
        if i == result:
            new_progression.append("..")
        else:
            new_progression.append(i)
    question = " ".join(map(str, new_progression))
    return question, result
