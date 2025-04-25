import prompt


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