import random
import string
import collections
VALID_CHARACTERS = string.ascii_letters + string.digits
def task_func(n_strings, string_length):
    """
    Generate n random strings of a specified length, count the frequency of each character across all strings, and return the result as a dictionary.
    """
    # Generate n random strings
    random_strings = [
        ''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length))
        for _ in range(n_strings)
    ]

    # Count the frequency of each character
    char_counts = collections.Counter()
    for s in random_strings:
        for c in s:
            char_counts[c] += 1

    # Return the result as a dictionary
    return char_counts