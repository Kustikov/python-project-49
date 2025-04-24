from random import choice, randint

import prompt

EXPRESSION_LIST = ["+", "-", "*"]
HIDDEN_SYM_FOR_PROGRESSION = ".."
HIDDEN_INDEX = randint(0, 9)


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def correct():
    print("Correct!")


def win(name):
    print(f"Congratulations, {name}!")


def wrong(user_answer, correct_answer, name):
    print(
f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
    )


def brain_calc_cli():
    random_number_1 = randint(FIRST_NUMBER, LAST_NUMBER)
    random_number_2 = randint(FIRST_NUMBER, LAST_NUMBER)
    random_expression = choice(EXPRESSION_LIST)
    question_for_user = (
        f"Question: {random_number_1} {random_expression} {random_number_2}"
    )
    print(question_for_user)
    user_answer = prompt.string("Your answer: ")
    return question_for_user, user_answer


def brain_gcd_cli():
    random_number_1 = randint(FIRST_NUMBER, LAST_NUMBER)
    random_number_2 = randint(FIRST_NUMBER, LAST_NUMBER)
    question_for_user = f"Question: {random_number_1} {random_number_2}"
    print(question_for_user)
    user_answer = prompt.string("Your answer: ")
    return question_for_user, user_answer


def brain_progression_cli():
    random_number = randint(FIRST_NUMBER, LAST_NUMBER)
    step = randint(FIRST_NUMBER, LAST_NUMBER)
    random_expression = [random_number + step * i for i in range(10)]
    correct_answer = step
    random_expression[HIDDEN_INDEX] = HIDDEN_SYM_FOR_PROGRESSION
    question_for_user = (
        f"Question: {' '.join(str(x) for x in random_expression)}"
    )
    print(question_for_user)
    user_answer = prompt.string("Your answer: ")
    return correct_answer, user_answer


