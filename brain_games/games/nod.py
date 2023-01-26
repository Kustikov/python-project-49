import prompt
from brain_games.output_func import (
    welcome_user,
    print_correct,
    print_congrat,
    print_wrong,
    nod,
)
from brain_games.math_func import get_max_devider


def brain_gcd():
    name = welcome_user(nod)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        true_answer = get_max_devider()
        user_answer = prompt.integer(prompt="Your answer: ")
        if user_answer == true_answer:
            print_correct()
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
    return
