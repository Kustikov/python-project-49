import prompt
from brain_games.welcome_user import welcome_user
from brain_games.output_func import rules_of_game, print_correct, print_congrat, print_wrong, calc
from brain_games.math_func import random_expression, result_of_expression


def brain_calculator():
    name = welcome_user()  # greeting's of user
    rule_of_game = rules_of_game(calc)
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_expression()
        print(f"Question: {result}")
        user_answer = prompt.integer(prompt="Your answer: ")
        true_answer = result_of_expression(result)
        if user_answer == true_answer:
            print_correct
            i += 1
        elif user_answer != true_answer:
            print_wrong(user_answer, true_answer, name)              
            return
    print_congrat(name)
    return
