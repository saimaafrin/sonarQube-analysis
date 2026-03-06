
import collections
import random
import string

def task_func(length=100):
    if length < 0:
        raise ValueError("Length must be a non-negative number")

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    # Count the occurrence of each character in the string
    char_counts = collections.Counter(random_string)

    return char_counts