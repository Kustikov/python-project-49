from random import randint
from random import choice


def random_number():
    random_number = randint(1, 20)
    return random_number


def is_even(random_number):
    result = random_number % 2
    if result == 0:
        return "yes"
    else:
        return "no"


def random_expression():  # Generate random expression
    num1 = random_number()
    num2 = random_number()
    index = randint(0, 2)
    operators = ["+", "-", "*"]
    current_operator = operators[index]
    result = f"{num1} {current_operator} {num2}"
    return result


def result_of_expression(str):  # calculate random expression
    num_list = str.split(" ")
    operand = num_list[1]
    num1 = int(num_list[0])
    num2 = int(num_list[2])
    result = 0
    if operand == "*":
        result = num1 * num2
    elif operand == "+":
        result = num1 + num2
    elif operand == "-":
        result = num1 - num2
    return result


def random_of_two_numbers():
    num1 = random_number()
    num2 = random_number()
    result = f"{num1} {num2}"
    return result


def get_max_devider(result):
    list = result.split(" ")
    print(result)
    result = 0
    num1 = int(list[0])
    num2 = int(list[1])
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    result = num1 + num2
    return result


def get_random_progression():
    start = random_number()
    diff = random_number()
    progression = [start]
    i = 0
    list_length = 10
    while i < list_length - 1:
        start += diff
        progression.append(start)
        i += 1
    return progression


#  Вопрос пользователю и получение правильного ответа по игре progression
def get_hidden_num():
    progression = get_random_progression()
    new_progression = []
    hidden_num = choice(progression)
    for i in progression:
        if i == hidden_num:
            new_progression.append("..")
        else:
            new_progression.append(i)
    question = " ".join(map(str, new_progression))
    print(f"Question: {question}")
    return hidden_num


# Вопрос пользователю и получение правильного ответа по игре brain-prime
def is_prime():
    result = random_number()
    print(f"Question: {result}")
    count = 2  # кол-во делителей для простого числа
    if result == 1:  # простое число > 1
        return "no"
    elif result > 1:
        for i in range(2, result):  # итератор в диапазоне от двух до number - 1
            if (result % i) == 0:  # if есть деление без остатка
                count += 1  # плюсуюм делитель
                break  # прерываем цикл чтобы не идти до конца
    if count > 2:  # делителей больше двух, значит не простое число
        return "no"
    else:
        return "yes"
