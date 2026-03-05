import random
import string
import collections
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
    random_strings = [
        ''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length))
        for _ in range(n_strings)
    ]

    # Count the frequency of each character across all strings
    char_freq = collections.Counter()
    for s in random_strings:
        for c in s:
            char_freq[c] += 1

    return char_freq