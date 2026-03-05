import collections
import string
import random
def task_func(length, seed=0):
    """
    Generate a random string of a given length using ASCII letters and calculate the frequency of each character.
    :param length: The length of the string to generate.
    :param seed: The seed to use for random number generation.
    :return: A dictionary with the frequency of each character in the generated string.
    """
    # Generate a random string of the given length
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    # Calculate the frequency of each character in the string
    char_freq = collections.Counter(random_string)

    # Return the frequency dictionary
    return char_freq