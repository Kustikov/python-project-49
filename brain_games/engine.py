import prompt

from brain_games.cli import correct, welcome_user, win, wrong

ROUND_COUNT = 3  

"""
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
"""

"""
def play_game(game_logic, rule):
    name = welcome_user()
    print(rule)

    while True:  # Этот цикл будет повторяться, если игрок ошибается
        i = 0
        while i < ROUND_COUNT:
            question, correct_answer = game_logic()
            correct_answer = str(correct_answer)
            print(f"Question: {question}")
            #user_answer = prompt.string("Your answer: ")
            user_answer = input("Your answer: ")
            user_answer = user_answer.lower()

            if user_answer == correct_answer:
                correct()
                i += 1
            else:
                wrong(user_answer, correct_answer, name)
                print("Let's try again!")
                break  # Выход из внутреннего цикла и перезапуск игры

        # Если игрок прошёл все раунды, показываем выигрыш
        if i == ROUND_COUNT:
            win(name)
            #break  # Завершаем игру
"""


def play_game(game_logic, rule):
    name = welcome_user()
    print(rule)
    i = 0
    while i < ROUND_COUNT:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        correct_answer = str(correct_answer)
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()  # if user use incorrect register
        if user_answer == correct_answer:
            correct()
            i += 1
        elif user_answer != correct_answer:
            wrong(user_answer, correct_answer, name)
            return
    win(name)
    return