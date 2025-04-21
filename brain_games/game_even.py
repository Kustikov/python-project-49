from brain_games.cli import brain_even_cli, welcome_user

BRAIN_EVEN_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return "yes" if number % 2 == 0 else "no"


def correct():
    print("Correct!")


def win(name):
    print(f"Congratulations, {name}!")


def wrong(user_answer, correct_answer, name):
    print(
f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
    )


def brain_even():
    name = welcome_user()
    print(BRAIN_EVEN_RULE)
    win_count = 3
    attempt = 0
    while attempt < win_count:
        random_number, user_answer = brain_even_cli()
        correct_answer = is_even(random_number)
        if correct_answer == user_answer:
            correct()
            attempt += 1
        else:
            wrong(user_answer, correct_answer, name)
            attempt -= attempt
    win(name)
