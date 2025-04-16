from brain_games.brain_even_cli import brain_even_cli
from brain_games.greet import welcome_user

BRAIN_EVEN_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def brain_even():
    name = welcome_user()
    print(BRAIN_EVEN_RULE)
    while True:
        point_for_win = 3
        win_count = 0
        while win_count < point_for_win:
            number, answer = brain_even_cli()
            correct = "yes" if is_even(number) else "no"
            if is_even(number) and answer == "yes":
                win_count += 1
                print("Correct!")
            elif not is_even(number) and answer == "no":
                win_count += 1
                print("Correct!")
            else:
                print(
                    f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'. \nLet's try again, {name}!"
                )
                break
        else:
            print(f"Congratulations, {name}!")
            return
