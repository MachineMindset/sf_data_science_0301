import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100
    
    while True:
        predict = (low + high) // 2
        count += 1
        
        if predict == number:
            break
        
        elif predict > number:
            
               