
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    if not isinstance(string, str):
        raise TypeError("Input string must be a str.")
    if not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("All patterns must be strings.")

    # Initialize a counter to keep track of pattern occurrences
    pattern_counter = collections.Counter()

    # Iterate over each pattern and count its occurrences in the string
    for pattern in patterns:
        matches = re.findall(pattern, string)
        pattern_counter[pattern] = len(matches)

    return dict(pattern_counter)