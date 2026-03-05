
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    """
    Counts the occurrence of specific patterns in a string.

    Parameters
    ----------
    string : str
        The string to search for patterns in.
    patterns : list of str, optional
        The patterns to search for. Defaults to ['nnn', 'aaa', 'sss', 'ddd', 'fff'].

    Returns
    -------
    dict
        A dictionary with patterns as keys and their counts as values.

    Raises
    ------
    TypeError
        If string is not a str.
        If patterns is not a list of str.
    """
    if not isinstance(string, str):
        raise TypeError('string must be a str')
    if not isinstance(patterns, list) or not all(isinstance(p, str) for p in patterns):
        raise TypeError('patterns must be a list of str')

    pattern_counts = collections.Counter()
    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))

    return pattern_counts