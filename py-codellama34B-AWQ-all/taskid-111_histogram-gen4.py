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

    dict_test = {}
    most_repetitive = ''
    count = 0
    for letter in test:
        if letter in dict_test:
            dict_test[letter] = dict_test[letter] + 1
        else:
            dict_test[letter] = 1

    for letter, occurrence in dict_test.items():
        if occurrence > count:
            count = occurrence
            most_repetitive = letter

    return {most_repetitive: count}
