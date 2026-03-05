import random
import math
def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    """
    Create a dictionary where keys are letters from a predefined list LETTERS and values are lists of random integers.
    Then, calculates the population standard deviation for each list of integers and returns a dictionary of these values.
    The random integers for each key are generated within the range 0 to 100, and each list contains between 1 to 10 integers.
    The function should output with:
        dict: A dictionary where each key corresponds to a letter from the input list and each value is the
        population standard deviation of a list of random integers associated with that key.
    """
    # Create a dictionary with keys as letters from the input list and values as lists of random integers
    letter_dict = {letter: [] for letter in LETTERS}
    for letter in LETTERS:
        for i in range(1, 11):
            letter_dict[letter].append(random.randint(0, 100))

    # Calculate the population standard deviation for each list of integers and return a dictionary of these values
    std_dev_dict = {}
    for letter, values in letter_dict.items():
        std_dev_dict[letter] = math.sqrt(sum((x - mean)**2 for x in values) / len(values))

    return std_dev_dict
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']