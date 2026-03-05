
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    # Create a dictionary where keys are letters from the input list and values are lists of random integers
    random_ints = {}
    for letter in LETTERS:
        random_ints[letter] = [random.randint(0, 100) for _ in range(1, 11)]

    # Calculate the population standard deviation for each list of random integers
    std_devs = {}
    for letter, ints in random_ints.items():
        std_devs[letter] = math.sqrt(sum(map(lambda x: x - mean(ints) ** 2, ints)) / (len(ints) - 1))

    return std_devs