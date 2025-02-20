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

    words = test.split()
    letters = []
    for word in words:
        letters.append(word)

    hist = {}
    for letter in letters:
        hist[letter] = hist.get(letter, 0) + 1

    most_frequent = max(hist.values())
    most_frequent_letters = [k for k, v in hist.items() if v == most_frequent]
    return {k:v for k,v in hist.items() if k in most_frequent_letters}
