import prompt
from random import randint
from brain_games.welcome_user import welcome_user


def random_number():
    random_number = randint(1, 100)
    return random_number


def brain_even():
    name = welcome_user()  # greeting's of user
    rule_of_game = 'Answer \'yes\' if the number is even, \
otherwise answer \'no\'.'
    correct_answer = 'Correct'
    error_for_not_even = f'\'yes\' is wrong answer ;(. \
Correct answer was \'no\'. Let\'s try again, {name}!'
    error_for_even = f'\'no\' is wrong answer ;(. \
Correct answer was \'yes\'. Let\'s try again, {name}!'
    non_existent_answer = f'Wrong answer ;(. \
You should use \'yes\' or \'no\'. \
Let\'s try again, {name}!'
    congritulation = f'Congratulations, {name}!'
    print(rule_of_game)  # start game
    answer_for_win = 3  # count of answer for win
    i = 0
    while i < answer_for_win:
        result = random_number()
        print(f'Question: {result}')
        answer = prompt.string('Your answer: ')
        check_answer = answer.lower()  # if user use incorrect register
        if result % 2 == 0 and check_answer == 'yes' or \
                result % 2 != 0 and check_answer == 'no':
            print(correct_answer)
            i += 1
        elif check_answer != 'yes' and check_answer != 'no':
            print(non_existent_answer)
            return
        elif result % 2 != 0 and check_answer != 'no':
            print(error_for_not_even)
            return
        elif result % 2 == 0 and check_answer != 'yes':
            print(error_for_even)
            return
    print(congritulation)
    return
