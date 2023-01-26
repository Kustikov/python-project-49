import prompt


NAME = ""
USER_ANSWER = ""
TRUE_ANSWER = ""
#  rules of games
nod = "Find the greatest common divisor of given numbers."
calc = "What is the result of the expression?"
even = 'Answer "yes" if the number is even, \
otherwise answer "no".'
progression = "What number is missing in the progression?"
prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def welcome_user():
    print("Welcome to the Brain Games!")
    NAME = prompt.string("May I have your name? ")
    print(f"Hello, {NAME}!")
    return NAME


def rules_of_game(nod):
    print(nod)
    return


def print_wrong(USER_ANSWER, TRUE_ANSWER, NAME):
    print(
        f"Your answer: {USER_ANSWER}\n'{USER_ANSWER}' \
is wrong answer ;(. Correct answer was '{TRUE_ANSWER}'.\
Let's try again, {NAME}!"
    )
    return


def print_congrat(NAME):
    print(f"Congratulations, {NAME}!")
    return


def print_correct():
    print("Correct")
    return
