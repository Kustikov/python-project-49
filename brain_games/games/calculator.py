import prompt
from brain_games.output_func import (
    welcome_user,
    print_correct,
    print_congrat,
    print_wrong,
    calc,
)
from brain_games.math_func import result_of_expression


def brain_calculator():
    name = welcome_user(calc)  # greeting's of user
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        true_answer = result_of_expression()
        user_answer = prompt.integer(prompt="Your answer: ")
        if user_answer == true_answer:
            print_correct
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
    return
