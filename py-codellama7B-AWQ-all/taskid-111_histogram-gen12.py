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
    words = test.split(" ")
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    max = dict[list(dict)[0]]
    for i in dict:
        if dict[i] > max:
            max = dict[i]
    for i in dict:
        if dict[i] != max:
            del dict[i]
    return dict
