name = ""
user_answer = ""
true_answer = ""
#  rules of games
nod = "Find the greatest common divisor of given numbers."
calc = "What is the result of the expression?"
even = "Answer 'yes' if the number is even, \
otherwise answer 'no'."
progression = "What number is missing in the progression?"


def rules_of_game(nod):
    print(nod)
    return


def print_wrong(user_answer, true_answer, name):
    print(
        f"Your answer: {user_answer}\n'{user_answer}' \
is wrong answer ;(. Correct answer was '{true_answer}'.\
Let's try again, {name}!"
    )
    return


def print_congrat(name):
    print(f"Congratulations, {name}!")
    return


def print_correct():
    print("Correct")
    return
