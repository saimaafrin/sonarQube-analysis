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

    if not test:
        return {}

    letters = test.split()
    letter_count: Dict[str, int] = {}

    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    max_occurrences = max(letter_count.values())
    repeated_letters = [letter for letter, occurrences in letter_count.items()
                         if occurrences == max_occurrences]
    return {letter: max_occurrences for letter in repeated_letters}
