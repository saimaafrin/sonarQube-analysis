
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    # Create a dictionary with keys as letters and values as lists of random integers
    letter_dict = {letter: [] for letter in LETTERS}
    for letter in LETTERS:
        for i in range(1, 11):
            letter_dict[letter].append(random.randint(0, 100))

    # Calculate the population standard deviation for each list of integers
    std_dev_dict = {}
    for letter, values in letter_dict.items():
        std_dev = math.sqrt(sum((x - mean)**2 for x in values) / len(values))
        std_dev_dict[letter] = std_dev

    return std_dev_dict