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

    # Your code here
    letters = test.split()
    letter_count: Dict[str, int] = {}
    for letter in letters:
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    letter_repetition = []
    for letter in letter_count:
        if letter_count[letter] > max(letter_count.values()):
            max_repetition = letter
        letter_repetition.append(letter)
    for letter in letter_repetition:
        if letter_count[letter] == max(letter_count.values()):
            max_repetition = letter
    return {max_repetition: letter_count[max_repetition]}
