import prompt
from brain_games.math_func import is_even
from brain_games.output_func import (
    welcome_user,
    rules_of_game,
    print_correct,
    print_congrat,
    print_wrong,
    even,
)


def brain_even():
    name = welcome_user()  # greeting's of user
    rules_of_game(even)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        true_answer = is_even()
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()  # if user use incorrect register
        if user_answer == true_answer:
            print_correct()
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
    return
