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
    # Create a dictionary with keys from LETTERS and values as empty lists
    data = {letter: [] for letter in LETTERS}

    # Generate random integers for each key within the range 0 to 100
    for letter in LETTERS:
        data[letter].extend(random.sample(range(0, 101), random.randint(1, 10)))

    # Calculate the population standard deviation for each list of integers
    std_devs = {letter: math.sqrt(sum((x - mean) ** 2 for x in data[letter]) / len(data[letter])) for letter in LETTERS}

    return std_devs
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']