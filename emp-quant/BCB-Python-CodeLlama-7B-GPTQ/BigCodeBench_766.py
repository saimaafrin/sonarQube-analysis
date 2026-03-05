import re
import collections
def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    """
    Counts the occurrence of specific patterns in a string.
    The function should raise the exception for:
        TypeError: If string is not a str.
        TypeError: If patterns is not a list of str.
    The function should output with:
        dict: A dictionary with patterns as keys and their counts as values.
    """
    if not isinstance(string, str):
        raise TypeError('string must be a str')
    if not isinstance(patterns, list):
        raise TypeError('patterns must be a list of str')
    if not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError('patterns must be a list of str')

    pattern_counts = collections.Counter()
    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))

    return pattern_counts