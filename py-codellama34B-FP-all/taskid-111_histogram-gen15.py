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

    # Create a dictionary of letter counts
    letter_counts = {}
    for letter in test.split(' '):
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # Create a dictionary of the letter with the most repetition
    # If several letters have the same occurrence, return all of them
    most_frequent = None
    max_count = 0
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            most_frequent = {letter: count}
        elif count == max_count:
            most_frequent[letter] = count

    return most_frequent
