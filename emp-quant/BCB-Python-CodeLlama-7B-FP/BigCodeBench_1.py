import collections
import random
import string
def task_func(length=100):
    """
    Generate a random string of the specified length composed of uppercase and lowercase letters, and then count the occurrence of each character in this string.
    The function should raise the exception for: ValueError if the length is a negative number
    The function should output with:
        dict: A dictionary where each key is a character from the generated string and the value
        is the count of how many times that character appears in the string.
    """
    if length < 0:
        raise ValueError("Length must be a non-negative number")

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    # Count the occurrence of each character in the string
    char_counts = collections.Counter(random_string)

    return char_counts