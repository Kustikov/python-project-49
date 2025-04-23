from brain_games.cli import brain_progression_cli, welcome_user

BRAIN_PROGRESSION_RULE = "What number is missing in the progression?"


def correct():
    print("Correct!")


def win(name):
    print(f"Congratulations, {name}!")


def wrong(user_answer, correct_answer, name):
    print(
f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
    )


def brain_progression():
    name = welcome_user()
    print(BRAIN_PROGRESSION_RULE)
    win_count = 3
    attempt = 0
    while attempt < win_count:
        correct_answer, user_answer = brain_progression_cli()
        if str(correct_answer) == user_answer:
            correct()
            attempt += 1
        else:
            wrong(user_answer, correct_answer, name)
            attempt -= attempt
    win(name)