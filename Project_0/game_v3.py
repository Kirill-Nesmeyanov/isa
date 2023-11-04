"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """ Угадываем число от 0 до 100. 
    При работе функции на каждой итерации цикла учитывается, 
    больше или меньше наше число, чем то, которое было "загадано" компьютером.
    Функция использует наименьшее количетво попыток.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0 
    # первое число задается рандомно
    predict = np.random.randint(1, 101) 
    # Границы поиска
    min_number, max_number = 0, 100 

    # в цикле перебираем числа с учетом того, 
    # больше или меньше загаданного наше число
    while number != predict:
        count += 1

        if number > predict:
            min_number = predict + 1
            predict = (max_number+min_number) // 2

        elif number < predict:
            max_number = predict - 1
            predict = (max_number+min_number) // 2

    # Ваш код заканчивается здесь

    return count
   

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(game_core_v3)

