import re
import string
from random import choice
def task_func(n, pattern):
    """
    Generates a random string of a specified length that conforms to a given regular expression pattern.
    The function repeatedly generates random strings, using both uppercase and lowercase ASCII letters, of the specified length until one matches the pattern.
    """
    while True:
        random_string = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, random_string):
            return random_string