import prompt
from brain_games.math_func import is_prime
from brain_games.output_func import (
    welcome_user,
    print_correct,
    print_congrat,
    print_wrong,
    prime,
)


def brain_prime():
    name = welcome_user(prime)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        true_answer = is_prime()
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()  # if user use incorrect register
        if user_answer == true_answer:
            print_correct()
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)
            return
    print_congrat(name)
