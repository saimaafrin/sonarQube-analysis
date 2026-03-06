
import re
import string
from random import choice

def task_func(n, pattern):
    """
    Generates a random string of length n that conforms to the given regular expression pattern.
    """
    while True:
        random_string = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, random_string):
            return random_string