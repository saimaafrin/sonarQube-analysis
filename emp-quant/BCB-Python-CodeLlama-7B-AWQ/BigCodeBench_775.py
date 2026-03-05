from string import ascii_lowercase
import re
from collections import Counter
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
def task_func(string):
    """
    Divide the string at the last occurrence of "-" and count the frequency of each lowercase letter in the prefix of the string.
    """
    match = LETTERS_PATTERN.search(string)
    if match:
        prefix = match.group(1)
        return Counter(prefix)
    else:
        return {}