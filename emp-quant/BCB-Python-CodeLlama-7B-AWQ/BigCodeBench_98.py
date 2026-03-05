import random
import string
from collections import Counter
def task_func(num_strings, string_length):
    """
    Creates a list of random strings, each of a specified length, and counts the frequency of each character across all strings. The function then returns the characters and their frequencies sorted by frequency in descending order. The random strings are composed of ASCII lowercase characters.
    """
    # Generate a list of random strings
    random_strings = [
        ''.join(random.choice(string.ascii_lowercase) for _ in range(string_length))
        for _ in range(num_strings)
    ]

    # Count the frequency of each character in the list of strings
    char_freq = Counter(
        ''.join(random_strings)
    )

    # Sort the characters and their frequencies by frequency in descending order
    sorted_char_freq = sorted(
        char_freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_char_freq