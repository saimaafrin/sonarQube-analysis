import collections
import string
import random
def task_func(length, seed=0):
    """
    Generate a random string of a given length using ASCII letters and calculate the frequency of each character.

    Args:
        length (int): The length of the generated string.
        seed (int, optional): The random seed. Defaults to 0.

    Returns:
        dict: A dictionary with the frequency of each character in the generated string.
    """
    random.seed(seed)
    generated_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    char_freq = collections.Counter(generated_string)
    return char_freq