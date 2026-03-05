
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    """
    Generate n random strings of a specified length, count the frequency of each character across all strings, and return the result as a dictionary.

    Args:
        n_strings (int): The number of random strings to generate.
        string_length (int): The length of each random string.

    Returns:
        dict: A dictionary containing character counts with characters as keys and their frequencies as values.
    """
    # Generate n random strings
    random_strings = [random.choice(VALID_CHARACTERS) for _ in range(n_strings)]

    # Count the frequency of each character across all strings
    char_counts = collections.Counter(char for string in random_strings for char in string)

    # Return the result as a dictionary
    return dict(char_counts)