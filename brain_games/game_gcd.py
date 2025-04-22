from brain_games.cli import brain_gcd_cli, welcome_user

BRAIN_GCD_RULE = "Find the greatest common divisor of given numbers."


def gcd(random_expression):
    expression = random_expression.split()
    number1 = int(expression[1])
    number2 = int(expression[2])
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1
    print(number1)
    return number1


def correct():
    print("Correct!")


def win(name):
    print(f"Congratulations, {name}!")


def wrong(user_answer, correct_answer, name):
    print(
f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
    )


def brain_gcd():
    name = welcome_user()
    print(BRAIN_GCD_RULE)
    win_count = 3
    attempt = 0
    while attempt < win_count:
        random_expression, user_answer = brain_gcd_cli()
        correct_answer = gcd(random_expression)
        if correct_answer == int(user_answer):
            correct()
            attempt += 1
        else:
            wrong(user_answer, correct_answer, name)
            attempt -= attempt
    win(name)

    
    

