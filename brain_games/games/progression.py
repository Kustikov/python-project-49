import prompt
from brain_games.welcome_user import welcome_user
from brain_games.math_func import get_hidden_num
from brain_games.output_func import (
    rules_of_game,
    print_correct,
    print_congrat,
    print_wrong,
    progression,
)


def brain_progression():
    name = welcome_user()
    rules_of_game(progression)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        true_answer = get_hidden_num()
        user_answer = prompt.integer(prompt="Your answer: ")
        if user_answer == true_answer:
            print_correct()
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
    return
