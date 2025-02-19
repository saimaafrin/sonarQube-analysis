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

    dict: Dict[str, int] = {}
    max_occurrence: int = 0
    letter: str = ''
    for c in test:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
            if dict[c] > max_occurrence:
                max_occurrence = dict[c]
                letter = c
    for k in dict:
        if dict[k] < max_occurrence:
            del dict[k]
    return dict
