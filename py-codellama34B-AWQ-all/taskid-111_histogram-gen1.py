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

    result: Dict[str, int] = {}
    if not test:
        return result

    max_repeated_char: str = None
    max_repeated_char_count: int = 0

    for char in test:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

        if max_repeated_char_count < result[char]:
            max_repeated_char = char
            max_repeated_char_count = result[char]

    for char in result:
        if char != max_repeated_char:
            del result[char]

    return result
