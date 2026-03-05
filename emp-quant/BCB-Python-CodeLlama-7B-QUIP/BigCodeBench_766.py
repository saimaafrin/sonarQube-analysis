
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    if not isinstance(string, str):
        raise TypeError("string must be a str")
    if not isinstance(patterns, list):
        raise TypeError("patterns must be a list of str")
    pattern_counts = collections.Counter(patterns)
    for pattern in patterns:
        pattern_counts[pattern] += len(re.findall(pattern, string))
    return pattern_counts