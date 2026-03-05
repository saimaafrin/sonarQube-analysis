
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    """
    Creates a dictionary where keys are letters from the input list LETTERS and values are lists of random integers.
    Then, calculates the population standard deviation for each list of integers and returns a dictionary of these values.
    """
    # Create a dictionary with keys from LETTERS and values as lists of random integers
    letter_dict = {letter: [] for letter in LETTERS}
    for letter in LETTERS:
        for _ in range(random.randint(1, 10)):
            letter_dict[letter].append(random.randint(0, 100))

    # Calculate the population standard deviation for each list of integers
    std_dev_dict = {}
    for letter, values in letter_dict.items():
        std_dev = math.sqrt(sum((x - mean)**2 for x in values) / len(values))
        std_dev_dict[letter] = std_dev

    return std_dev_dict