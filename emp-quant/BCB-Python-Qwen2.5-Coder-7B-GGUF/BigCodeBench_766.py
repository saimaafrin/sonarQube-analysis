
import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    if not isinstance(string, str):
        raise TypeError("The input string must be a str.")
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("The patterns must be a list of str.")
    
    pattern_counts = collections.defaultdict(int)
    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))
    
    return dict(pattern_counts)