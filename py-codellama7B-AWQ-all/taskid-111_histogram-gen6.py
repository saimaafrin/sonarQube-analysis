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

    histogram = {}
    words = test.split(' ')
    for word in words:
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1
    max_count = 0
    max_value = None
    for word in histogram.keys():
        if histogram[word] > max_count:
            max_count = histogram[word]
            max_value = word
    result = {}
    result[max_value] = max_count
    return result
