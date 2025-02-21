from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """

    if len(test) == 0:
        return {}

    occurences = {}
    for char in test.split(' '):
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1

    max_count = max(occurences.values())
    result = {}
    for char, count in occurences.items():
        if count == max_count:
            result[char] = count

    return result
