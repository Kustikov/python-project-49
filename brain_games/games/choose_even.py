import prompt
from brain_games.welcome_user import welcome_user
from brain_games.output_func import (
    rules_of_game,
    print_correct,
    print_congrat,
    print_wrong,
    even,
)
from brain_games.math_func import random_number, is_even


def brain_even():
    name = welcome_user()  # greeting's of user
    rules_of_game(even)
    #    correct_answer = "Correct!"
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_number()
        print(f"Question: {result}")
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()  # if user use incorrect register
        true_answer = is_even(result)
        if user_answer == true_answer:
            print_correct()
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
    return
