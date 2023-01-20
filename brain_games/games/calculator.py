import prompt
from brain_games.welcome_user import welcome_user
from brain_games.math_func import random_expression, result_of_expression


def brain_calculator():
    name = welcome_user()  # greeting's of user
    rule_of_game = "What is the result of the expression?"
    correct_answer = "Correct!"
    congratulation = f"Congratulations, {name}!"
    #   non_existent_answer = f"Wrong answer ;(. \  #
    # You should use Numbers, {name}!"  #
    print(rule_of_game)  # start game
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_expression()
        print(f"Question: {result}")
        user_answer = prompt.integer(prompt="Your answer:")
        true_answer = result_of_expression(result)
        if user_answer == true_answer:
            print(correct_answer)
            i += 1
        elif user_answer != true_answer:
            print(
                f"Your answer: {user_answer}\n'{user_answer}' \
is wrong answer ;(. Correct answer was '{true_answer}'.\
Let's try again, {name}!"
            )
            return
    print(congratulation)
    return
