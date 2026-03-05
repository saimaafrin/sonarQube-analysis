
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    if not isinstance(string, str):
        raise TypeError("Input string must be a str.")
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("Input patterns must be a list of str.")
    
    counts = collections.defaultdict(int)
    for pattern in patterns:
        counts[pattern] = len(re.findall(pattern, string))
    
    return dict(counts)