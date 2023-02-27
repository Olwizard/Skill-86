"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def num_very(number):
    x_max = np.random.randint(1, number)
    return x_max
    
def num_litl(number_l):
    x_litl = np.random.randint(number_l, 101)
    return x_litl


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    x_number = np.random.randint(1,101) # загадываемое число
    x_guess = np.random.randint(1,101) # Отгадываем число
    count = 0

    while True:
        count += 1
        """ Угадываем число с помощью бинарного поиска """
        
        if x_guess < x_number:
            num_mean = []
            for x in range(x_guess, 101):
                num_mean.append(x)

            x_guess = int(np.mean(num_mean))
            if x_guess > x_number:
                x_guess = num_very(x_guess)
        
            if x_guess < x_number:
                x_guess = num_litl(x_guess)
                
        if x_guess > x_number:
            num_mean_b = []
            for x in range(1, x_guess):
                num_mean_b.append(x)

            x_guess = int(np.mean(num_mean_b))
            if x_guess > x_number:
                x_guess = num_very(x_guess)
        
            if x_guess < x_number:
                x_guess = num_litl(x_guess)
        
        if x_guess == x_number:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
