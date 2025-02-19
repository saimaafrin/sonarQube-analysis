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


    assert all(test[i] == ' ' for i in range(len(test)-1, 0, -1))
    
    letter_count: Dict[str, int] = dict()

    for letter in test:
        if letter == ' ':
            continue
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    
    max_value = max(letter_count.values())

    return {k: v for k, v in letter_count.items() if v == max_value}
