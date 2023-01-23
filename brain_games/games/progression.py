import prompt
from brain_games.welcome_user import welcome_user
from brain_games.output_func import (
    rules_of_game,
    print_correct,
    print_congrat,
    print_wrong,
    progression,
)


def brain_progression():
    name = welcome_user()
    rule_of_game = rules_of_game(progression)
    pass
