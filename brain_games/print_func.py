NAME = ""
user_answer = ""
true_answer = ""


def print_wrong(user_answer, true_answer, NAME):
    print(
        f"Your answer: {user_answer}\n'{user_answer}' \
is wrong answer ;(. Correct answer was '{true_answer}'.\
Let's try again, {NAME}!"
    )
    return


def print_correct():
    print("Correct")
    return


def print_congrat(NAME):
    print(f"Congratulations, {NAME}!")
    return
