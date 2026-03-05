
from random import randint, seed as random_seed
import time
import matplotlib.pyplot as plt

def task_func(my_list, size=100, seed=100):
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")
    if not all(isinstance(x, (int, float)) for x in my_list):
        raise ValueError("'my_list' must contain only numeric elements")
    random_seed(seed)
    start_time = time.time()
    random_list = []
    for i in range(size):
        random_list.append(randint(1, 100))
    random_list.extend(my_list)
    end_time = time.time()
    time_taken = end_time - start_time
    histogram = plt.hist(random_list, bins=100)
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    return time_taken, histogram