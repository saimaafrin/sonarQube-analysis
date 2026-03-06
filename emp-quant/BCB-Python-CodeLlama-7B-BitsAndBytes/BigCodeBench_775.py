
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    """
    Divide the string at the last occurrence of "-" and count the frequency of each lowercase letter in the prefix of the string.
    """
    match = LETTERS_PATTERN.search(string)
    if match:
        prefix = match.group(1)
        counter = Counter(prefix)
        return counter
    else:
        return {}