
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    match = LETTERS_PATTERN.match(string)
    if match:
        prefix = match.group(1)
        return Counter(prefix)
    else:
        return {}