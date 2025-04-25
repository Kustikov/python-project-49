import prompt

from brain_games.cli import correct, welcome_user, win, wrong

ROUND_COUNT = 3  # round count's


def play_game(game_logic, rule):
    name = welcome_user()
    print(rule)
    i = 0
    while i < ROUND_COUNT:
        question, correct_answer = game_logic()
        correct_answer = str(correct_answer)
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()
        if user_answer == correct_answer:
            correct()
            i += 1
        elif user_answer != correct_answer:
            wrong(user_answer, correct_answer, name)
    win(name)