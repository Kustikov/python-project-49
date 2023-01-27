import prompt
from brain_games.print_func import print_correct, print_wrong, print_congrat


name = ""
game = ""


#  rules of games
nod = "Find the greatest common divisor of given numbers."
calc = "What is the result of the expression?"
even = 'Answer "yes" if the number is even, \
otherwise answer "no".'
progr = "What number is missing in the progression?"
is_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def name_of_game(nod):
    print(nod)
    return


def welcome_user(nod):
    print("Welcome to the Brain Games!")
    NAME = prompt.string("May I have your name? ")
    print(f"Hello, {NAME}!")
    name_of_game(nod)
    return NAME


def start_game(name, game):
    name = welcome_user(name)  # greeting's of user
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        question, true_answer = game()
        print(f"Question: {question}")
        true_answer = str(true_answer)
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
