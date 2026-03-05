
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    """
    Given a string, divide it at the last occurrence of "-" and count the frequency of each lowercase letter in the prefix of the string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary with the frequency of each lowercase letter.
    """
    match = LETTERS_PATTERN.match(string)
    if match:
        prefix = match.group(1)
        count = Counter(prefix)
        return {letter: count[letter] for letter in LETTERS}
    else:
        return {}