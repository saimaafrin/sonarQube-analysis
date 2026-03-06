import random
import string
import collections
def task_func(n_strings, string_length):
    """
    Generate n random strings of a specified length, count the frequency of each character across all strings, and return the result as a dictionary.

    Parameters:
    - n_strings (int): The number of random strings to generate.
    - string_length (int): The length of each random string.

    Returns:
    - dict: A dictionary containing character counts with characters as keys and their frequencies as values.

    Requirements:
    - random
    - string
    - collections

    Constants:
    - VALID_CHARACTERS: A string containing all valid characters (ASCII letters and digits) that can be used in the random strings.

    Example:
    >>> random.seed(42)
    >>> task_func(2, 3)
    {'O': 1, 'h': 1, 'b': 1, 'V': 1, 'r': 1, 'p': 1}
    """
    # Generate n random strings of a specified length
    random_strings = [random_string(string_length) for _ in range(n_strings)]

    # Count the frequency of each character across all strings
    character_counts = collections.Counter(char for string in random_strings for char in string)

    # Return the result as a dictionary
    return character_counts