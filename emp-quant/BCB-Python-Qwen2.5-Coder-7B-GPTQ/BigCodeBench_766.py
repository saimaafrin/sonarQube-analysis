import re
import collections
def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    # Check if the input string is a string
    if not isinstance(string, str):
        raise TypeError("Input string must be a string")
    
    # Check if the patterns is a list of strings
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("Patterns must be a list of strings")
    
    # Initialize a dictionary to store the counts of each pattern
    pattern_counts = collections.defaultdict(int)
    
    # Iterate over each pattern and count its occurrences in the string
    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))
    
    return dict(pattern_counts)