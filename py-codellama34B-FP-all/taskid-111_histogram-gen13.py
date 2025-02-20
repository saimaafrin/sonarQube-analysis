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

    count: Dict[str, int] = {}
    for char in test:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    
    max_count = 0
    for char in count:
        if count[char] > max_count:
            max_count = count[char]

    result = {char: count[char] for char in count if count[char] == max_count}
    return result
