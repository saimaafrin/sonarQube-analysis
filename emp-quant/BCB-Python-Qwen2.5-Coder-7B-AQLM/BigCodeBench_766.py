
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    if not isinstance(string, str):
        raise TypeError("The input string must be a string.")
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("The patterns must be a list of strings.")
    
    counts = collections.defaultdict(int)
    for pattern in patterns:
        counts[pattern] = len(re.findall(pattern, string))
    
    return dict(counts)