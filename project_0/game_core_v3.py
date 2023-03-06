import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадывает число с помощью двоичного поиска
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1       # Нижний порог
    high = 100    # верхний порог
    
    while True:
        predict = (low + high) // 2
        count += 1
        
        if predict == number: 
            break
        
        elif predict > number:
            high = predict - 1 
        
        else:
            low = predict + 1
        
    return count 

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(game_core_v3)