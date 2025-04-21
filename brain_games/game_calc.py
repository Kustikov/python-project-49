from brain_games.cli import brain_calc_cli, welcome_user

BRAIN_CALC_RULE = "What is the result of the expression?"


def calc(random_expression):
    result = int
    expression = random_expression.split()
    number1 = int(expression[1])
    operand = expression[2]
    number2 = int(expression[3])
    match operand:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
    return result


def correct():
    print("Correct!")


def win(name):
    print(f"Congratulations, {name}!")


def wrong(user_answer, correct_answer, name):
    print(
f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
    )


def brain_calc():
    name = welcome_user()
    print(BRAIN_CALC_RULE)
    win_count = 3
    attempt = 0
    while attempt < win_count:
        random_expression, user_answer = brain_calc_cli()
        correct_answer = calc(random_expression)
        user_answer = int(user_answer)
        if correct_answer == user_answer:
            correct()
            attempt += 1
        else:
            wrong(user_answer, correct_answer, name)
            attempt -= attempt
    win(name)
