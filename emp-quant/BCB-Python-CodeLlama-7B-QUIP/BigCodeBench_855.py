
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Generate n random strings of the specified length
    random_strings = [random.choice(VALID_CHARACTORS) for _ in range(n_strings)]

    # Count the frequency of each character across all strings
    char_counts = collections.Counter(random_strings)

    # Return the result as a dictionary
    return {char: count for char, count in char_counts.items()}