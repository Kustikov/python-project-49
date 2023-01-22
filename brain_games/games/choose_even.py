import prompt
from brain_games.welcome_user import welcome_user
from brain_games.math_func import random_number


def brain_even():
    name = welcome_user()  # greeting's of user
    rule_of_game = "Answer 'yes' if the number is even, \
otherwise answer 'no'."
    correct_answer = "Correct!"
    error_for_not_even = f"'yes' is wrong answer ;(. \
Correct answer was 'no'. Let's try again, {name}!"
    error_for_even = f"'no' is wrong answer ;(. \
Correct answer was 'yes'. Let's try again, {name}!"
    non_existent_answer = f"Wrong answer ;(. \
You should use 'yes' or 'no'. \
Let's try again, {name}!"
    congritulation = f"Congratulations, {name}!"
    print(rule_of_game)  # start game
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_number()
        even = result % 2
        print(f"Question: {result}")
        user_answer = prompt.string("Your answer: ")
        true_answer = user_answer.lower()  # if user use incorrect register
        if even == 0 and true_answer == "yes" or even != 0 and true_answer == "no":
            print(correct_answer)
            i += 1
        elif true_answer != "yes" and true_answer != "no":
            print(non_existent_answer)
            return
        elif even != 0 and true_answer != "no":
            print(error_for_not_even)
            return
        elif even == 0 and true_answer != "yes":
            print(error_for_even)
            return
    print(congritulation)
    return
