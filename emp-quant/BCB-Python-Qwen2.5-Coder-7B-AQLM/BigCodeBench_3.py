
import random
import numpy as np

def task_func(LETTERS):
    result = {}
    for letter in LETTERS:
        num_list = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        mean_value = np.mean(num_list)
        result[letter] = mean_value
    return result