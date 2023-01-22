import prompt
from brain_games.welcome_user import welcome_user
from brain_games.output_func import nod, rules_of_game
from brain_games.math_func import random_of_two_numbers, get_max_devider


def brain_gcd():
    name = welcome_user()
    rule_of_game = rules_of_game(nod)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_of_two_numbers()
        print(f"Question: {result}")
        user_answer = prompt.integer(prompt="Your answer: ")
        true_answer = get_max_devider(result)
        print(true_answer)
    return