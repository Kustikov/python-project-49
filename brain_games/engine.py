import prompt

from brain_games.cli import correct, welcome_user, win, wrong

ROUND_COUNT = 3  # round count's


def play_game(game_logic, rule):
    name = welcome_user()
    print(rule)
    correct_answers = 0
    while correct_answers < ROUND_COUNT:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").lower()
        if user_answer != correct_answer:
            wrong(user_answer, correct_answer, name)
        else:
            correct()
            correct_answers += 1
    win(name)