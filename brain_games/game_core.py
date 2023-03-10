import prompt


ANSWER_FOR_WIN = 3  # count of answer for win


def play_game(rules, get_game_round):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)
    i = 0
    while i < ANSWER_FOR_WIN:
        question, true_answer = get_game_round()
        print(f"Question: {question}")
        true_answer = str(true_answer)
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()  # if user use incorrect register
        if user_answer == true_answer:
            print("Correct")
            i += 1
        elif user_answer != true_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct \
answer was '{true_answer}'.\n\
Let's try again, {name}!"
            )
            return
    print(f"Congratulations, {name}!")
    return
