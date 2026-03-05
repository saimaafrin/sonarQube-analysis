import random
import numpy as np
def task_func(LETTERS):
    result = {}
    for letter in LETTERS:
        # Generate a random number of integers between 1 and 10
        num_integers = random.randint(1, 10)
        # Generate a list of random integers between 0 and 100
        random_integers = [random.randint(0, 100) for _ in range(num_integers)]
        # Calculate the mean of the list of integers
        mean_value = np.mean(random_integers)
        # Store the mean value in the result dictionary with the letter as the key
        result[letter] = mean_value
    return result