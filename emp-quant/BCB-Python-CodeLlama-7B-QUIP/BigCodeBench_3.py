
import random
import numpy as np

def task_func(LETTERS):
    # Create a dictionary where keys are specified letters and values are lists of random integers
    random_dict = {}
    for letter in LETERNS:
        random_dict[letter] = [random.randint(0, 100) for _ in range(random.randint(1, 10))]

    # Calculate the mean of these integers for each key and return a dictionary of these means
    means = {}
    for letter, values in random_dict.items():
        means[letter] = np.mean(values)

    return means